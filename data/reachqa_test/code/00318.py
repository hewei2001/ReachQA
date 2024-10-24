import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Data: Number of renewable energy projects (in hundreds)
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America']
solar_projects = [45, 70, 65, 60, 50]
wind_projects = [30, 55, 75, 40, 35]
hydro_projects = [25, 60, 50, 45, 40]

# Set up the figure and 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Positions for the bars along the x-axis
x_pos = np.arange(len(continents))

# Define positions for different project types along the y-axis
y_pos_solar = np.zeros_like(x_pos)
y_pos_wind = np.ones_like(x_pos)
y_pos_hydro = 2 * np.ones_like(x_pos)

# Define the width, depth, and color patterns for each set of bars
width = 0.2
depth = 0.5
solar_colors = ['#FFD700', '#FFD700CC', '#FFD70099', '#FFD70066', '#FFD70033']  # Variations for Solar
wind_colors = ['#1E90FF', '#1E90FFCC', '#1E90FF99', '#1E90FF66', '#1E90FF33']  # Variations for Wind
hydro_colors = ['#32CD32', '#32CD32CC', '#32CD3299', '#32CD3266', '#32CD3233']  # Variations for Hydro

# Plot the 3D bars
for i, (x, s, w, h) in enumerate(zip(x_pos, solar_projects, wind_projects, hydro_projects)):
    ax.bar3d(x, y_pos_solar[i], 0, width, depth, s, color=solar_colors[i], alpha=0.8)
    ax.bar3d(x, y_pos_wind[i], 0, width, depth, w, color=wind_colors[i], alpha=0.8)
    ax.bar3d(x, y_pos_hydro[i], 0, width, depth, h, color=hydro_colors[i], alpha=0.8)
    
# Customizing the axes
ax.set_xlabel('Continents', fontsize=12, labelpad=10)
ax.set_ylabel('Project Type', fontsize=12, labelpad=10)
ax.set_zlabel('Projects (hundreds)', fontsize=12, labelpad=10)
ax.set_xticks(x_pos)
ax.set_xticklabels(continents, fontsize=10)
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(['Solar', 'Wind', 'Hydro'], fontsize=10)

# Adding a title with multiple lines for clarity
ax.set_title('Renewable Energy Projects Across Continents\n'
             'Distribution of Solar, Wind, and Hydro Projects', fontsize=14, fontweight='bold', pad=30)

# Add a legend with custom patches
solar_patch = mpatches.Patch(color='#FFD700', label='Solar Projects')
wind_patch = mpatches.Patch(color='#1E90FF', label='Wind Projects')
hydro_patch = mpatches.Patch(color='#32CD32', label='Hydro Projects')
ax.legend(handles=[solar_patch, wind_patch, hydro_patch], loc='upper left', bbox_to_anchor=(0.75, 0.95))

# Adjust the viewing angle for better visibility
ax.view_init(elev=30, azim=120)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()