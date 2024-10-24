import matplotlib.pyplot as plt
import numpy as np

# Cities and architectural elements
cities = ['Alexandria', 'Babylon', 'Athens', 'Rome']
elements = ['Temples', 'Towers', 'Palaces', 'Bridges']

# Volumes in cubic meters for each element in each city
volumes = np.array([
    [1500, 1200, 800, 1100],  # Alexandria
    [1800, 1400, 950, 1200],  # Babylon
    [1300, 1100, 850, 1000],  # Athens
    [2000, 1500, 1300, 1400]  # Rome
])

# Define the x and y coordinates for the grid
x = np.arange(len(cities))
y = np.arange(len(elements))
x, y = np.meshgrid(x, y)

# Flatten the arrays for easy plotting
x = x.flatten()
y = y.flatten()
z = np.zeros_like(x)  # Bottoms of the bars

# Flatten the volumes array for plotting
dz = volumes.flatten()

# Create the figure and axis for 3D plotting
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Define colors for different architectural elements
colors = ['#8a2be2', '#ff7f50', '#3cb371', '#ffd700']

# Plot the 3D bars
for i in range(len(elements)):
    ax.bar3d(x[i::len(elements)], y[i::len(elements)], z[i::len(elements)], 
             0.7, 0.7, dz[i::len(elements)], color=colors[i], alpha=0.8, label=elements[i])

# Set the axes labels and title
ax.set_xlabel('Cities', fontsize=12, labelpad=10)
ax.set_ylabel('Architectural Elements', fontsize=12, labelpad=15)
ax.set_zlabel('Volume (Cubic Meters)', fontsize=12, labelpad=10)
ax.set_title('Monolithic Marvels:\nArchitectural Volumes of Ancient Cities', fontsize=15, fontweight='bold', pad=20)

# Set the ticks and labels for the x and y axes
ax.set_xticks(np.arange(len(cities)) + 0.35)
ax.set_yticks(np.arange(len(elements)) + 0.35)
ax.set_xticklabels(cities, rotation=45, ha='right')
ax.set_yticklabels(elements)

# Adjust the viewing angle for better visibility
ax.view_init(elev=25, azim=135)

# Add a legend
ax.legend(loc='upper right', fontsize=10, title='Architectural Elements')

# Enable grid for clarity
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()