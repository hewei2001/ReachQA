import matplotlib.pyplot as plt
import numpy as np

# List of skyscrapers
skyscrapers = ['Burj Khalifa', 'Shanghai Tower', 'Abraj Al Bait', 'Ping An\nFinance Centre', 'Lotte\nWorld Tower']

# Stress test scores data over a decade
stress_scores = [
    [85, 88, 90, 87, 85, 89, 91, 88, 86, 89, 90],  # Burj Khalifa
    [82, 84, 86, 83, 85, 87, 89, 84, 83, 85, 86],  # Shanghai Tower
    [78, 80, 82, 79, 81, 83, 85, 80, 79, 81, 82],  # Abraj Al Bait
    [87, 89, 91, 88, 90, 92, 94, 89, 87, 90, 91],  # Ping An Finance Centre
    [83, 85, 87, 84, 86, 88, 90, 85, 84, 86, 87]   # Lotte World Tower
]

# Calculate average stress scores per year across all skyscrapers
years = list(range(2010, 2021))
avg_scores_per_year = [np.mean([scores[i] for scores in stress_scores]) for i in range(len(years))]

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Box plot of stress scores
axes[0].boxplot(stress_scores, labels=skyscrapers, patch_artist=True, notch=True,
                boxprops=dict(facecolor='#cce5ff', color='#0000ff'),
                whiskerprops=dict(color='#0000ff'), capprops=dict(color='#0000ff'),
                medianprops=dict(color='orange'), flierprops=dict(marker='o', color='#00ff00', alpha=0.5))

axes[0].set_title("Structural Integrity Assessments\nof Iconic Skyscrapers (2010-2020)", fontsize=12, fontweight='bold')
axes[0].set_ylabel("Stress Test Score", fontsize=10)
axes[0].set_xlabel("Skyscrapers", fontsize=10)

# Annotate average scores
for i, scores in enumerate(stress_scores):
    avg_score = np.mean(scores)
    axes[0].annotate(f'Avg: {avg_score:.1f}', (i + 1, avg_score), textcoords="offset points", xytext=(0, 10),
                     ha='center', fontsize=9, color='red')

axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Line plot of average scores per year
axes[1].plot(years, avg_scores_per_year, marker='o', color='purple', linestyle='-', linewidth=2, markersize=5)
axes[1].set_title("Average Yearly Stress Test Scores\n(2010-2020)", fontsize=12, fontweight='bold')
axes[1].set_xlabel("Year", fontsize=10)
axes[1].set_ylabel("Average Stress Score", fontsize=10)

# Annotate points on the line plot
for (year, score) in zip(years, avg_scores_per_year):
    axes[1].annotate(f'{score:.1f}', (year, score), textcoords="offset points", xytext=(-5, 5),
                     ha='center', fontsize=9, color='blue')

axes[1].grid(axis='both', linestyle='--', alpha=0.7)

# Adjust layout to fit everything
plt.tight_layout()

# Show the plots
plt.show()