import matplotlib.pyplot as plt

# Data: Happiness Index Scores for Different Continents (2010-2020)
happiness_scores_africa = [4.3, 4.5, 4.7, 4.6, 4.8, 4.4, 4.9, 4.6, 4.7, 4.5, 4.6]
happiness_scores_asia = [5.1, 5.2, 5.0, 5.4, 5.3, 5.2, 5.1, 5.3, 5.4, 5.0, 5.5]
happiness_scores_europe = [6.7, 6.8, 6.9, 6.8, 6.7, 6.9, 7.0, 6.8, 6.9, 6.7, 7.1]
happiness_scores_north_america = [6.1, 6.3, 6.2, 6.5, 6.4, 6.5, 6.2, 6.6, 6.7, 6.8, 6.4]
happiness_scores_south_america = [5.8, 5.7, 5.9, 5.8, 5.9, 6.0, 5.6, 6.1, 5.9, 5.8, 6.0]

# Combine data
data = [
    happiness_scores_africa,
    happiness_scores_asia,
    happiness_scores_europe,
    happiness_scores_north_america,
    happiness_scores_south_america
]

# Labels for the continents
labels = ['Africa', 'Asia', 'Europe', 'North America', 'South America']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Boxplot with enhanced visuals
boxplot = ax.boxplot(
    data, 
    patch_artist=True, 
    notch=True, 
    vert=True, 
    boxprops=dict(facecolor='lightblue', color='blue'),
    whiskerprops=dict(color='gray', linestyle='--'),
    capprops=dict(color='black', linewidth=1.5),
    medianprops=dict(color='darkorange', linewidth=2),
    flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5)
)

# Title and labels
ax.set_title("Global Happiness Index:\nA Decade of Joy Across Continents", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Continent", fontsize=12)
ax.set_ylabel("Happiness Index Score", fontsize=12)
ax.set_xticklabels(labels, fontsize=11, rotation=15)

# Grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Tight layout for clarity
plt.tight_layout()

# Show the plot
plt.show()