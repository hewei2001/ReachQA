import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data definition
regions = ['North America', 'Europe', 'Asia']
years = [2020, 2021, 2022]
energy_sources = ['Solar', 'Wind', 'Hydropower']

# Energy generation data (in TWh)
solar_generation = np.array([[300, 340, 380],  # North America
                             [260, 290, 320],  # Europe
                             [450, 480, 510]])  # Asia

wind_generation = np.array([[400, 430, 460],
                            [370, 400, 420],
                            [500, 530, 560]])

hydro_generation = np.array([[500, 530, 550],
                             [450, 470, 480],
                             [600, 630, 650]])

# Stacking energy data
energy_data = np.array([solar_generation, wind_generation, hydro_generation])

# Initialize figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Bar width and depth
bar_width = 0.2
bar_depth = 0.5

# Initial position for stacking bars
x_pos = np.array([[year - bar_width/2 for year in years]]*len(regions))
y_pos = np.array([[j - bar_depth/2 for j in range(len(regions))]]*len(years)).T

# Colors for different energy sources
colors = ['#FFD700', '#32CD32', '#4682B4']  # Solar, Wind, Hydropower

# Plot each energy source for each region, stacking them appropriately
for i, source in enumerate(energy_sources):
    ax.bar3d(
        x_pos.flatten(), 
        y_pos.flatten(), 
        np.sum(energy_data[:i], axis=0).flatten(),  # Cumulative height for stacking
        bar_width, 
        bar_depth, 
        energy_data[i].flatten(), 
        color=colors[i], 
        alpha=0.8, 
        label=source
    )

# Set axis labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Region', fontsize=12)
ax.set_zlabel('Energy Generation (TWh)', fontsize=12)

# Set y-axis tick labels to regions
ax.set_yticks(range(len(regions)))
ax.set_yticklabels(regions)

# Title
ax.set_title(
    'Powering the Future:\nStacked 3D Analysis of Renewable Energy Generation by Region', 
    fontsize=16, 
    fontweight='bold', 
    pad=20
)

# Add legend
ax.legend(loc='upper left', fontsize=10, title='Energy Source', frameon=False)

# Set viewing angle
ax.view_init(elev=25, azim=135)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()