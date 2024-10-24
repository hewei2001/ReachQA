import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define years and regions
years = np.arange(2025, 2036)
regions = ['Flavorland', 'New Aroma City', 'Taste Haven']

# Market share percentage data for Citrus, Berry, Exotic, Classic
market_share_data = np.array([
    [30, 20, 25, 25],   # 2025
    [32, 19, 27, 22],   # 2026
    [34, 18, 28, 20],   # 2027
    [36, 17, 29, 18],   # 2028
    [38, 16, 30, 16],   # 2029
    [39, 15, 31, 15],   # 2030
    [40, 15, 32, 13],   # 2031
    [41, 14, 33, 12],   # 2032
    [42, 13, 34, 11],   # 2033
    [43, 12, 35, 10],   # 2034
    [44, 11, 36, 9]     # 2035
])

# Colors for different beverage flavors
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9']  # Citrus, Berry, Exotic, Classic

# Create a new figure and set the 3D projection
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting
for i, region in enumerate(regions):
    xs = np.repeat(years, market_share_data.shape[1])
    ys = np.full(xs.shape, i * 5)
    zs = np.zeros(years.shape)

    # Cumulative stacking of bars
    for j, (color, label) in enumerate(zip(colors, ['Citrus', 'Berry', 'Exotic', 'Classic'])):
        height = market_share_data[:, j]
        ax.bar3d(xs[j::4], ys[j::4], zs, dx=0.8, dy=0.8, dz=height, color=color, alpha=0.8, label=label if i == 0 else "")
        zs += height

# Set labels and titles
ax.set_xlabel('Year')
ax.set_ylabel('Region')
ax.set_zlabel('Market Share (%)')
ax.set_yticks([i * 5 for i in range(len(regions))])
ax.set_yticklabels(regions)

# Adjust the view angle for better visibility
ax.view_init(elev=25, azim=135)

# Adjust layout to prevent label overlap
plt.tight_layout()

# Unique legend for the plot
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:4], labels[:4], loc='upper left')

# Title with a newline for clarity
plt.title('Market Share of Beverage Flavors\nin Future Markets (2025-2035)', pad=20)

plt.show()