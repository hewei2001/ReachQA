import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Expanded Efficiency Data for Different Solar Panel Types
monocrystalline_efficiency = [18, 19, 20, 21, 18, 20, 19, 20, 21, 22, 19, 20, 18, 21, 23, 24, 22, 20, 21, 23]
polycrystalline_efficiency = [15, 16, 15, 17, 15, 16, 16, 15, 17, 18, 16, 15, 16, 16, 14, 17, 15, 15, 14, 16]
thin_film_efficiency = [10, 11, 9, 12, 11, 10, 10, 9, 13, 12, 11, 10, 11, 9, 8, 9, 10, 11, 9, 12]
bifacial_efficiency = [17, 18, 18, 19, 17, 18, 19, 17, 20, 19, 18, 17, 19, 18, 19, 20, 18, 19, 20, 21]
half_cut_monocrystalline_efficiency = [19, 20, 21, 22, 20, 21, 22, 23, 24, 23, 21, 22, 20, 23, 22, 23, 24, 25, 24, 21]

# Compile data for the boxplot
data = [
    monocrystalline_efficiency,
    polycrystalline_efficiency,
    thin_film_efficiency,
    bifacial_efficiency,
    half_cut_monocrystalline_efficiency
]

# Define the solar panel types
panel_types = ['Monocrystalline', 'Polycrystalline', 'Thin-Film', 'Bifacial', 'Half-Cut Mono']

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(14, 10))

# Create the box plot
box = ax.boxplot(data, vert=True, patch_artist=True, labels=panel_types, notch=True)

# Customize the box plot
colors = ['#FFD700', '#87CEEB', '#90EE90', '#FF69B4', '#FFA500']
for patch, color in zip(box['boxes'], colors):
    patch.set(facecolor=color, alpha=0.7)

# Set properties of other plot elements
plt.setp(box['whiskers'], color='gray', linestyle='--')
plt.setp(box['caps'], color='black')
plt.setp(box['medians'], color='red', linewidth=2)

# Set titles and labels
ax.set_title('Solar Panel Efficiency Variability\nAcross Different Technologies\nand Advanced Types', fontsize=16, fontweight='bold')
ax.set_ylabel('Efficiency (%)', fontsize=12)
ax.set_xlabel('Solar Panel Type', fontsize=12)

# Add grid to the plot
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Overlay additional statistical measures: means
means = [np.mean(d) for d in data]
ax.plot(np.arange(1, len(means) + 1), means, 'o', color='blue', markersize=8, label='Mean')

# Legend handling
color_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, panel_types)]
ax.legend(handles=color_patches + [plt.Line2D([0], [0], marker='o', color='w', label='Mean', markerfacecolor='blue', markersize=8)],
          title='Panel Type', loc='upper left', fontsize=10, frameon=False)

# Adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the plot
plt.show()