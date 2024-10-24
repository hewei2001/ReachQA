import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Fictional Eco-Destinations
destinations = [
    "Sunny Shores", "Green Valley", "Blue Oasis",
    "Mountain Peak", "Desert Bloom", "Forest Haven",
    "River Bend", "Island Retreat", "City Park"
]

# 3D Data for plotting
popularity = np.array([90, 75, 65, 80, 60, 85, 70, 55, 95])
environmental_impact = np.array([30, 45, 55, 40, 65, 35, 50, 70, 25])
visitor_satisfaction = np.array([85, 80, 75, 90, 70, 95, 60, 50, 88])
accessibility = np.array([500, 600, 550, 450, 620, 480, 590, 530, 610])

# Create 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with varying bubble sizes and colors
bubble_chart = ax.scatter(popularity, environmental_impact, visitor_satisfaction,
                          s=accessibility, alpha=0.7, c=accessibility,
                          cmap='viridis', edgecolors='w')

# Annotate each bubble with the destination name
for i, destination in enumerate(destinations):
    ax.text(popularity[i], environmental_impact[i], visitor_satisfaction[i],
            destination, fontsize=9, ha='center', va='center')

# Set labels and title
ax.set_xlabel('Popularity (Score)', fontsize=10)
ax.set_ylabel('Environmental Impact (Score)', fontsize=10)
ax.set_zlabel('Visitor Satisfaction (Score)', fontsize=10)
ax.set_title('Eco Travel Destinations Analysis:\nPopularity vs Impact vs Satisfaction', fontsize=14, fontweight='bold')

# Add a color bar to explain the bubble color mapping to accessibility
cbar = plt.colorbar(bubble_chart, shrink=0.6, aspect=10)
cbar.set_label('Accessibility (Scale)', fontsize=10)

# Adjust view angle for better visualization
ax.view_init(elev=30, azim=120)

# Ensure layout is tight and well-arranged
plt.tight_layout()

# Display the plot
plt.show()