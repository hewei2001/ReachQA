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

# Derived data for additional plot
impact_vs_accessibility = environmental_impact * (accessibility / 100)

# Create figure and subplots
fig = plt.figure(figsize=(14, 8))

# 3D Bubble Plot
ax1 = fig.add_subplot(121, projection='3d')
bubble_chart = ax1.scatter(popularity, environmental_impact, visitor_satisfaction,
                           s=accessibility, alpha=0.7, c=accessibility,
                           cmap='viridis', edgecolors='w')

for i, destination in enumerate(destinations):
    ax1.text(popularity[i], environmental_impact[i], visitor_satisfaction[i],
             destination, fontsize=8, ha='center', va='center')

ax1.set_xlabel('Popularity (Score)', fontsize=10)
ax1.set_ylabel('Environmental Impact (Score)', fontsize=10)
ax1.set_zlabel('Visitor Satisfaction (Score)', fontsize=10)
ax1.set_title('Eco Destinations: Popularity vs Impact vs Satisfaction', fontsize=12, fontweight='bold')

cbar = plt.colorbar(bubble_chart, ax=ax1, shrink=0.6, aspect=10)
cbar.set_label('Accessibility (Scale)', fontsize=10)

ax1.view_init(elev=30, azim=120)

# 2D Heatmap Plot
ax2 = fig.add_subplot(122)
heatmap = ax2.imshow(impact_vs_accessibility.reshape((3, 3)), cmap='coolwarm', interpolation='nearest')

ax2.set_xticks(np.arange(3))
ax2.set_yticks(np.arange(3))
ax2.set_xticklabels(destinations[:3])
ax2.set_yticklabels(destinations[3:6])
ax2.set_xlabel('Destinations (Part 1)', fontsize=10)
ax2.set_ylabel('Destinations (Part 2)', fontsize=10)
ax2.set_title('Impact vs Accessibility Heatmap', fontsize=12, fontweight='bold')

cbar2 = plt.colorbar(heatmap, ax=ax2)
cbar2.set_label('Impact-Accessibility Score', fontsize=10)

# Ensure layout is tight and well-arranged
plt.tight_layout()

# Display the plot
plt.show()