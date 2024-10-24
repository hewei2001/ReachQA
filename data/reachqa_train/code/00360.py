import matplotlib.pyplot as plt
import numpy as np

# Define the categories and decades
categories = ['Dresses', 'Suits', 'Accessories', 'Footwear']
decades = ['1920s', '1950s', '1970s', '1990s']

# Popularity index values for each category across the decades
data = [
    [65, 58, 75, 68, 72, 70, 74],  # Dresses
    [60, 62, 68, 55, 71, 65, 69],  # Suits
    [90, 85, 87, 95, 88, 89, 92],  # Accessories
    [55, 60, 64, 59, 63, 61, 67],  # Footwear
]

# Mean popularity index over the decades for a line plot
mean_data = [np.mean(d) for d in data]

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 8))
boxprops = dict(facecolor='#ADD8E6', color='navy')
whiskerprops = dict(color='navy', linestyle='--')
capprops = dict(color='navy')
flierprops = dict(markerfacecolor='darkred', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='darkgreen', linewidth=2)

boxes = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                   boxprops=boxprops, whiskerprops=whiskerprops,
                   capprops=capprops, flierprops=flierprops,
                   medianprops=medianprops)

colors = ['#FFC1C1', '#ADD8E6', '#C6EFCE', '#FFECB3']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Plot the mean data line plot
for i, (category, mean) in enumerate(zip(categories, mean_data)):
    ax.plot(mean, i + 1, 'o-', label=f'{category} Mean', color='darkred')

# Customize the y-axis to reflect categories
ax.set_yticks(range(1, len(categories) + 1))
ax.set_yticklabels(categories)

# Grid and labels
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.title("Vintage Fashion Resurgence\nPopularity Index of Clothing Categories by Decade", fontsize=16, fontweight='bold')
plt.xlabel("Popularity Index", fontsize=12)
plt.ylabel("Vintage Clothing Categories", fontsize=12)

# Legend for the mean line plot
handles, labels = ax.get_legend_handles_labels()
box_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
combined_legend = handles + box_legend
combined_labels = labels + [f'{category} Spread' for category in categories]
ax.legend(combined_legend, combined_labels, loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()