import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data Preparation
years = np.arange(2018, 2023)

# Square footage data for each type of garden in each city
# GreenTown
vegetable_greentown = [2000, 2300, 2600, 2900, 3200]
flower_greentown = [1500, 1700, 1900, 2100, 2300]
herb_greentown = [1000, 1200, 1300, 1400, 1600]

# FlowerCity
vegetable_flowercity = [1800, 2000, 2200, 2500, 2700]
flower_flowercity = [1600, 1800, 2000, 2200, 2400]
herb_flowercity = [800, 1000, 1100, 1200, 1300]

# Herbopolis
vegetable_herbopolis = [1700, 1950, 2150, 2350, 2600]
flower_herbopolis = [1400, 1600, 1800, 2000, 2200]
herb_herbopolis = [900, 1100, 1250, 1350, 1500]

# Create a 3D figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar width
width = 0.25
colors = ['#8BC34A', '#FFC107', '#FF5722']  # Colors for Vegetable, Flower, and Herb

# GreenTown
x = years
y = np.zeros_like(x)
ax.bar3d(x, y, np.zeros_like(x), width, width, vegetable_greentown, color=colors[0], alpha=0.8, label='Vegetable Gardens')
ax.bar3d(x, y, vegetable_greentown, width, width, flower_greentown, color=colors[1], alpha=0.8, label='Flower Gardens')
ax.bar3d(x, y, np.array(vegetable_greentown) + np.array(flower_greentown), width, width, herb_greentown, color=colors[2], alpha=0.8, label='Herb Gardens')

# FlowerCity
y = np.ones_like(x)
ax.bar3d(x, y, np.zeros_like(x), width, width, vegetable_flowercity, color=colors[0], alpha=0.8)
ax.bar3d(x, y, vegetable_flowercity, width, width, flower_flowercity, color=colors[1], alpha=0.8)
ax.bar3d(x, y, np.array(vegetable_flowercity) + np.array(flower_flowercity), width, width, herb_flowercity, color=colors[2], alpha=0.8)

# Herbopolis
y = np.ones_like(x) * 2
ax.bar3d(x, y, np.zeros_like(x), width, width, vegetable_herbopolis, color=colors[0], alpha=0.8)
ax.bar3d(x, y, vegetable_herbopolis, width, width, flower_herbopolis, color=colors[1], alpha=0.8)
ax.bar3d(x, y, np.array(vegetable_herbopolis) + np.array(flower_herbopolis), width, width, herb_herbopolis, color=colors[2], alpha=0.8)

# Setting labels and titles
ax.set_xlabel('Year')
ax.set_ylabel('City')
ax.set_zlabel('Square Footage')
ax.set_yticks([0.5, 1.5, 2.5])
ax.set_yticklabels(['GreenTown', 'FlowerCity', 'Herbopolis'])
ax.set_title("Urban Garden Revolution: \nGrowth in Garden Spaces Across Major Cities (2018-2022)", fontsize=14, fontweight='bold')

# Set the viewing angle for optimal visibility
ax.view_init(elev=20., azim=120)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()