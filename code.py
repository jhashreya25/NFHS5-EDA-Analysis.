# =========================
# NFHS-5 EDA – Contest Template
# Cleaned for running as a normal .py script
# =========================

import os, re, json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------- 0) Setup ----------
DATA_PATH = Path("NFHS_5_Factsheets_Data.xls")   # change to .csv or .xlsx if you convert
OUT_DIR    = Path("nfhs5_eda_outputs")
PLOTS_DIR  = OUT_DIR / "plots"
OUT_DIR.mkdir(parents=True, exist_ok=True); PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# Helper to preview DataFrames safely
def show(df, n=5, title=""):
    print("\n=== " + title + " ===")
    print(df.head(n))
    print("Shape:", df.shape)

# ---------- 1) Load data ----------
def load_data(path: Path) -> pd.DataFrame:
    ext = path.suffix.lower()
    if ext == ".csv":
        return pd.read_csv(path)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(path)   # requires xlrd for .xls
    else:
        raise ValueError("Unsupported file type. Use .csv, .xlsx, or .xls")
        
df = load_data(DATA_PATH)
print("Loaded shape:", df.shape)
print("Columns:", list(df.columns)[:10], "...")  # just first 10 columns

show(df, 5, "Raw Data Preview")

# ---------- 2) Standardize columns & detect schema ----------
def std_col(c):
    c = str(c).strip()
    c = re.sub(r"\s+", " ", c)
    return c

df.columns = [std_col(c) for c in df.columns]

# Guess typical columns
state_col = next((c for c in df.columns if std_col(c).lower() in {
    "state/ut","state","states/uts","state / ut","state name","name","States/UTs".lower()
}), None)

indicator_col = next((c for c in df.columns if "indicator" in c.lower()), None)
value_col     = None
for pref in ["Total", "Value", "All persons", "Both", "Overall", "Number", "Percent", "%"]:
    if pref in df.columns:
        value_col = pref; break

schema = "wide"
if state_col and indicator_col and value_col:
    schema = "tall"
print("Detected schema:", schema, "| state:", state_col, "| indicator:", indicator_col, "| value:", value_col)

# ---------- 3) Cleaning helpers ----------
def clean_text(x):
    if pd.isna(x): return x
    s = str(x).strip()
    s = re.sub(r"\s+", " ", s)
    return s

def to_numeric_safely(series: pd.Series) -> pd.Series:
    s1 = pd.to_numeric(series, errors="coerce")
    if s1.notna().sum() < max(3, int(0.1 * len(series))):
        s = series.astype(str).str.replace(",", "", regex=False)
        s = s.str.replace("%", "", regex=False).str.replace("−", "-", regex=False)
        s = s.str.replace("\u2013", "-", regex=False).str.replace("\u2212", "-", regex=False)
        s = s.str.replace(r"[^0-9\.\-]", "", regex=True)
        return pd.to_numeric(s, errors="coerce")
    return s1

for c in df.select_dtypes(include=["object"]).columns:
    df[c] = df[c].apply(clean_text)

# ---------- 4) Reshape tall -> wide (if needed) ----------
if schema == "tall":
    prefer = "Total" if "Total" in df.columns else value_col
    mini = df[[state_col, indicator_col, prefer]].copy()
    mini[prefer] = to_numeric_safely(mini[prefer])
    wide = mini.pivot_table(index=state_col, columns=indicator_col, values=prefer, aggfunc="mean").reset_index()
    wide.columns = [std_col(c) if isinstance(c, str) else std_col(" ".join(map(str, c))) for c in wide.columns]
else:
    wide = df.copy()

# Convert numeric columns
num_candidates = [c for c in wide.columns if c != state_col]
for c in num_candidates:
    wide[c] = to_numeric_safely(wide[c])

show(wide, 5, "Cleaned Wide Data")
wide.to_csv(OUT_DIR / "NFHS5_clean_wide.csv", index=False)
print("Saved cleaned dataset:", OUT_DIR / "NFHS5_clean_wide.csv")

# ---------- 5) Missing values ----------
missing = (wide.isna().sum().to_frame("missing_count")
           .assign(missing_pct=lambda x: (x["missing_count"] / len(wide) * 100).round(2))
           .sort_values("missing_pct", ascending=False).reset_index().rename(columns={"index": "column"}))
show(missing, 10, "Missing Values")

# ---------- 6) Duplicates ----------
dups = wide[wide.duplicated(keep=False)]
print("\nDuplicate rows:", dups.shape[0])

# ---------- 7) Noise checks ----------
notes = []
if state_col in wide.columns:
    uniq = pd.Series(wide[state_col].unique()).dropna().map(clean_text)
    if uniq.duplicated().any():
        notes.append("Potential inconsistent State/UT naming")

