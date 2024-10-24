import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Enhanced data set with more cities and additional data dimensions
cities = ['San Francisco', 'Berlin', 'Bangalore', 'Tokyo', 'New York']
num_startups = np.array([2500, 1500, 2000, 1800, 3000])
funding_received = np.array([20000, 8000, 12000, 10000, 25000])
avg_employee_size = np.array([50, 40, 35, 45, 60])
rd_spending = np.array([500, 300, 400, 350, 600])
innovation_index = np.array([7.5, 6.5, 6.8, 7.0, 8.2])

# Bubble sizes proportional to a new composite index
bubble_size = num_startups / 5 + funding_received / 100 + rd_spending / 5

# Colors using a gradient based on the innovation index
colors = plt.cm.viridis(innovation_index / max(innovation_index))

# Set up the figure and 3D axis
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Create the 3D scatter plot
sc = ax.scatter(num_startups, funding_received, avg_employee_size,
                s=bubble_size, c=colors, alpha=0.8, edgecolors='k', linewidth=0.5)

# Add labels for each city with adjusted positions to avoid overlap
for i, city in enumerate(cities):
    ax.text(num_startups[i], funding_received[i], avg_employee_size[i] + 2, city,
            fontsize=10, ha='center', va='bottom', color='black', weight='bold')

# Set axis labels
ax.set_xlabel('Number of Startups', labelpad=10)
ax.set_ylabel('Funding Received ($M)', labelpad=10)
ax.set_zlabel('Avg Employee Size', labelpad=10)

# Set title with line breaks for better layout
ax.set_title('Tech Startups Performance in Major Cities\nAnalysis of Startups, Funding, R&D, and Innovation in 2023',
             pad=30, fontsize=14)

# Add a color bar for the innovation index
cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Innovation Index', rotation=270, labelpad=15)

# Adjust viewing angle for optimal view
ax.view_init(elev=30, azim=120)

# Improve layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()