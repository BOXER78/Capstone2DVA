# Data Dictionary

## Dataset Summary

| Item | Details |
|---|---|
| Dataset name | Student Mental Health & Burnout Dataset |
| Source | Kaggle — synthetic student mental health simulation dataset |
| Direct link | https://www.kaggle.com/datasets/adilshamim8/student-mental-health-and-burnout-dataset |
| Raw file name | `student_mental_health_burnout_1M.csv` |
| Processed file | `data/processed/cleaned_dataset.csv` |
| Tableau-ready file | `data/processed/burnout_sampled.csv` |
| Last updated | April 2026 |
| Rows | 1,000,000 |
| Columns (raw) | 20 |
| Columns (Tableau-ready) | 33 |
| Granularity | One row per student observation |

---

## Raw Column Definitions

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| `age` | int | Student age in years | `23` | EDA, Tableau | Clipped to range 17–29; cast to int |
| `gender` | string | Student gender identity | `Male` | EDA, Tableau filter | Title-cased; values: Male, Female, Other |
| `academic_year` | int | Year of study (1 = first year, 4 = final year) | `2` | EDA, Tableau filter | Clipped to 1–4; cast to int |
| `study_hours_per_day` | float | Average hours spent studying per day | `5.60` | EDA, KPI, Tableau | Clipped to 0–24 |
| `exam_pressure` | float | Self-reported exam pressure score (0–10) | `6.49` | EDA, KPI, Tableau | Clipped to 0–10 |
| `academic_performance` | float | Academic performance score (0–100) | `68.41` | EDA, KPI, Tableau | Clipped to 0–100 |
| `stress_level` | float | Self-reported stress level (0–10) | `4.12` | EDA, KPI, Tableau | Clipped to 0–10 |
| `anxiety_score` | float | Anxiety severity score (0–10) | `2.28` | EDA, KPI, Tableau | Clipped to 0–10 |
| `depression_score` | float | Depression severity score (0–10) | `1.99` | EDA, KPI, Tableau | Clipped to 0–10 |
| `sleep_hours` | float | Average sleep hours per night | `6.88` | EDA, KPI, Tableau | Clipped to 0–12 |
| `physical_activity` | float | Physical activity level score (0–10) | `2.73` | EDA, KPI, Tableau | Clipped to 0–10 |
| `social_support` | float | Perceived social support score (0–10) | `6.47` | EDA, KPI, Tableau | Clipped to 0–10 |
| `screen_time` | float | Daily screen time in hours | `4.99` | EDA, KPI, Tableau | Clipped to 0–16 |
| `internet_usage` | float | Daily internet usage in hours | `4.98` | EDA, Tableau | Clipped to 0–16 |
| `financial_stress` | float | Financial stress score (0–10) | `3.45` | EDA, KPI, Tableau | Clipped to 0–10 |
| `family_expectation` | float | Perceived family expectation pressure (0–10) | `3.59` | EDA, KPI, Tableau | Clipped to 0–10 |
| `burnout_score` | float | Overall burnout severity score (0–10) | `2.04` | EDA, KPI, Tableau | Clipped to 0–10; primary outcome variable |
| `mental_health_index` | float | Composite mental health index (0–10, higher = better) | `7.07` | EDA, KPI, Tableau | Clipped to 0–10 |
| `risk_level` | string | Categorical risk classification | `Low` | EDA, Tableau filter | Title-cased; values: Low, Medium, High |
| `dropout_risk` | float | Predicted dropout risk score (0–10) | `1.75` | EDA, KPI, Tableau | Clipped to 0–10 |

---

## Derived Columns (added in `05_final_load_prep.ipynb`)

| Derived Column | Logic | Business Meaning |
|---|---|---|
| `Anxiety` | Alias of `Anxiety Score` | Duplicate field required by Tableau schema for dimension/measure split |
| `Depression` | Alias of `Depression Score` | Duplicate field required by Tableau schema for dimension/measure split |
| `Anxiety Norm` | `(Anxiety Score − min) / (max − min)` | Normalised 0–1 scale for cross-metric radar and composite charts |
| `Depression Norm` | `(Depression Score − min) / (max − min)` | Normalised 0–1 scale |
| `Physical Norm` | `(Physical Activity − min) / (max − min)` | Normalised 0–1 scale |
| `Sleep Norm` | `(Sleep Hours − min) / (max − min)` | Normalised 0–1 scale |
| `Support Norm` | `(Social Support − min) / (max − min)` | Normalised 0–1 scale |
| `Count anxiety` | Constant `1` per row | Enables COUNT aggregation in Tableau without a separate row-count field |
| `Sleep Hours (bin)` | pd.cut into `<4h`, `4-6h`, `6-7h`, `7-8h`, `8-10h`, `10-12h` | Binned axis for sleep distribution charts in Tableau |
| `Study Hours Per Day (bin)` | pd.cut into `0-2h`, `2-4h`, `4-6h`, `6-8h`, `8-10h`, `10h+` | Binned axis for study hours distribution charts |
| `Family Expectation (bin)` | pd.cut into `0-2`, `2-4`, `4-6`, `6-8`, `8-10` | Binned dimension for family pressure segmentation |
| `Screen time sectors` | `Low` (0–4h), `Medium` (4–8h), `High` (8h+) | Categorical filter for screen time segmentation |
| `Sleep sectors` | `Short` (<6h), `Normal` (6–8h), `Long` (>8h) | Categorical filter for sleep quality segmentation |

---

## Key Statistics (cleaned dataset)

| Metric | Value |
|---|---|
| Total students | 1,000,000 |
| Age range | 17–29 |
| Gender split | Female 48.0%, Male 47.9%, Other 4.0% |
| Risk Level split | Low 76.7%, Medium 21.8%, High 1.5% |
| Mean Burnout Score | 1.784 / 10 |
| Mean Stress Level | 4.246 / 10 |
| Mean Anxiety Score | 2.986 / 10 |
| Mean Depression Score | 1.275 / 10 |
| Mean Dropout Risk | 1.325 / 10 |
| Mean Mental Health Index | 7.023 / 10 |

---

## Data Quality Notes

- No missing values remain after median/mode imputation in `02_cleaning.ipynb`.
- No duplicate rows were found in the raw dataset.
- All numeric columns were clipped to their valid domain ranges — no rows were dropped.
- The dataset is synthetic (simulation-generated); distributions are smooth and may not reflect real-world skew.
- `risk_level` has three values (Low, Medium, High), not two as initially assumed.
- `gender` includes an `Other` category (~4% of records) in addition to Male and Female.
- `burnout_score` and `dropout_risk` are heavily right-skewed — most students score low, with a small high-risk tail.
