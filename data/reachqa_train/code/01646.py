import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the data
countries = ['USA', 'China', 'India']
years = np.arange(2030, 2041)

# Number of projects per year for each country
usa_projects = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
china_projects = np.array([8, 10, 13, 15, 17, 20, 22, 25, 27, 30, 32])
india_projects = np.array([5, 7, 9, 12, 14, 16, 18, 20, 22, 24, 26])

# Create a new figure for a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create position arrays for each bar
xpos = np.arange(len(years))
ypos_usa = np.zeros_like(xpos)
ypos_china = np.ones_like(xpos) * 1
ypos_india = np.ones_like(xpos) * 2

# Define the base position for the bars
zpos = np.zeros_like(xpos)

# Define the bar width and depth
dx = np.ones_like(xpos) * 0.8
dy = np.ones_like(xpos) * 0.8

# Plot the bars for each country
ax.bar3d(xpos, ypos_usa, zpos, dx, dy, usa_projects, color='r', alpha=0.8, label='USA')
ax.bar3d(xpos, ypos_china, zpos, dx, dy, china_projects, color='g', alpha=0.8, label='China')
ax.bar3d(xpos, ypos_india, zpos, dx, dy, india_projects, color='b', alpha=0.8, label='India')

# Set axis labels
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Country', fontsize=12, labelpad=10)
ax.set_zlabel('Number of Projects', fontsize=12, labelpad=10)

# Set x ticks with year labels
ax.set_xticks(xpos)
ax.set_xticklabels(years)

# Set y ticks with country labels
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(countries)

# Set the viewing angle for better visibility
ax.view_init(elev=20, azim=40)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.5)

# Add a title
ax.set_title('Mars Colonization Research Initiatives\nA Decade of Exploration (2030-2040)', fontsize=16, pad=20)

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()