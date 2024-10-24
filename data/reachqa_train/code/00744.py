import matplotlib.pyplot as plt
import numpy as np

# Neighborhoods and months
neighborhoods = ["Downtown", "Suburban North", "Suburban South", "Industrial Zone", "Parkside", "Riverside"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Temperature and humidity differences
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
fig, ax = plt.subplots(2, 1, figsize=(14, 10), constrained_layout=True)

# Temperature heatmap
c1 = ax[0].imshow(temperature_diff, cmap='coolwarm', aspect='auto', interpolation='nearest')
ax[0].set_xticks(np.arange(len(months)))
ax[0].set_xticklabels(months)
ax[0].set_yticks(np.arange(len(neighborhoods)))
ax[0].set_yticklabels(neighborhoods)
ax[0].set_title('Avg. Monthly Temperature Difference\nGreen-Rich vs. Sparse Areas (°C)', fontsize=14, weight='bold')
fig.colorbar(c1, ax=ax[0], orientation='vertical', label='Temp Difference (°C)')

# Humidity heatmap
c2 = ax[1].imshow(humidity_diff, cmap='Greens', aspect='auto', interpolation='nearest')
ax[1].set_xticks(np.arange(len(months)))
ax[1].set_xticklabels(months)
ax[1].set_yticks(np.arange(len(neighborhoods)))
ax[1].set_yticklabels(neighborhoods)
ax[1].set_title('Avg. Monthly Humidity Difference\nGreen-Rich vs. Sparse Areas (%)', fontsize=14, weight='bold')
fig.colorbar(c2, ax=ax[1], orientation='vertical', label='Humidity Difference (%)')

# Display the plot
plt.suptitle("Climate Mitigation Effects of Urban Green Spaces\nAcross City Neighborhoods", fontsize=16, fontweight='bold')
plt.show()