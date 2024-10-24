import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Data for tech startups across three major cities
cities = ['San Francisco', 'New York', 'Berlin']
years_since_founding = np.array([1, 2, 3, 5, 6, 3, 4, 5, 7, 8, 6])
funding_amounts = np.array([120, 300, 250, 500, 600, 450, 400, 350, 750, 800, 550])
valuations = np.array([600, 1500, 1200, 2000, 2300, 1800, 1700, 1600, 2800, 3100, 1900])

# Assign each startup to a city (corrected to match data arrays)
city_indices = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1])

# Define colors using a colormap
colormap = cm.get_cmap('viridis', len(cities))
colors = [colormap(i) for i in range(len(cities))]

# Create a 3D scatter plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each startup
for i in range(len(years_since_founding)):
    ax.scatter(
        years_since_founding[i],
        funding_amounts[i],
        valuations[i],
        s=valuations[i] / 2.5,  # Adjust bubble size scaling
        c=[colors[city_indices[i]]],  # Color based on city
        alpha=0.7,  # Adjusted transparency
        edgecolor='k',  # Black edge for better contrast
        linewidth=0.5
    )

# Add more descriptive axis labels
ax.set_xlabel('Years Since Founding', labelpad=10, fontsize=10)
ax.set_ylabel('Funding Amount ($M)', labelpad=10, fontsize=10)
ax.set_zlabel('Startup Valuation ($M)', labelpad=10, fontsize=10)

# Set a multiline title to handle long text
ax.set_title('Tech Startups Boom\nVenture Capital Trends in Emerging Cities\nOver Time', pad=30, fontsize=12)

# Add a legend with a distinct placement
handles = [plt.Line2D([0], [0], marker='o', color='w', label=cities[i],
                      markerfacecolor=colors[i], markersize=10, alpha=0.7, markeredgecolor='k', markeredgewidth=0.5) for i in range(len(cities))]
ax.legend(handles, cities, loc='upper left', bbox_to_anchor=(1.08, 1), title="City", fontsize=8)

# Add grid for better depth perception
ax.grid(True, linestyle='--', alpha=0.5)

# Apply a better viewing angle
ax.view_init(elev=15, azim=125)

# Use tight_layout to automatically adjust spacing
plt.tight_layout()

# Display the plot
plt.show()