import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Years and cities
years = np.arange(2030, 2041)
cities = ['Solar City', 'Windville', 'Biomass Town']

# Energy data (GWh) for Solar, Wind, Biomass
energy_data = np.array([
    [100, 200, 50],    # 2030
    [120, 220, 55],    # 2031
    [140, 240, 60],    # 2032
    [160, 260, 65],    # 2033
    [180, 280, 70],    # 2034
    [200, 300, 75],    # 2035
    [220, 320, 80],    # 2036
    [240, 340, 85],    # 2037
    [260, 360, 90],    # 2038
    [280, 380, 95],    # 2039
    [300, 400, 100]    # 2040
])

# Colors for different energy types
colors = ['#FF7F0E', '#1F77B4', '#2CA02C']  # Solar, Wind, Biomass

# Create a new figure and set the 3D projection
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Loop through cities and plot data
for i, city in enumerate(cities):
    xs = np.repeat(years, energy_data.shape[1])  # Repeat each year for each energy type
    ys = np.full(xs.shape, i * 3)  # Unique position for each city on the y-axis
    zs = np.zeros(years.shape)  # Initialize base at zero for each year

    # Cumulative stacking of bars
    for j, (color, label) in enumerate(zip(colors, ['Solar', 'Wind', 'Biomass'])):
        height = energy_data[:, j]  # Current energy type's data for all years
        ax.bar3d(xs[j::3], ys[j::3], zs, dx=0.8, dy=0.8, dz=height, color=color, alpha=0.8, label=label if i == 0 else "")
        zs += height  # Update the base height for the next stack

# Set labels and titles
ax.set_xlabel('Year')
ax.set_ylabel('City')
ax.set_zlabel('Energy Output (GWh)')
ax.set_yticks([i * 3 for i in range(len(cities))])
ax.set_yticklabels(cities)

# Enhance view for clarity
ax.view_init(elev=30, azim=120)  # Adjust angle for better visibility

# Adjust layout for better fit
plt.tight_layout()

# Unique legend for the plot
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:3], labels[:3], loc='upper left')

# Title
plt.title('Evolution of Renewable Energy Sources\nin Future Cities (2030-2040)')

plt.show()