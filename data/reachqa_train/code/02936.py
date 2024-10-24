import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define the categories for evaluation
categories = ['Atmosphere Quality', 'Surface Temp', 'Water Presence', 'Orbital Stability', 'Overall Score']

# Habitability scores for each exoplanet across different criteria
scores = {
    'Planet Xylon': [7.5, 8.0, 6.5, 7.0, 7.25],
    'Planet Taron': [8.0, 6.0, 5.5, 6.5, 6.5],
    'Planet Zenthra': [5.5, 9.0, 7.5, 6.0, 7.0],
    'Planet Qalaxar': [6.0, 7.5, 8.0, 8.5, 7.5],
    'Planet Uthoria': [7.0, 8.5, 9.0, 7.5, 8.0]
}

# Convert data for easy plotting
data = np.array(list(scores.values()))
planet_names = list(scores.keys())

# Create figure and axis objects
fig, axes = plt.subplots(2, 1, figsize=(14, 12), gridspec_kw={'height_ratios': [2, 1]})
plt.subplots_adjust(hspace=0.4)

# Plot 1: Combined Boxplot and Violin Plot
ax1 = axes[0]

# Seaborn violin plot
sns.violinplot(data=data, inner=None, ax=ax1, palette="pastel", linewidth=1.5)

# Add boxplot on top of violin plot
sns.boxplot(data=data, ax=ax1, showcaps=False, boxprops=dict(facecolor='None'), whiskerprops=dict(linewidth=2), palette='muted')

# Overlay jittered scatter
for i, planet_data in enumerate(data):
    ax1.scatter(np.full(planet_data.shape, i), planet_data, alpha=0.6, color='darkblue', edgecolor='w', s=60, linewidth=1)

ax1.set_xticklabels(planet_names)
ax1.set_title("Astrobiologist Survey: Habitability Scores of Exoplanets\n(Combined Box and Violin Plot)", fontsize=16, fontweight='bold', loc='center')
ax1.set_ylabel('Habitability Score (1-10)')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate an observation
ax1.annotate('High Water Presence', xy=(4, scores['Planet Uthoria'][2]), xytext=(3.8, scores['Planet Uthoria'][2] + 0.5),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='darkblue')

# Plot 2: Scores by Criteria
ax2 = axes[1]

# Transpose data for criteria-wise plotting
criteria_data = data.T

# Plot a bar graph for each criterion
for idx, criterion_scores in enumerate(criteria_data):
    ax2.bar(np.arange(len(planet_names)) + idx/10, criterion_scores, width=0.1, label=categories[idx])

ax2.set_title("Scores by Evaluation Criterion", fontsize=14, fontweight='bold')
ax2.set_xticks(np.arange(len(planet_names)))
ax2.set_xticklabels(planet_names)
ax2.set_ylabel('Habitability Score (1-10)')
ax2.set_xlabel('Exoplanets')
ax2.legend(title='Criteria', loc='upper right', bbox_to_anchor=(1.15, 1))
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Show the chart
plt.show()