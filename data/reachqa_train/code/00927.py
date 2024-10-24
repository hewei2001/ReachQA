import matplotlib.pyplot as plt
import numpy as np

# Define regions and coffee types
regions = ['Americas', 'Europe', 'Asia-Pacific']
coffee_types = ['Espresso', 'Latte', 'Cold Brew']

# Adjusted data: percentage of consumption for each coffee type by region
data = np.array([
    [55, 25, 20],  # Americas: Espresso, Latte, Cold Brew
    [35, 40, 25],  # Europe: Espresso, Latte, Cold Brew
    [20, 30, 50]   # Asia-Pacific: Espresso, Latte, Cold Brew
])

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Set positions for bars
xpos, ypos = np.meshgrid(np.arange(len(regions)), np.arange(len(coffee_types)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Flatten data for easy bar plotting
dz = data.flatten()

# Define bar width and depth
dx = dy = 0.5

# Choose distinct colors for each coffee type
colors = ['#8B4513', '#DEB887', '#D2B48C']

# Plot each bar
for i in range(len(coffee_types)):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i], 
             color=colors[i], alpha=0.8, label=coffee_types[i])

# Label axes
ax.set_xlabel('Regions', fontsize=12, labelpad=10)
ax.set_ylabel('Coffee Types', fontsize=12, labelpad=10)
ax.set_zlabel('Percentage (%)', fontsize=12, labelpad=10)

# Set x and y ticks
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(coffee_types)))
ax.set_yticklabels(coffee_types, fontsize=10)

# Normalize the z-axis
ax.set_zlim(0, 100)

# Set title
plt.title('Regional Coffee Consumption\nBreakdown: 2023', fontsize=16, weight='bold', pad=20)

# Add legend
ax.legend(title='Coffee Types', loc='upper left', fontsize=10)

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()