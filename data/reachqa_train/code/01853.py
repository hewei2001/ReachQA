import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data setup for five plants
plants = ['Tomato', 'Lettuce', 'Bell Pepper', 'Cucumber', 'Basil']
average_height = np.array([90, 30, 70, 150, 40])  # cm
light_exposure = np.array([8, 6, 7, 9, 5])  # hours per day
water_usage = np.array([20, 10, 15, 25, 5])  # liters per week

# Bubble sizes represent plant height
bubble_sizes = average_height * 10

# Assigning colors for different plants
colors = ['red', 'lightgreen', 'orange', 'green', 'purple']

# Create the 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
scatter = ax.scatter(light_exposure, water_usage, average_height, s=bubble_sizes, c=colors, alpha=0.6, edgecolors="w")

# Add title and labels
ax.set_title('Urban Gardening: Impact of Light and Water on Plant Growth\nCommunity Garden Insights', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Light Exposure (hours/day)', fontsize=12)
ax.set_ylabel('Water Usage (liters/week)', fontsize=12)
ax.set_zlabel('Average Plant Height (cm)', fontsize=12)

# Annotating each plant type on the plot
for i, plant in enumerate(plants):
    ax.text(light_exposure[i], water_usage[i], average_height[i] + 5, plant, fontsize=9, ha='center')

# Create a legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=plant, markersize=np.sqrt(bubble_sizes[i])/2, markerfacecolor=color, alpha=0.6) 
                   for i, (plant, color) in enumerate(zip(plants, colors))]
ax.legend(handles=legend_elements, loc='upper left', title="Plants")

# Adjust the view angle for better visibility
ax.view_init(elev=20, azim=135)

# Automatically adjust the image layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()