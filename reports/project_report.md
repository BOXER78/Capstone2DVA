# Student Mental Health & Burnout Analysis - Final Project Report

## 1. Cover Page
- **Project Title:** Student Mental Health & Burnout Analysis
- **Sector:** Education / Healthcare
- **Team ID and Team Members:** [To be filled]
- **Faculty Mentor:** [To be filled]
- **Institute:** Newton School of Technology
- **Submission Date:** [To be filled]

## 2. Executive Summary
- **Problem:** Student burnout and mental health struggles are peaking due to academic pressure, financial stress, and sleep deprivation.
- **Approach:** Analyzed a massive dataset of 150,001 students using Python to extract core insights on burnout indicators.
- **Key Insights:** Burnout levels strongly correlate with high academic pressure, low sleep quality, and high anxiety scores.
- **Key Recommendations:** Universities must improve access to mental health resources and re-evaluate academic loads to prevent systemic student burnout.

## 3. Sector and Business Context
- **Sector Overview:** Higher Education and EdTech.
- **Decision-Maker:** University administrators, academic advisors, and student welfare teams.
- **Why this matters:** Burnout leads to university dropouts, lower CGPA, and severe long-term mental health disorders.

## 4. Problem Statement and Objectives
- **Formal Definition:** To identify the leading predictors of high burnout levels among university students across various courses.
- **Scope:** 150,001 students evaluating their sleep, study hours, financial stress, and academic pressure.
- **Success Criteria:** Identify the top 3 statistically significant drivers of student burnout.

## 5. Data Description
- **Source:** Kaggle Dataset (Student Mental Health)
- **Size:** 150,001 rows, 20 columns
- **Key Columns:** `daily_study_hours`, `burnout_level`, `anxiety_score`, `academic_pressure_score`, `sleep_quality`
- **Quality:** Excellent, requiring standard ETL for column naming and spacing.

## 6. Cleaning and Transformation
- **Steps:** Snake_case normalization, dropped duplicates, standardized string columns.
- **Output:** Cleaned dataset exported for EDA and Tableau.

## 7. KPI Framework
- **Burnout Prevalence (%):** Percentage of students in the "High" burnout category.
- **Average Anxiety Score (1-10):** High anxiety indicates risk.
- **Average Sleep Hours:** Baseline metric for physical recovery.

## 8. Exploratory Analysis
- **Trends:** CGPA is normally distributed; higher study hours don't linearly translate to better mental health.
- **Visuals:** Generated correlation heatmaps and boxplots mapping Burnout Level against Daily Study Hours in `03_eda.ipynb`.

## 9. Statistical Analysis
- **Method Used:** Pearson Correlation and T-Tests.
- **Results:** High academic pressure strongly correlates with high anxiety scores.
- **Interpretation:** The pressure to perform academically is a direct mathematical driver of student anxiety.

## 10. Dashboard Walkthrough
- *(To be completed after Tableau dashboard is built)*

## 11. Key Insights
1. **Academic Pressure = Anxiety:** There is a direct statistical correlation between academic pressure and reported anxiety scores.
2. **Burnout Segment:** Students reporting "High" burnout levels often show poor sleep quality and higher average study hours.
3. **Financial Stress:** Adds a significant compounding factor to overall stress levels.
4. **Social Support:** High social support acts as a buffer, slightly lowering depression scores.
5. **Course Variance:** BTech and MBA students show varying baseline stress compared to other courses.

## 12. Recommendations
1. **Academic Load Re-evaluation:** Departments must audit coursework volume to ensure it doesn't cross the threshold into high academic pressure.
2. **Financial Aid Expansion:** Introduce micro-grants to reduce the financial stress compounding student burnout.
3. **Mandatory Wellness Seminars:** Equip students with time-management and stress-regulation tools in their 1st year.

## 13. Limitations and Next Steps
- **Limitations:** Self-reported scale metrics (1-10) are subjective.
- **Next Steps:** Implement a pilot wellness program for high-risk BTech students and track burnout levels over 1 semester.

## 14. Contribution Matrix
- *(Matches GitHub commits)*
