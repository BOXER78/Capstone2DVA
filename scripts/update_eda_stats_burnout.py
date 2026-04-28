import json
from pathlib import Path

nb_path = Path("notebooks/03_eda.ipynb")
with open(nb_path, "r") as f:
    nb = json.load(f)

new_cells = nb["cells"][:4]
cells_to_add = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 1. Distribution of Key Variables\n"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "fig, axes = plt.subplots(1, 3, figsize=(18, 5))\n",
            "sns.histplot(df['cgpa'], bins=20, ax=axes[0], color='skyblue').set_title('CGPA Distribution')\n",
            "sns.histplot(df['daily_study_hours'], bins=15, ax=axes[1], color='lightgreen').set_title('Daily Study Hours')\n",
            "sns.countplot(data=df, x='burnout_level', ax=axes[2], palette='salmon').set_title('Burnout Level Count')\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 2. Correlation Matrix\n"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.figure(figsize=(10, 8))\n",
            "numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns\n",
            "corr = df[numeric_cols].corr()\n",
            "sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')\n",
            "plt.title('Correlation Matrix')\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 3. Burnout vs Study Hours\n"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.figure(figsize=(8, 6))\n",
            "sns.boxplot(data=df, x='burnout_level', y='daily_study_hours', palette='Set2')\n",
            "plt.title('Study Hours by Burnout Level')\n",
            "plt.show()"
        ]
    }
]
nb["cells"] = new_cells + cells_to_add
with open(nb_path, "w") as f:
    json.dump(nb, f, indent=1)

nb_path2 = Path("notebooks/04_statistical_analysis.ipynb")
with open(nb_path2, "r") as f:
    nb2 = json.load(f)
new_cells2 = nb2["cells"][:3]
cells_to_add2 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 1. T-Test: Sleep Hours by Gender\n"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "group_m = df[df['gender'] == 'male']['daily_sleep_hours']\n",
            "group_f = df[df['gender'] == 'female']['daily_sleep_hours']\n",
            "t_stat, p_val = stats.ttest_ind(group_m.dropna(), group_f.dropna(), equal_var=False)\n",
            "print(f\"T-Statistic: {t_stat:.4f}, P-Value: {p_val:.4e}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 2. Correlation: Academic Pressure vs Burnout Score (Anxiety)\n"]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "corr, p_val = stats.pearsonr(df['academic_pressure_score'].dropna(), df['anxiety_score'].dropna())\n",
            "print(f\"Pearson Corr: {corr:.4f}, P-Value: {p_val:.4e}\")"
        ]
    }
]
nb2["cells"] = new_cells2 + cells_to_add2
with open(nb_path2, "w") as f:
    json.dump(nb2, f, indent=1)
