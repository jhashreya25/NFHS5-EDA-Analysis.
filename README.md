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
![Correlation Heatmap](nfhs5_eda_outputs/plots/correlation_heatmap.png)  
 **Insight:** Strong correlations exist between women’s education, sanitation access, and child health outcomes. States with higher education levels tend to have better sanitation and lower child mortality.

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
