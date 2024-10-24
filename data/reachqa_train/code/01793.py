import matplotlib.pyplot as plt
import numpy as np

# Ocean regions and months
regions = ['North Atlantic', 'South Atlantic', 'North Pacific', 'South Pacific', 'Indian Ocean', 'Southern Ocean']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Temperature data (in Celsius) for each region over the months
temperature_data = np.array([
    [7, 8, 9, 10, 12, 14, 16, 16, 14, 12, 9, 7],  # North Atlantic
    [26, 26, 25, 24, 23, 22, 21, 21, 22, 23, 25, 26],  # South Atlantic
    [5, 6, 8, 10, 13, 16, 18, 18, 16, 13, 9, 6],  # North Pacific
    [22, 23, 23, 22, 21, 20, 18, 18, 19, 21, 22, 23],  # South Pacific
    [28, 28, 29, 30, 30, 29, 28, 28, 28, 29, 29, 28],  # Indian Ocean
    [-1, 0, 1, 2, 3, 3, 2, 2, 1, 0, -1, -1]  # Southern Ocean
])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
heatmap = ax.imshow(temperature_data, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Add color bar
cbar = plt.colorbar(heatmap)
cbar.set_label('Temperature (°C)', fontsize=12)

# Set labels, title, and adjust layout
ax.set_title('Monthly Ocean Temperature Variations\nAcross Global Oceans', fontsize=14, pad=20)
ax.set_xticks(np.arange(len(months)))
ax.set_yticks(np.arange(len(regions)))
ax.set_xticklabels(months, fontsize=10, rotation=45, ha='right')
ax.set_yticklabels(regions, fontsize=10)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Ocean Regions', fontsize=12)

# Annotate each cell with the temperature value
for i in range(len(regions)):
    for j in range(len(months)):
        ax.text(j, i, f'{temperature_data[i, j]}°C', va='center', ha='center', color='black', fontsize=8)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()