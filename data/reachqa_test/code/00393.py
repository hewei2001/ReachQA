import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the regions
regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa']

# Define the energy sources
energy_sources = ['Wind', 'Solar', 'Hydroelectric']

# Create sample data for each energy source by region
wind_production = np.array([20, 15, 30, 10, 5])  # in TWh
solar_production = np.array([10, 20, 15, 30, 25])  # in TWh
hydroelectric_production = np.array([50, 40, 30, 20, 15])  # in TWh

# Create a figure and 3D axes
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Define bar width and depth
width = 0.8
depth = 0.8

# Set x and z coordinates for the bars
x = np.arange(len(regions))
z = np.array([wind_production, solar_production, hydroelectric_production])

# Create the bars
for i, energy_source in enumerate(energy_sources):
    ax.bar3d(x, np.full(len(regions), i), np.zeros(len(regions)), width, depth, z[i], 
              color=plt.cm.RdYlGn(i/3), alpha=0.7, label=energy_source)

# Set the labels
ax.set_xlabel('Regions', labelpad=10)
ax.set_ylabel('Energy Sources', labelpad=10)
ax.set_zlabel('Production (TWh)', labelpad=10)

# Set the tick labels
ax.set_xticks(x)
ax.set_yticks(np.arange(len(energy_sources)))
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(energy_sources, fontsize=10)

# Set the title
ax.set_title("Global Renewable Energy Production\nby Region and Energy Source", fontsize=14)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1), fontsize=10)

# Adjust the viewing angle
ax.view_init(elev=25, azim=-60)

# Add grid and axis lines
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Show the plot
plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.show()