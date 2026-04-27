# DVA-Oriented Resume



## Project Details for Resume

**Project Title:** Student Mental Health & Burnout — Data-Driven Risk Analysis  
**Sector:** EdTech / Higher Education  
**Tools:** Python, Jupyter Notebooks, pandas, scipy, statsmodels, Tableau Public, GitHub  
**Dataset:** 1,000,000 student records × 20 variables  
**Duration:** 2 weeks  

---

## Resume Bullet Templates by Role

### Data Lead / ETL Lead
- Built a Python ETL pipeline (pandas, `etl_pipeline.py`) to clean and validate 1,000,000 student records; applied median imputation, range clipping, and categorical standardisation with zero data loss
- Engineered 13 derived columns for Tableau including min-max normalised scores, binned dimensions (sleep, study hours, family expectation), and sector labels (screen time, sleep quality)

### EDA Lead
- Performed exploratory data analysis on 1M student records using pandas, matplotlib, and seaborn; produced correlation heatmaps, distribution plots, and segment-level profiling across gender, academic year, and risk level
- Identified sleep deprivation (<6h) and low social support as the strongest modifiable risk factors for student burnout

### Analysis Lead
- Applied Welch's t-test, one-way ANOVA, OLS multiple regression (R² ≈ 0.65), and logistic regression to quantify burnout predictors and validate segment-level differences with statistical significance
- Found stress level, anxiety, and depression to be the top 3 burnout predictors; sleep hours and social support as the strongest protective factors

### Visualization Lead
- Built an interactive Tableau Public dashboard with KPI summary cards, risk-level drill-downs, and filters for gender, academic year, sleep sector, and screen time sector

### Strategy Lead / Report Lead
- Translated statistical findings into 5 actionable business recommendations for academic welfare teams, including semester-start stress screening and peer mentoring expansion
- Authored the full project report covering problem framing, data engineering, KPI framework, statistical analysis, and recommendations

- **Languages:** Python
- **Libraries:** pandas, numpy, matplotlib, seaborn, scipy, statsmodels
- **Tools:** Jupyter Notebooks, Tableau Public, GitHub
- **Techniques:** ETL pipeline design, EDA, hypothesis testing, OLS regression, logistic regression, data visualisation, KPI design
- **Domain:** EdTech, student mental health analytics, higher education risk modelling
