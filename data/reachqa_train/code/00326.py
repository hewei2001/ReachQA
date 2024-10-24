import matplotlib.pyplot as plt
import numpy as np

# Define enhanced data with additional cities and years
cities = ['New York', 'Shanghai', 'Dubai', 'London', 'Tokyo', 'Sydney', 'Johannesburg', 'São Paulo']
years = list(range(1980, 2025, 5))
height_data = np.array([
    [320, 350, 381, 420, 450, 520, 541, 546, 570],  # New York
    [300, 350, 400, 420, 468, 500, 492, 632, 650],  # Shanghai
    [180, 200, 250, 360, 700, 828, 828, 828, 900],  # Dubai
    [160, 170, 180, 235, 310, 315, 310, 320, 330],  # London
    [450, 455, 460, 480, 490, 610, 634, 634, 700],  # Tokyo
    [250, 260, 270, 280, 290, 350, 380, 400, 420],  # Sydney
    [150, 180, 200, 220, 240, 270, 280, 300, 320],  # Johannesburg
    [180, 200, 210, 250, 260, 280, 300, 340, 360]   # São Paulo
])

# Create figure and a 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Determine number of bars along the x and y axes
xpos, ypos = np.meshgrid(np.arange(len(years)), np.arange(len(cities)))

# Flatten arrays
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Flatten the height data for bars
dz = height_data.flatten()

# Bar dimensions
dx = dy = 0.5

# Create color gradient based on heights
norm_dz = dz / dz.max()  # Normalize heights
colors = plt.cm.viridis(norm_dz)  # Use a colormap for gradients

# Plot the bars
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8, zsort='average')

# Set the axis labels
ax.set_xlabel('Year')
ax.set_ylabel('City')
ax.set_zlabel('Height (m)')
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(len(cities)))
ax.set_yticklabels(cities)

# Title for the plot
plt.title("Evolution of Skyscraper Heights\nAcross Major Cities Worldwide (1980-2025)", pad=40)

# Set viewing angle for optimal visualization
ax.view_init(elev=20, azim=120)

# Add grid for better depth perception
ax.grid(True)

# Automatic layout adjustment to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()