pct_cols = [c for c in wide.columns if any(k in c.lower() for k in ["%", "percent", "percentage", "per cent"])]
range_issues = []
for c in pct_cols:
    s = wide[c]
    bad = wide[(s < 0) | (s > 100)]
    if not bad.empty:
        range_issues.append((c, bad.shape[0]))
print("Percentage-like range issues:", range_issues if range_issues else "None")

# ---------- 8) Outliers (IQR) ----------
num_cols = wide.select_dtypes(include=[np.number]).columns.tolist()
outlier_rows = []
for c in num_cols:
    s = wide[c].dropna()
    if s.nunique() < 5: continue
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    mask = (wide[c] < lo) | (wide[c] > hi)
    outlier_rows.append({"column": c, "outlier_count": int(mask.sum())})
outlier_summary = pd.DataFrame(outlier_rows).sort_values("outlier_count", ascending=False)
show(outlier_summary, 10, "Outlier Summary")

# ---------- 9) Distributions ----------
def save_hist(col):
    series = wide[col].dropna()
    plt.figure()
    plt.hist(series, bins=12)
    plt.title(f"Histogram: {col}")
    plt.xlabel(col); plt.ylabel("Frequency")
    p = PLOTS_DIR / f"hist_{re.sub(r'[^a-zA-Z0-9]+','_',col)}.png"
    plt.tight_layout(); plt.savefig(p); plt.close(); return p

def save_box(col):
    series = wide[col].dropna()
    plt.figure()
    plt.boxplot(series, vert=True)
    plt.title(f"Boxplot: {col}")
    plt.ylabel(col)
    p = PLOTS_DIR / f"box_{re.sub(r'[^a-zA-Z0-9]+','_',col)}.png"
    plt.tight_layout(); plt.savefig(p); plt.close(); return p

eligible = []
for c in num_cols:
    miss = wide[c].isna().mean()
    if miss < 0.2:
        eligible.append((c, np.nanvar(wide[c].values)))
eligible = sorted(eligible, key=lambda x: x[1], reverse=True)[:6]
dist_cols = [c for c, _ in eligible]

hist_paths = [save_hist(c) for c in dist_cols]
box_paths  = [save_box(c) for c in dist_cols]
print("Saved histograms:", hist_paths)
print("Saved boxplots:", box_paths)

# ---------- 10) Correlation heatmap ----------
top20 = sorted([(c, np.nanvar(wide[c].values)) for c in num_cols if wide[c].isna().mean() < 0.3],
               key=lambda x: x[1], reverse=True)[:20]
corr_cols = [c for c, _ in top20]
corr = wide[corr_cols].corr()

plt.figure(figsize=(8,6))
plt.imshow(corr, aspect="auto")
plt.colorbar()
plt.xticks(range(len(corr_cols)), corr_cols, rotation=90)
plt.yticks(range(len(corr_cols)), corr_cols)
plt.title("Correlation Heatmap")
corr_path = PLOTS_DIR / "correlation_heatmap.png"
plt.tight_layout(); plt.savefig(corr_path); plt.close()
print("Saved correlation heatmap:", corr_path)

# ---------- 11) Auto Summary ----------
insights = []
def add_top_bottom(col, nice=None):
    if col in wide.columns and col in num_cols:
        sub = wide[[state_col, col]].dropna()
        if sub.empty: return
        nice = nice or col
        top5 = sub.sort_values(col, ascending=False).head(5).values.tolist()
        bot5 = sub.sort_values(col, ascending=True).head(5).values.tolist()
        insights.append(f"Top 5 states for {nice}: " + "; ".join([f"{s}: {round(v,2)}" for s,v in top5]))
        insights.append(f"Bottom 5 states for {nice}: " + "; ".join([f"{s}: {round(v,2)}" for s,v in bot5]))

stunting = next((c for c in wide.columns if "stunting" in c.lower()), None)
inst_del = next((c for c in wide.columns if "institutional" in c.lower() and "deliver" in c.lower()), None)
immun    = next((c for c in wide.columns if "immunization" in c.lower() or "immunisation" in c.lower()), None)
san      = next((c for c in wide.columns if "sanitation" in c.lower() or "toilet" in c.lower()), None)

if stunting: add_top_bottom(stunting, "Child Stunting (%)")
if inst_del: add_top_bottom(inst_del, "Institutional Deliveries (%)")
if immun:    add_top_bottom(immun, "Child Immunization (%)")
if san:      add_top_bottom(san, "Sanitation/Toilet Access (%)")

# save summary
(OUT_DIR / "EDA_summary.txt").write_text("\n".join(f"- {x}" for x in insights), encoding="utf-8")
print("\n=== Key Insights (auto) ===")
for line in insights:
    print(line)

print("\nAll outputs saved in:", OUT_DIR.resolve())
