import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define years and districts
years = np.arange(2012, 2023)
districts = ['Downtown', 'Uptown', 'Riverside']

# Skyscraper data: Residential, Commercial, Mixed-use for each district
downtown = np.array([[5, 3, 2], [7, 5, 3], [8, 6, 4], [10, 7, 5], [12, 8, 6], [15, 10, 8], 
                     [18, 12, 10], [20, 15, 12], [23, 18, 14], [26, 20, 16], [30, 22, 18]])
uptown = np.array([[2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 8, 7], [7, 9, 8], 
                   [9, 11, 10], [11, 13, 12], [13, 15, 14], [15, 17, 16], [17, 19, 18]])
riverside = np.array([[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], 
                      [7, 9, 8], [9, 11, 10], [11, 13, 12], [13, 15, 14], [15, 17, 16]])

# Create figure and 3D axes
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Bar attributes
bar_width = 0.6
colors = ['#8B4513', '#1E90FF', '#32CD32']  # Colors for Residential, Commercial, Mixed-use

# Generate 3D bar chart
for i, district in enumerate(districts):
    xpos = np.arange(len(years))
    ypos = np.full_like(xpos, i) * 2  # Separate districts vertically

    # Select data for each district
    if district == 'Downtown':
        skyscrapers = downtown
    elif district == 'Uptown':
        skyscrapers = uptown
    elif district == 'Riverside':
        skyscrapers = riverside

    # Stacking skyscraper data
    bottom_heights = np.zeros_like(xpos)
    for j, (label, color) in enumerate(zip(['Residential', 'Commercial', 'Mixed-use'], colors)):
        ax.bar3d(xpos, ypos, bottom_heights, bar_width, bar_width, skyscrapers[:, j], color=color, alpha=0.8, label=label if i == 0 else "")
        bottom_heights += skyscrapers[:, j]

# Adjusting visual aspects
ax.set_xlabel('Year')
ax.set_ylabel('District')
ax.set_zlabel('Number of Skyscrapers')
ax.set_title('Skyline Metropolis: A Decade of Skyscraper Development', fontsize=14, fontweight='bold', pad=30)

# Set district ticks
ax.set_yticks([0, 2, 4])
ax.set_yticklabels(districts)

# Viewing angle for better visibility
ax.view_init(elev=25, azim=135)

# Avoid label overlapping and add legend
plt.tight_layout()
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Building Type')

# Display the chart
plt.show()