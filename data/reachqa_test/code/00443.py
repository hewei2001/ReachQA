import matplotlib.pyplot as plt
import numpy as np

# Define regions and time management aspects
regions = ['Eon Plains', 'Twilight Heights', 'Dawn Valley', 'Dusk Ridge', 'Eclipse Peninsula']
aspects = ['Temporal Acceleration', 'Time Dilation', 'Chrono Stability', 'Time Reversal Efficiency']

# Adjusted energy management capacities (arbitrary units) for better distribution
data = np.array([
    [55, 40, 35, 20],  # Eon Plains
    [45, 35, 30, 25],  # Twilight Heights
    [40, 45, 30, 25],  # Dawn Valley
    [50, 30, 20, 10],  # Dusk Ridge
    [35, 40, 25, 30]   # Eclipse Peninsula
])

# Create a 3D plot
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection='3d')

# Set positions for bars
_x = np.arange(len(regions))
_y = np.arange(len(aspects))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Bar sizes
z = np.zeros_like(x)
dx = dy = 0.6  # Increased bar width
dz = data.T.ravel()

# Plot the bars
colors = plt.cm.viridis(np.linspace(0, 1, len(aspects)))
for i, c in enumerate(colors):
    idx = _yy.ravel() == i
    ax.bar3d(x[idx], y[idx], z[idx], dx, dy, dz[idx], color=c, alpha=0.8, edgecolor='k', linewidth=0.5)

# Setting labels and title
ax.set_xlabel('Regions', labelpad=50)
ax.set_ylabel('Time Management Aspects', labelpad=20)
ax.set_zlabel('Energy Capacity (Units)', labelpad=15)
ax.set_xticks(_x + dx/2)
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax.set_yticks(_y + dy/2)
ax.set_yticklabels(aspects, fontsize=10)
ax.set_title('Time Tower Energy Distribution in Chronon: A 3D Exploration\nof Temporal Resources', pad=35, fontsize=16)

# Enhance axis and grid
ax.view_init(elev=25, azim=135)  # Adjusted view angle for better visualization
ax.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Add a legend
legend_handles = [plt.Rectangle((0,0),1,1, color=colors[i]) for i in range(len(aspects))]
ax.legend(legend_handles, aspects, title='Aspects', loc='upper right')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()