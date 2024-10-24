import matplotlib.pyplot as plt

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

# Prepare data for the box plot
box_plot_data = list(scores.values())

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Create the vertical boxplot
boxprops = dict(linestyle='-', linewidth=2, color='purple', facecolor='lavender')
medianprops = dict(linestyle='-', linewidth=2, color='darkviolet')
whiskerprops = dict(linestyle='--', linewidth=1.5, color='purple')
capprops = dict(linestyle='-', linewidth=2, color='purple')

# Plot the boxplot
ax.boxplot(box_plot_data, labels=scores.keys(), patch_artist=True,
           boxprops=boxprops, medianprops=medianprops,
           whiskerprops=whiskerprops, capprops=capprops,
           flierprops=dict(marker='o', color='magenta', markersize=5, alpha=0.5),
           notch=True)

# Add plot details
ax.set_title("Astrobiologist Survey:\nHabitability Scores of Exoplanets", fontsize=16, fontweight='bold', loc='center')
ax.set_ylabel('Habitability Score (1-10)', fontsize=12)
ax.set_xlabel('Exoplanets', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate an observation
ax.annotate('High Water Presence', xy=(5, scores['Planet Uthoria'][2]), xytext=(4.8, scores['Planet Uthoria'][2] + 0.5),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='darkblue')

# Automatically adjust the layout
plt.tight_layout()

# Show the chart
plt.show()