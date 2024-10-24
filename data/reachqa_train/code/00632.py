import matplotlib.pyplot as plt
import numpy as np

# Habitat module designs
designs = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']

# Data: interior area in square meters for each functional zone in each habitat design
life_support = np.array([30, 35, 33, 29, 40])
research = np.array([25, 20, 30, 28, 22])
living_quarters = np.array([40, 50, 45, 38, 55])
recreation = np.array([20, 25, 15, 18, 25])
storage = np.array([15, 10, 12, 14, 8])

# Combine the data into a single array for each design
data = np.array([life_support, research, living_quarters, recreation, storage]).T

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(data, vert=False, patch_artist=True, labels=designs, notch=True, whis=1.5)

# Customize box plot colors for clarity and distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

# Setting titles and labels
ax.set_title('Comparative Analysis of Habitat Module Designs\nfor Mars Colonization', fontsize=14, pad=15)
ax.set_xlabel('Interior Area Allocation (Square Meters)', fontsize=12)
ax.set_ylabel('Habitat Module Design', fontsize=12)

# Adding a grid for better visual reference
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Legend for the functional zones
legend_labels = ['Life Support', 'Research', 'Living Quarters', 'Recreation', 'Storage']
patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(patches, legend_labels, loc='upper right', fontsize=10, title='Functional Zones')

# Improve layout spacing
plt.tight_layout()

# Show the plot
plt.show()