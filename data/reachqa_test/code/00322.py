import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# City names
cities = ["Eco City", "Green Metropolis", "Skyville", "Solarburg", "Wind Heights", 
          "Sunset Town", "Rainyville", "Foggy Hill", "Harmony Flats", "Coastal Bay"]

# Air Quality Index (x-axis)
aqi = np.array([120, 80, 150, 60, 200, 110, 95, 130, 140, 75])

# Population in thousands (y-axis)
population = np.array([500, 850, 600, 400, 700, 560, 710, 430, 600, 800])

# Altitude in meters (z-axis)
altitude = np.array([250, 180, 300, 100, 400, 220, 170, 280, 290, 190])

# Urban area in square kilometers (Bubble size)
urban_area = np.array([120, 150, 100, 90, 140, 110, 130, 85, 95, 160])

# Green Space Percentage (additional variable for complexity)
green_space = np.array([40, 35, 50, 20, 15, 45, 50, 30, 25, 55])

# 3D Bubble Chart
fig = plt.figure(figsize=(18, 12))
ax = fig.add_subplot(111, projection='3d')

# Plot data points
scatter = ax.scatter(
    aqi,
    population,
    altitude,
    s=urban_area * 8,  # Scale bubble sizes
    c=green_space,     # Use green space percentage for color
    cmap='YlGnBu',
    alpha=0.9,
    edgecolors='k'
)

# Set axis labels
ax.set_xlabel('Air Quality Index (AQI)', fontsize=12, labelpad=15)
ax.set_ylabel('Population (thousands)', fontsize=12, labelpad=15)
ax.set_zlabel('Altitude (m)', fontsize=12, labelpad=15)

# Set title with line breaks for clarity
ax.set_title(
    'Comprehensive Urban Analysis: Air Quality, Population,\nAltitude, Urban Area, and Green Space',
    fontsize=16, fontweight='bold', pad=20
)

# Annotate cities to avoid occlusion
for i, city in enumerate(cities):
    ax.text(aqi[i], population[i], altitude[i], city, fontsize=9, ha='right', va='bottom')

# Add color bar for green space percentage
color_bar = fig.colorbar(scatter, ax=ax, shrink=0.6, aspect=10)
color_bar.set_label('Green Space Percentage', fontsize=12)

# Set viewing angle for best perspective
ax.view_init(elev=25, azim=140)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()