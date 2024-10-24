import matplotlib.pyplot as plt
import numpy as np

# Define the data for the chart
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_sources = ['Solar', 'Wind', 'Hydroelectric']

# Adoption levels in percentage for each continent and energy source
adoption_levels = np.array([
    [35, 40, 25],  # Africa
    [50, 30, 20],  # Asia
    [45, 50, 40],  # Europe
    [55, 35, 30],  # North America
    [40, 45, 35],  # South America
    [30, 25, 20]   # Oceania
])

# Create a figure for the 3D bar chart
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Set positions for the bars
x = np.arange(len(continents))
y = np.arange(len(energy_sources))

# Create meshgrid for bar positions
x_pos, y_pos = np.meshgrid(x, y)
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()

# Bar parameters
z_pos = np.zeros_like(x_pos)
dx = 0.5
dy = 0.3
dz = adoption_levels.flatten()

# Colors for each energy source
colors = ['#e6550d', '#31a354', '#3182bd']

# Plot each energy source as a separate layer
for i, color in enumerate(colors):
    ax.bar3d(x_pos[y_pos == i], y_pos[y_pos == i], z_pos[y_pos == i], dx, dy, dz[y_pos == i], 
             color=color, alpha=0.8, label=energy_sources[i])

# Customize the axes
ax.set_xlabel('Continent', fontsize=12, labelpad=20)
ax.set_ylabel('Energy Source', fontsize=12, labelpad=20)
ax.set_zlabel('Adoption Level (%)', fontsize=12, labelpad=10)

# Set axis labels with custom tick positions
ax.set_xticks(x)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(y)
ax.set_yticklabels(energy_sources)
ax.set_zlim(0, 60)

# Add a title
ax.set_title("Rise of Renewable Energy:\nGlobal Adoption across Continents in 2050", fontsize=16, fontweight='bold')

# Add a legend
ax.legend(loc='upper left', fontsize=10, title='Energy Sources')

# Adjust the view angle to enhance visibility
ax.view_init(elev=30, azim=130)

# Enhance grid visibility for better perception of depth
ax.grid(True, linestyle='--', linewidth=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()