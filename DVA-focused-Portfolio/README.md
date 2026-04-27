# DVA-Focused Portfolio



## Project Summary

**Title:** Student Mental Health & Burnout — Data-Driven Risk Analysis  
**Sector:** EdTech / Higher Education  
**Tools:** Python, pandas, scipy, statsmodels, Tableau Public, GitHub  
**Dataset:** 1,000,000 student records × 20 variables  

---

## Portfolio Case Study Template

### Problem Statement
Universities lack a systematic, data-driven method to identify students at risk of burnout and dropout before the situation becomes critical. This project analyses 1 million student records to surface the key drivers of burnout and build a Tableau dashboard that enables welfare teams to act early.

### Dataset
- 1,000,000 rows, 20 columns
- Variables: stress, anxiety, depression, sleep, physical activity, social support, screen time, academic performance, burnout score, dropout risk
- Source: Kaggle (synthetic simulation dataset)

### What I Did
- Built a full ETL pipeline in Python (extraction → cleaning → EDA → statistical analysis → Tableau export)
- Cleaned and validated 1M rows: null imputation, range clipping, categorical standardisation
- Performed EDA: distributions, correlation heatmaps, segment profiling, academic year trends
- Ran statistical tests: Welch's t-test, one-way ANOVA, OLS regression, logistic regression
- Engineered 13 derived columns for Tableau: normalised scores, binned dimensions, sector labels
- Built an interactive Tableau Public dashboard with KPI cards, filters, and drill-downs

### Key Findings
- Stress, anxiety, and depression are the top 3 burnout predictors (OLS regression, R² ≈ 0.65)
- Students sleeping under 6 hours show burnout scores significantly above the mean
- Social support is the strongest protective factor against burnout
- Burnout escalates most sharply at the Year 2 → Year 3 transition
- Only 1.5% of students are High risk, but they carry dropout risk 4–5× the average

### Recommendations
1. Deploy semester-start stress screening — flag students scoring >7/10 for early counselling
2. Launch sleep hygiene campaigns targeting the Short sleep sector
3. Expand peer mentoring for Year 3 and 4 students

### Links
- GitHub Repository: https://github.com/bhavish-codes/Tablue
- Dashboard: https://github.com/bhavish-codes/Tablue/tree/main/tableau/screenshots

---

## Portfolio Bullet Points 

- Analysed 1M student records to identify burnout risk drivers using Python (pandas, scipy, statsmodels); built OLS and logistic regression models achieving R² ≈ 0.65
- Engineered a 33-column Tableau-ready dataset with normalised scores, binned dimensions, and sector labels from a 20-column raw source
- Delivered an interactive Tableau Public dashboard enabling academic administrators to segment students by risk level, sleep pattern, and academic year
- Identified sleep deprivation and low social support as the top modifiable risk factors for student burnout across 1 million records
