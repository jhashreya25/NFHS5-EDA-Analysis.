# NFHS-5 Data Analysis (Exploratory Data Analysis)

##  Overview
This project analyzes the **NFHS-5 (National Family Health Survey)** dataset using Python.  
The goal is to **clean, explore, visualize, and extract insights** from the dataset for a data analysis contest.  

## Steps Performed
1. **Data Cleaning**
   - Removed missing values & duplicates
   - Handled noise and outliers
   - Standardized column names

2. **Exploratory Data Analysis (EDA)**
   - Identified missing data patterns
   - Detected outliers in key health indicators
   - Checked distributions and relationships between variables

3. **Visualizations**
   - Histograms for distributions
   - Boxplots for outliers
   - Correlation heatmap for relationships
   - State-wise comparisons

4. **Key Insights**
   - Sanitation and toilet access is **highest in Lakshadweep & Kerala**, but **lowest in Bihar & Ladakh**.
   - Child nutrition indicators (stunting, wasting, underweight) show alarming trends in multiple states.
   - Internet usage shows a **large gender gap** (men > women).
   - Health insurance coverage remains **low in most states**, especially rural areas.
   - Out-of-pocket expenditure for childbirth varies widely between states.

5. **Outputs**
   -  `nfhs5_eda_outputs/plots/` → graphs & charts  
   -  `nfhs5_eda_outputs/NFHS5_clean_wide.csv` → cleaned dataset  

## Example Visuals with Insights

### Correlation Heatmap
![Correlation Heatmap](https://raw.githubusercontent.com/jhashreya25/NFHS5-EDA-Analysis./refs/heads/main/correlation_heatmap.png)  
Insight:
Strong positive correlation between female literacy, internet use, and women’s empowerment indicators (e.g., household decision-making).

Child nutrition and sanitation are strongly correlated — better toilet access links to lower stunting/wasting rates.

Negative correlations show that early marriage and low literacy go hand-in-hand with poor maternal/child health.

Implication: Education and empowerment policies can directly improve health outcomes.
![Household Survey Distribution] https://raw.githubusercontent.com/jhashreya25/NFHS5-EDA-Analysis./refs/heads/main/hist_Number_of_Households_surveyed.png
 Insight:
Distribution shows wide variation across states.

Larger states like Uttar Pradesh and Maharashtra had very high household sample sizes, while smaller UTs like Lakshadweep had very low counts.

This indicates that survey data is representative at both state and national levels, but comparisons between big states and small UTs must consider sample size differences.

👶 Sex Ratio at Birth (last 5 years)

File: box_Sex_ratio_at_birth_for_children_born_in_the_last_five_years_females_per_1_000_males_.png
📊 Insight:

Median sex ratio at birth is close to 950–970 females per 1000 males, but there are significant outliers.

Some states (e.g., Punjab, Haryana) show lower ratios (<900), highlighting persistent gender imbalance.

States like Kerala perform much better, closer to natural ratio (~1000).

Implication: Despite progress, certain regions still show gender bias at birth.

💰 Out-of-Pocket Delivery Costs

File: hist_Average_out_of_pocket_expenditure_per_delivery_in_a_public_health_facility_for_last_birth_in_the_5_years_before_the_survey_Rs_.png
📊 Insight:

Most deliveries in public facilities cost between ₹1,000–₹5,000, but some states report much higher averages.

Outliers suggest inequities — in some regions, public health deliveries are not fully free, creating barriers for poor families.

Implication: Strengthening Janani Suraksha Yojana (JSY) and similar schemes is still crucial.

### Sanitation Access
![Sanitation Boxplot](nfhs5_eda_outputs/plots/box_Population_living_in_households_that_use_an_improved_sanitation_facility2.png)  
 **Insight:** Lakshadweep and Kerala lead with ~100% sanitation access, while Bihar and Ladakh lag below 50%. This highlights regional inequality.

### Internet Usage (Gender Gap)
![Internet Usage](nfhs5_eda_outputs/plots/box_Women_age_15_49_years_who_have_ever_used_the_internet.png)  
 **Insight:** Men consistently report higher internet use than women. The digital gender divide is starkest in northern states.

### Child Nutrition (Stunting)
![Child Stunting](nfhs5_eda_outputs/plots/box_Children_under_5_years_who_are_stunted.png)  
 **Insight:** Stunting rates remain high in several states, reflecting chronic malnutrition. Southern states perform better than northern states.

### Out-of-Pocket Delivery Cost
![Delivery Cost](nfhs5_eda_outputs/plots/box_Average_out_of_pocket_expenditure_per_delivery_in_a_public_health_facility.png)  
 **Insight:** Wide variation across states: in some, deliveries cost <₹1,000, while in others, >₹10,000. This reflects inequality in access to affordable healthcare.

## Key Takeaways

1. **Regional Inequality:** Southern states (Kerala, Tamil Nadu) perform much better in sanitation, healthcare, and child nutrition compared to northern states (Bihar, Uttar Pradesh, Ladakh).  
2. **Digital Divide:** A clear gender gap exists in internet usage — men consistently outpace women, highlighting barriers for women in accessing technology.  
3. **Healthcare Costs:** Out-of-pocket expenditure for delivery shows huge variation across states, pointing to inequality in affordable maternal healthcare.  
4. **Nutrition Challenge:** Child stunting and anaemia remain high in many states despite progress in education and sanitation — showing nutrition is still a bottleneck.  
5. **Correlation Story:** Education of women strongly links to better child health and sanitation access — investing in women’s education pays off across multiple indicators.

---

 **Big Picture:** India has made progress in healthcare and sanitation, but inequality (regional + gender) is the biggest challenge. Closing these gaps is key to achieving equitable development.



```markdown
![Correlation Heatmap](nfhs5_eda_outputs/plots/correlation_heatmap.png)
