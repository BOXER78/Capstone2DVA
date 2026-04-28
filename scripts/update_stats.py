import json
from pathlib import Path

nb_path = Path("notebooks/04_statistical_analysis.ipynb")
with open(nb_path, "r") as f:
    nb = json.load(f)

new_cells = nb["cells"][:3]

cells_to_add = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 1. T-Test: Stress Level by Depression Label\n",
            "Are stress levels significantly different between teenagers labeled with depression vs those who are not?"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "group_depressed = df[df['depression_label'] == 1]['stress_level']\n",
            "group_not_depressed = df[df['depression_label'] == 0]['stress_level']\n",
            "\n",
            "t_stat, p_val = stats.ttest_ind(group_depressed, group_not_depressed, equal_var=False)\n",
            "print(f\"T-Statistic: {t_stat:.4f}\")\n",
            "print(f\"P-Value: {p_val:.4e}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "**Interpretation:** A very low p-value (typically < 0.05) indicates that there is a statistically significant difference in stress levels between the two groups. In a business context, this validates stress as a strong proxy or predictor for depression.\n",
            "\n",
            "## 2. Pearson Correlation: Social Media Hours vs. Stress Level"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "corr, p_val = stats.pearsonr(df['daily_social_media_hours'], df['stress_level'])\n",
            "print(f\"Pearson Correlation: {corr:.4f}\")\n",
            "print(f\"P-Value: {p_val:.4e}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "**Interpretation:** A positive correlation implies that as social media usage increases, stress levels tend to increase as well. This supports the recommendation for limiting screen time.\n",
            "\n",
            "## 3. T-Test: Daily Social Media Hours by Gender"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "group_male = df[df['gender'] == 'male']['daily_social_media_hours']\n",
            "group_female = df[df['gender'] == 'female']['daily_social_media_hours']\n",
            "\n",
            "t_stat, p_val = stats.ttest_ind(group_male, group_female, equal_var=False)\n",
            "print(f\"Male Avg: {group_male.mean():.2f} hours\")\n",
            "print(f\"Female Avg: {group_female.mean():.2f} hours\")\n",
            "print(f\"T-Statistic: {t_stat:.4f}\")\n",
            "print(f\"P-Value: {p_val:.4e}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "**Interpretation:** If the p-value is significant, it means one gender uses social media significantly more than the other, allowing stakeholders to target specific demographics for intervention."
        ]
    }
]

nb["cells"] = new_cells + cells_to_add

with open(nb_path, "w") as f:
    json.dump(nb, f, indent=1)

print("Updated 04_statistical_analysis.ipynb successfully.")
