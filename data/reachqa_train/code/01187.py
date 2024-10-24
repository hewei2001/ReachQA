import matplotlib.pyplot as plt

# Define crops and seasons
crops = ['Wheat', 'Corn', 'Rice']
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Updated artificial yield data (metric tons per hectare) for each crop across seasons
# Data: [Spring, Summer, Autumn, Winter] for each crop
yield_data = {
    'Wheat': [4.2, 5.1, 3.5, 2.3],
    'Corn': [5.8, 6.5, 4.9, 3.0],
    'Rice': [6.2, 5.9, 5.6, 4.5]
}

# Prepare data for the box plot
data = [[yield_data[crop][season] for crop in crops] for season in range(4)]

# Create the box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Customize colors for each box
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Plot the box plot with notches and color patches
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, labels=seasons, widths=0.6)

# Setting colors for each crop's box and adding transparency
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize other elements of the box plot
plt.setp(bp['whiskers'], color='gray', linestyle='--')
plt.setp(bp['caps'], color='gray')
plt.setp(bp['medians'], color='orange', linewidth=2)
plt.setp(bp['fliers'], color='red', marker='o', alpha=0.5)

# Add title and labels
ax.set_title("Seasonal Productivity of Crops in Agriculture\nAcross Different Seasons", fontsize=14, fontweight='bold')
ax.set_xlabel("Season", fontsize=12)
ax.set_ylabel("Yield (Metric Tons per Hectare)", fontsize=12)

# Add legend
colors_legend = [plt.Line2D([0], [0], color=color, lw=4, label=crop) for color, crop in zip(colors, crops)]
ax.legend(handles=colors_legend, title="Crops", loc='upper left')

# Customize the grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adjust layout for better readability
plt.tight_layout()

# Show plot
plt.show()