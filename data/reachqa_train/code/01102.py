import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the countries and years
countries = ['USA', 'Russia', 'Japan', 'Germany', 'Canada']
years = ['2020', '2021', '2022', '2023']

# Data: Number of research projects per year by each country
research_projects = np.array([
    [50, 55, 60, 65],  # USA
    [40, 42, 45, 48],  # Russia
    [20, 25, 27, 29],  # Japan
    [15, 20, 23, 25],  # Germany
    [10, 13, 15, 18]   # Canada
])

# Create a figure and a 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define a colormap for different countries
colors = plt.cm.viridis(np.linspace(0, 1, len(countries)))

# Bar position setup
_x = np.arange(len(years))
_y = np.arange(len(countries))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Initial bottom position of bars
bottom = np.zeros_like(x, dtype=float)

# Plot each country's data as separate bars
for country_idx in range(len(countries)):
    for year_idx in range(len(years)):
        z = research_projects[country_idx, year_idx]
        ax.bar3d(x[year_idx::len(years)][country_idx], 
                 y[year_idx::len(years)][country_idx], 
                 bottom[year_idx::len(years)][country_idx], 
                 0.8, 0.8, z, color=colors[country_idx], alpha=0.8)
        bottom[year_idx::len(years)][country_idx] += z

# Formatting the plot
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Country', labelpad=10)
ax.set_zlabel('Research Projects', labelpad=10)
ax.set_title('International Space Station Research Contributions\n(2020-2023)', fontsize=14, fontweight='bold')

# Set the ticks for the years and countries
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=15, ha='right')
ax.set_yticks(np.arange(len(countries)))
ax.set_yticklabels(countries)

# Adjust the view angle for better visibility
ax.view_init(elev=25, azim=140)

# Add a legend manually (since bar3d doesn't support stacking legends easily)
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(countries))]
ax.legend(legend_handles, countries, loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10, title='Country')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()