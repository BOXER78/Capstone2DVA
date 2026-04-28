import json
import os

# 1. Update README
readme_path = "README.md"
with open(readme_path, "r") as f:
    readme = f.read()

readme = readme.replace("Teenager Mental Health Analysis", "Student Mental Health & Burnout Analysis")
readme = readme.replace("1,201", "150,001")
readme = readme.replace("13", "20")
readme = readme.replace("https://www.kaggle.com/datasets/algozee/teenager-menthal-healy", "student_mental_health_burnout.csv")
readme = readme.replace("daily_social_media_hours", "daily_study_hours")
readme = readme.replace("Hours spent on social media", "Hours spent studying")
readme = readme.replace("depression_label", "burnout_level")
readme = readme.replace("Indicator of depression", "Target variable for burnout segmentation")
readme = readme.replace("platform_usage", "course")
readme = readme.replace("Platforms used (Instagram, TikTok)", "Course enrolled in")

with open(readme_path, "w") as f:
    f.write(readme)

# 2. Update Data Dictionary
dd_path = "docs/data_dictionary.md"
dd_content = """# Data Dictionary: Student Mental Health & Burnout Dataset

| Column Name | Data Type | Description |
|---|---|---|
| `student_id` | Numeric | Unique ID |
| `age` | Numeric | Age of student |
| `gender` | Categorical | Gender |
| `course` | Categorical | Course enrolled |
| `year` | Categorical | Year of study |
| `daily_study_hours` | Numeric | Hours of study daily |
| `daily_sleep_hours` | Numeric | Hours of sleep daily |
| `screen_time_hours` | Numeric | Hours of screen time |
| `stress_level` | Categorical | Low/Medium/High |
| `anxiety_score` | Numeric | 1-10 |
| `depression_score` | Numeric | 1-10 |
| `academic_pressure_score` | Numeric | 1-10 |
| `financial_stress_score` | Numeric | 1-10 |
| `social_support_score` | Numeric | 1-10 |
| `physical_activity_hours` | Numeric | Hours |
| `sleep_quality` | Categorical | Poor/Average/Good |
| `attendance_percentage` | Numeric | Percentage |
| `cgpa` | Numeric | GPA |
| `internet_quality` | Categorical | Poor/Average/Good |
| `burnout_level` | Categorical | Low/High/Medium |
"""
with open(dd_path, "w") as f:
    f.write(dd_content)

# 3. Notebooks update
for nb_file in ["notebooks/01_extraction.ipynb", "notebooks/02_cleaning.ipynb"]:
    with open(nb_file, "r") as f:
        nb = json.load(f)
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            for i, line in enumerate(cell["source"]):
                cell["source"][i] = line.replace("Teen_Mental_Health_Dataset.csv", "student_mental_health_burnout.csv")
    with open(nb_file, "w") as f:
        json.dump(nb, f, indent=1)
