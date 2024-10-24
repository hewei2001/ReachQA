import numpy as np
import matplotlib.pyplot as plt

# Define months and corresponding festival popularity scores
months = np.arange(1, 13)
popularity_scores = np.array([15, 22, 10, 5, 8, 12, 20, 25, 18, 10, 6, 30])

# Normalize popularity scores for plotting
max_radius = 10
radii = popularity_scores / popularity_scores.max() * max_radius

# Define the angles for each month (in radians)
angles = np.linspace(0, 2 * np.pi, len(months), endpoint=False)

# Colors for each sector
colors = plt.cm.viridis(np.linspace(0, 1, len(months)))

# Set up the plot
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

# Plot each sector as a bar
bars = ax.bar(angles, radii, width=2*np.pi/len(months), color=colors, alpha=0.7, edgecolor='black')

# Add labels for each month
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(angles)
ax.set_xticklabels(month_labels)

# Customize the plot
ax.set_title("Festival Popularity in Harmony Bay\nby Month", va='bottom', fontsize=16, fontweight='bold')
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
legend_labels = [f"{month}: {score}" for month, score in zip(month_labels, popularity_scores)]
ax.legend(bars, legend_labels, loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Monthly Popularity Scores")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()