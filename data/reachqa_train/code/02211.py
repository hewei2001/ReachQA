import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define continents and renewable energy types
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_types = ['Solar', 'Wind', 'Hydro', 'Bioenergy']

# Projections of renewable energy percentages for each continent in 2050
energy_percentages = np.array([
    [30, 25, 35, 10],  # Africa
    [40, 20, 25, 15],  # Asia
    [25, 40, 20, 15],  # Europe
    [35, 30, 25, 10],  # North America
    [20, 35, 30, 15],  # South America
    [50, 20, 20, 10]   # Oceania
])

# Create a figure for the 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Assigning positions for each bar
x_positions = np.arange(len(continents))
y_positions = np.arange(len(energy_types))
xpos, ypos = np.meshgrid(x_positions, y_positions)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Flatten energy percentages to match bar positions
dz = energy_percentages.flatten()

# Define bar width and depth
dx = dy = 0.8

# Define colors for each type of renewable energy
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']  # Gold, Dodger Blue, Lime Green, Tomato

# Plot each bar with corresponding energy type color
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=np.repeat(colors, len(continents)))

# Set axis labels and title
ax.set_xlabel('Continents')
ax.set_ylabel('Energy Types')
ax.set_zlabel('Percentage')
ax.set_title('Mapping the Future:\nRenewable Energy Adoption Across the Continents (2050 Projections)', 
             fontsize=14, fontweight='bold', pad=20)

# Set tick labels for each axis
ax.set_xticks(x_positions)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(y_positions)
ax.set_yticklabels(energy_types)

# Add a legend for the colors
legend_labels = ['Solar', 'Wind', 'Hydro', 'Bioenergy']
color_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(color_patches, legend_labels, loc='upper left', bbox_to_anchor=(1.05, 1), title="Energy Types")

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()