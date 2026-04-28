import json
from pathlib import Path

nb_path = Path("notebooks/03_eda.ipynb")
with open(nb_path, "r") as f:
    nb = json.load(f)

# Keep the first 4 cells (Imports, load data, describe)
new_cells = nb["cells"][:4]

# Add EDA visualizations
cells_to_add = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 1. Distribution of Key Variables\n",
            "Let's look at the distribution of Age, Daily Social Media Hours, and Stress Level."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "fig, axes = plt.subplots(1, 3, figsize=(18, 5))\n",
            "sns.histplot(df['age'], bins=10, ax=axes[0], color='skyblue').set_title('Age Distribution')\n",
            "sns.histplot(df['daily_social_media_hours'], bins=15, ax=axes[1], color='lightgreen').set_title('Daily Social Media Hours')\n",
            "sns.histplot(df['stress_level'], bins=10, ax=axes[2], color='salmon').set_title('Stress Level Distribution')\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 2. Correlation Matrix\n",
            "Checking how numeric variables like screen time, sleep, and mental health indicators correlate with each other."
        ]
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
            "sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)\n",
            "plt.title('Correlation Matrix')\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "**Insight:** Look for strong positive correlations between `daily_social_media_hours`, `stress_level`, and `anxiety_level`. Also check if `sleep_hours` is negatively correlated with these metrics.\n",
            "\n",
            "## 3. Stress Level by Platform Usage\n",
            "Does the choice of social media platform impact stress levels?"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.figure(figsize=(8, 6))\n",
            "sns.boxplot(data=df, x='platform_usage', y='stress_level', palette='Set2')\n",
            "plt.title('Stress Level vs. Platform Usage')\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 4. Depression Label vs Social Media Hours\n",
            "How does social media usage differ between those labeled with depression vs those without?"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.figure(figsize=(8, 6))\n",
            "sns.violinplot(data=df, x='depression_label', y='daily_social_media_hours', palette='pastel')\n",
            "plt.title('Daily Social Media Hours by Depression Label')\n",
            "plt.xticks([0, 1], ['No Depression (0)', 'Depression (1)'])\n",
            "plt.show()"
        ]
    }
]

nb["cells"] = new_cells + cells_to_add

with open(nb_path, "w") as f:
    json.dump(nb, f, indent=1)

print("Updated 03_eda.ipynb successfully.")
