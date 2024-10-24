import matplotlib.pyplot as plt
import numpy as np

# Original data for the boxplot
depth_ranges = ['0-50m', '50-200m', '200-1000m', '1000-4000m', '4000-6000m']
diversity_scores = [
    [7, 8, 9, 9, 8, 7, 6, 9, 9, 8],  # Coral Reef
    [5, 6, 7, 6, 5, 5, 6, 5, 6, 7],  # Continental Shelf
    [4, 5, 4, 4, 4, 5, 3, 4, 5, 4],  # Twilight Zone
    [2, 3, 2, 3, 2, 2, 3, 2, 3, 2],  # Midnight Zone
    [1, 1, 1, 1, 2, 1, 1, 2, 1, 1]   # Abyssal Plains
]

# Colors for the ecosystems
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#9467bd', '#d62728']

# Calculate the average diversity scores for the bar plot
average_diversity = [np.mean(scores) for scores in diversity_scores]

# Create subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
fig.suptitle("Exploration of Marine Biodiversity Across Ocean Depths", fontsize=16, fontweight='bold', y=1.05)

# First subplot: Boxplot
bplot = axs[0].boxplot(diversity_scores, vert=False, patch_artist=True, labels=depth_ranges, notch=True)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_title("Diversity Score Distribution", fontsize=12)
axs[0].set_xlabel("Diversity Score")
axs[0].set_ylabel("Depth Range (meters)")
axs[0].grid(True, linestyle='--', alpha=0.6, axis='x')

# Legend for boxplot
colors_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
labels_legend = ["Coral Reef", "Continental Shelf", "Twilight Zone", "Midnight Zone", "Abyssal Plains"]
axs[0].legend(colors_legend, labels_legend, title="Ecosystems", loc='upper right', fontsize=10)

# Second subplot: Bar chart for average diversity
axs[1].barh(depth_ranges, average_diversity, color=colors, alpha=0.8, edgecolor='black')
axs[1].set_title("Average Diversity Score Per Depth Range", fontsize=12)
axs[1].set_xlabel("Average Diversity Score")
axs[1].set_ylabel("Depth Range (meters)")

# Annotate the bar chart with average values
for i, v in enumerate(average_diversity):
    axs[1].text(v + 0.1, i, f"{v:.2f}", color='black', va='center', fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# Display the plot
plt.show()