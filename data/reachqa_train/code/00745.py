import matplotlib.pyplot as plt
import numpy as np

# Data setup
neighborhoods = ["Downtown", "Suburban North", "Suburban South", "Industrial Zone", "Parkside", "Riverside"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature_diff = np.array([
    [-2.1, -1.5, -0.8, 0.0, 1.2, 1.8, 2.5, 2.3, 1.0, 0.4, -0.6, -1.8],
    [0.5, 1.0, 1.8, 2.3, 3.1, 3.5, 3.8, 3.6, 2.9, 2.1, 1.3, 0.7],
    [0.8, 1.2, 2.0, 2.4, 3.5, 4.0, 4.3, 4.0, 3.4, 2.5, 1.5, 1.0],
    [-3.0, -2.5, -1.2, -0.5, 0.8, 1.5, 2.2, 1.9, 0.5, -0.3, -1.5, -2.5],
    [1.8, 2.0, 2.8, 3.5, 4.5, 5.0, 5.2, 5.0, 4.1, 3.0, 2.2, 1.5],
    [1.5, 1.8, 2.5, 3.0, 4.0, 4.6, 4.8, 4.5, 3.7, 2.8, 2.0, 1.2]
])

humidity_diff = np.array([
    [-5, -4, -2, 0, 1, 2, 3, 2, 0, -1, -3, -4],
    [1, 3, 4, 5, 6, 7, 8, 7, 6, 4, 3, 2],
    [2, 3, 5, 6, 8, 9, 10, 9, 7, 5, 4, 3],
    [-6, -5, -3, -1, 0, 1, 2, 1, 0, -2, -4, -5],
    [4, 5, 6, 7, 9, 10, 11, 10, 8, 6, 5, 4],
    [3, 4, 5, 7, 8, 9, 10, 9, 7, 6, 4, 3]
])

# Initialize the plot
fig, ax = plt.subplots(2, 1, figsize=(16, 12), constrained_layout=True)

# Temperature heatmap
c1 = ax[0].imshow(temperature_diff, cmap='coolwarm', aspect='auto', interpolation='nearest')
ax[0].set_xticks(np.arange(len(months)))
ax[0].set_xticklabels(months)
ax[0].set_yticks(np.arange(len(neighborhoods)))
ax[0].set_yticklabels(neighborhoods)
ax[0].set_title('Avg. Monthly Temperature Difference\nGreen-Rich vs. Sparse Areas (°C)', fontsize=14, weight='bold')

# Annotate each cell with temperature data
for i in range(len(neighborhoods)):
    for j in range(len(months)):
        ax[0].text(j, i, f"{temperature_diff[i, j]:.1f}", ha='center', va='center', color='black', fontsize=8)

fig.colorbar(c1, ax=ax[0], orientation='vertical', label='Temp Difference (°C)')

# Humidity heatmap
c2 = ax[1].imshow(humidity_diff, cmap='YlGn', aspect='auto', interpolation='nearest')
ax[1].set_xticks(np.arange(len(months)))
ax[1].set_xticklabels(months)
ax[1].set_yticks(np.arange(len(neighborhoods)))
ax[1].set_yticklabels(neighborhoods)
ax[1].set_title('Avg. Monthly Humidity Difference\nGreen-Rich vs. Sparse Areas (%)', fontsize=14, weight='bold')

# Annotate each cell with humidity data
for i in range(len(neighborhoods)):
    for j in range(len(months)):
        ax[1].text(j, i, f"{humidity_diff[i, j]}", ha='center', va='center', color='black', fontsize=8)

fig.colorbar(c2, ax=ax[1], orientation='vertical', label='Humidity Difference (%)')

# Add gridlines for clarity
for axis in ax:
    axis.grid(False)
    axis.set_xticks(np.arange(-.5, len(months), 1), minor=True)
    axis.set_yticks(np.arange(-.5, len(neighborhoods), 1), minor=True)
    axis.grid(which="minor", color="w", linestyle='-', linewidth=2)

# Title for the entire figure
plt.suptitle("Climate Mitigation Effects of Urban Green Spaces\nAcross City Neighborhoods", fontsize=16, fontweight='bold')

# Adjust layout
plt.show()