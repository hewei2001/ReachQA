import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the years for which the data is available
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

# Percentage contributions by each renewable energy source
solar = np.array([5, 10, 15, 20, 25, 30])
wind = np.array([10, 12, 15, 17, 19, 22])
hydro = np.array([60, 55, 50, 45, 40, 35])
biomass = np.array([25, 23, 20, 18, 16, 13])

# Stack the data for plotting
data = np.array([solar, wind, hydro, biomass])

# Define categories for the x-axis
categories = ['Solar', 'Wind', 'Hydro', 'Biomass']
x = np.arange(len(categories))

# Create the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define colors for different energy sources
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plot bars for each year
for idx, year in enumerate(years):
    ax.bar(x, data[:, idx], zs=year, zdir='y', color=colors, alpha=0.8, width=0.6, edgecolor='black')

# Customize axes
ax.set_xlabel('Energy Source', labelpad=10)
ax.set_ylabel('Year', labelpad=10)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=15, ha='right')
ax.set_yticks(years)
ax.set_yticklabels(years)
ax.set_zlim(0, 100)

# Set the viewing angle
ax.view_init(elev=20, azim=135)

# Add a descriptive title
ax.set_title('A Decade of Transformation:\nRenewable Energy Sources in the 2010s', fontsize=16, fontweight='bold')

# Create a custom legend
legend_handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(legend_handles, categories, loc='upper right', title='Energy Sources', bbox_to_anchor=(1.15, 0.9))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()