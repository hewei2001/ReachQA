import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define years and continents
years = np.arange(2010, 2021)
continents = ['Asia', 'Europe', 'North America']

# Define the percentage of renewable energy consumption over the years
renewable_percentage = np.array([
    [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 34],  # Asia
    [20, 23, 26, 28, 30, 33, 35, 37, 40, 42, 45],  # Europe
    [15, 17, 20, 22, 25, 28, 30, 32, 35, 37, 39]   # North America
])

# Set up the figure and 3D axis
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Define bar width and depth
bar_width = 0.2
bar_depth = 0.5

# Set positions for the bars
x_positions = np.arange(len(years))
y_positions = np.arange(len(continents))

# Colors for each continent
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot each continent's data
for i, continent in enumerate(continents):
    xpos = x_positions - bar_width + i * bar_width
    ypos = np.full_like(xpos, i)  # y-position remains same for a continent
    ax.bar3d(xpos, ypos, np.zeros_like(xpos), bar_width, bar_depth, renewable_percentage[i], color=colors[i], alpha=0.8, label=continent)

# Customize the axes
ax.set_title('Renewable Energy Adoption Rates\nAcross Continents (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Continent', fontsize=12)
ax.set_zlabel('Renewable Energy (%)', fontsize=12)

# Setting tick positions and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(y_positions)
ax.set_yticklabels(continents)
ax.set_zlim(0, 50)

# Add legend
ax.legend(loc='upper left', fontsize=10, title='Continents', title_fontsize='12')

# Enhance visual clarity and presentation
plt.tight_layout()
ax.view_init(elev=30, azim=125)

# Show the plot
plt.show()