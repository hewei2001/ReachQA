import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from itertools import cycle

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Area data in acres for each type of urban farming over the years
rooftop_gardens = np.array([10, 15, 20, 25, 35, 45, 55, 65, 80, 95, 110])
vertical_farms = np.array([5, 8, 12, 18, 25, 35, 45, 60, 75, 90, 105])
community_plots = np.array([15, 20, 28, 40, 52, 67, 83, 100, 120, 140, 160])
hydroponics = np.array([2, 5, 8, 14, 22, 30, 45, 60, 80, 100, 120])

# Colors for each farming type
colors = ['#76c7c0', '#f7cac9', '#92a8d1', '#ff6f61']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Cycle through different color maps for gradients
color_maps = cycle([cm.Blues, cm.Reds, cm.Greens, cm.Oranges])

# Stack data for each type of urban farming
cumulative_data = np.zeros_like(years)

# Create the area plot with gradient and markers
for idx, (data, color, cmap) in enumerate(zip(
        [rooftop_gardens, vertical_farms, community_plots, hydroponics],
        colors,
        color_maps)):
    rgba_color = cmap(np.linspace(0.5, 0.95, len(years)))  # Apply gradient
    ax.fill_between(years, cumulative_data, cumulative_data + data,
                    color=color, alpha=0.8)
    ax.plot(years, cumulative_data + data,
            label=f"{['Rooftop Gardens', 'Vertical Farms', 'Community Plots', 'Hydroponics'][idx]}",
            linewidth=2, marker='o', color=color)
    cumulative_data += data

# Title and labels
ax.set_title('Urban Agriculture:\nDecadal Growth of Urban Farming Spaces in Metropolis',
             fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Area Covered (Acres)', fontsize=12)

# Customize x-axis
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add legend
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Add grid with enhanced visibility
ax.grid(True, linestyle='--', alpha=0.5)

# Highlight significant trends with annotations
ax.annotate('Emergence of Vertical Farms', xy=(2017, 65), xytext=(2015, 140),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')

ax.annotate('Rapid Growth in Hydroponics', xy=(2021, 360), xytext=(2018, 400),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')

# Enhancing readability of overlapping text
plt.tight_layout()

# Display the plot
plt.show()