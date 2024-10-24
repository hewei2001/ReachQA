import matplotlib.pyplot as plt
import numpy as np

# Data setup
countries = ['Country A', 'Country B', 'Country C']
energy_types = ['Solar', 'Wind', 'Hydro']
percentage_distributions = np.array([
    [40, 35, 25],  # Country A
    [30, 40, 30],  # Country B
    [50, 20, 30]   # Country C
])

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define x and y positions for the bars
x_positions = np.arange(len(countries))
y_positions = np.arange(len(energy_types))
xpos, ypos = np.meshgrid(x_positions, y_positions, indexing='ij')
xpos = xpos.flatten()
ypos = ypos.flatten()

# Flatten the percentage distribution array
z_positions = np.zeros_like(xpos)
bar_heights = percentage_distributions.flatten()

# Define colors for each energy type
colors = ['#ff9999', '#66b3ff', '#99ff99']  # Solar, Wind, Hydro colors

# Create the bars
ax.bar3d(xpos, ypos, z_positions, dx=0.5, dy=0.5, dz=bar_heights, color=np.repeat(colors, len(countries)))

# Customize the plot
ax.set_title('Sustainable Energy Adoption Across Countries (2023)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Countries', labelpad=15)
ax.set_ylabel('Energy Types', labelpad=15)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_xticks(x_positions + 0.25)
ax.set_yticks(y_positions + 0.25)
ax.set_xticklabels(countries, rotation=15)
ax.set_yticklabels(energy_types)
ax.set_zlim(0, 60)

# Add a legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=energy_type, markerfacecolor=color, markersize=10) 
                   for energy_type, color in zip(energy_types, colors)]
ax.legend(handles=legend_elements, title='Energy Types', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Automatically adjust the subplot layout to make room for the legend and labels
plt.tight_layout()

# Show the plot
plt.show()