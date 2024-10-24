import matplotlib.pyplot as plt
import numpy as np

# Define data
cities = ['New York', 'Shanghai', 'Dubai', 'London']
years = [1990, 2000, 2010, 2020]
height_data = np.array([
    [381, 420, 541, 546],  # New York
    [420, 468, 492, 632],  # Shanghai
    [355, 360, 828, 828],  # Dubai
    [180, 235, 310, 310]   # London
])

# Create a figure and a 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Number of bars along the x and y axes
xpos, ypos = np.meshgrid(np.arange(len(years)), np.arange(len(cities)))

# Flatten the arrays
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Heights of the bars
dz = height_data.flatten()

# Bar dimensions
dx = dy = 0.4

# Colors for each city, repeating them for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red
colors_flat = np.array(colors)[ypos]

# Plot the bars
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors_flat, alpha=0.8, zsort='average')

# Set the axis labels
ax.set_xlabel('Year')
ax.set_ylabel('City')
ax.set_zlabel('Height (m)')
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(len(cities)))
ax.set_yticklabels(cities)

# Title for the plot
plt.title("Evolution of Skyscraper Heights\nAcross Major Cities (1990-2020)", pad=40)

# Set viewing angle for optimal visualization
ax.view_init(elev=20, azim=120)

# Add grid for better depth perception
ax.grid(True)

# Automatic layout adjustment
plt.tight_layout()

# Show the plot
plt.show()