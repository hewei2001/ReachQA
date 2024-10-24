import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the forest habitats and the years for the x and y axes
habitats = ["Tropical Rainforest", "Temperate Forest", "Boreal Forest", "Mangroves", "Savanna"]
years = np.arange(2030, 2040)

# Create percentage data for different animal groups in each habitat across the years
mammals = np.array([
    [30, 28, 27, 26, 25, 24, 24, 23, 22, 21],
    [35, 34, 33, 32, 32, 31, 30, 29, 29, 28],
    [20, 20, 21, 21, 22, 22, 23, 24, 24, 25],
    [25, 25, 24, 24, 23, 23, 22, 22, 21, 20],
    [15, 16, 17, 18, 19, 20, 21, 21, 22, 23]
])

birds = np.array([
    [25, 26, 27, 28, 28, 29, 30, 30, 31, 32],
    [20, 20, 21, 21, 22, 23, 24, 25, 26, 27],
    [35, 34, 33, 32, 32, 31, 30, 29, 29, 28],
    [30, 31, 31, 31, 32, 32, 33, 34, 34, 35],
    [30, 29, 28, 28, 27, 27, 26, 25, 25, 24]
])

reptiles = np.array([
    [10, 11, 12, 13, 13, 14, 15, 15, 16, 17],
    [10, 10, 11, 11, 12, 13, 13, 14, 14, 15],
    [5, 6, 7, 8, 9, 10, 10, 11, 12, 13],
    [15, 14, 14, 13, 13, 12, 12, 11, 10, 10],
    [5, 5, 5, 6, 6, 7, 7, 8, 8, 9]
])

amphibians = np.array([
    [20, 19, 19, 18, 17, 17, 16, 16, 15, 14],
    [15, 14, 14, 13, 13, 12, 11, 11, 10, 10],
    [10, 11, 11, 12, 13, 13, 14, 15, 15, 16],
    [10, 10, 11, 12, 12, 13, 14, 14, 15, 16],
    [30, 31, 31, 32, 32, 33, 33, 34, 34, 35]
])

insects = np.array([
    [15, 16, 15, 15, 17, 16, 15, 16, 16, 16],
    [20, 22, 21, 23, 21, 21, 22, 21, 21, 20],
    [30, 29, 28, 27, 24, 24, 23, 22, 20, 18],
    [20, 19, 19, 20, 20, 20, 19, 19, 20, 19],
    [20, 19, 19, 18, 16, 16, 13, 12, 11, 9]
])

# Set up the plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Axis configuration
x_ticks = np.arange(len(habitats))
ax.set_xticks(x_ticks)
ax.set_xticklabels(habitats, rotation=45, ha='right', fontsize=10)

y_ticks = np.arange(len(years))
ax.set_yticks(y_ticks)
ax.set_yticklabels(years, fontsize=10)

ax.set_zlim(0, 100)
ax.set_zlabel('Biodiversity (%)', fontsize=12)

# Define colors for each species
cmap = cm.get_cmap('Set3')
colors = [cmap(i) for i in range(len(habitats))]
bar_width = 0.4

# Plot each species data as a stacked bar
species_data = [mammals, birds, reptiles, amphibians, insects]
species_names = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects']

for j, habitat in enumerate(habitats):
    bottom = np.zeros_like(years)
    for i, species in enumerate(species_data):
        x_pos = np.ones_like(years) * x_ticks[j]
        y_pos = years - years[0]
        z_pos = bottom
        dz = species[j]
        
        ax.bar3d(x_pos, y_pos, z_pos, bar_width, 1, dz, color=colors[i], alpha=0.8, label=species_names[i] if j == 0 else "")
        bottom += dz

# Annotate one or two significant data points
ax.text(x_ticks[0], years[5] - years[0], bottom[5], 'Peak\nReptiles', color='black', fontsize=9)

# Title and legend
plt.title("Decadal Trends in Biodiversity Across Forest Habitats\n(2030-2039)", fontsize=14, pad=30, loc='left')
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Animal Groups', fontsize=10)

# Adjust view angle
ax.view_init(elev=20., azim=-35)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()