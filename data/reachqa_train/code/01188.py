import matplotlib.pyplot as plt
import numpy as np

# Define crops and seasons
crops = ['Wheat', 'Corn', 'Rice']
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Artificial yield data (metric tons per hectare) for each crop across seasons
yield_data = {
    'Wheat': [4.2, 5.1, 3.5, 2.3],
    'Corn': [5.8, 6.5, 4.9, 3.0],
    'Rice': [6.2, 5.9, 5.6, 4.5]
}

# Prepare data for the box plot
data = [[yield_data[crop][season] for crop in crops] for season in range(4)]

# Mean values for annotations
mean_values = [np.mean(season_data) for season_data in data]

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 7))

# Customize colors and patterns for each box
colors = ['#ff9999', '#66b3ff', '#99ff99']
hatches = ['/', '\\', '|']

# Plot the box plot with notches and color patterns
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, labels=seasons, widths=0.6)

# Setting colors, patterns, and transparency for each crop's box
for patch, color, hatch in zip(bp['boxes'], colors, hatches):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
    patch.set_hatch(hatch)

# Customizing other box plot elements
plt.setp(bp['whiskers'], color='gray', linestyle='--')
plt.setp(bp['caps'], color='gray')
plt.setp(bp['medians'], color='orange', linewidth=2)
plt.setp(bp['fliers'], color='red', marker='o', alpha=0.5)

# Add mean points and annotations
for i, mean in enumerate(mean_values):
    ax.plot(i+1, mean, 'b*', markersize=10, label='Mean' if i == 0 else "")
    ax.annotate(f'{mean:.2f}', (i+1, mean), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='blue')

# Add lines connecting median values to show trend
median_positions = [np.median(season_data) for season_data in data]
ax.plot(range(1, len(seasons) + 1), median_positions, color='purple', linestyle='-', linewidth=1, marker='s', label='Median Trend')

# Add title and labels with layout adjustments
ax.set_title("Seasonal Productivity of Crops in Agriculture\nAcross Different Seasons", fontsize=14, fontweight='bold')
ax.set_xlabel("Season", fontsize=12)
ax.set_ylabel("Yield (Metric Tons per Hectare)", fontsize=12)

# Add enhanced legend
colors_legend = [plt.Line2D([0], [0], color=color, lw=4, label=crop, linestyle='-', marker='') for color, crop in zip(colors, crops)]
ax.legend(handles=colors_legend + [plt.Line2D([0], [0], color='purple', lw=1, label='Median Trend'), plt.Line2D([0], [0], color='b', marker='*', linestyle='', label='Mean')], title="Crops", loc='upper left', fontsize=10)

# Customize the grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adjust layout for better readability
plt.tight_layout()

# Show plot
plt.show()