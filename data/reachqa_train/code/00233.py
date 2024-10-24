import matplotlib.pyplot as plt
import numpy as np

# Define regions and years
regions = ['Arctic', 'Africa', 'Asia', 'North America', 'South America', 'Europe', 'Australia']
years = ['2015', '2016', '2017', '2018', '2019']

# Temperature anomaly data (degrees Celsius)
temperature_data = np.array([
    [1.2, 1.4, 1.6, 1.8, 2.0],  # Arctic
    [0.3, 0.4, 0.5, 0.6, 0.7],  # Africa
    [0.2, 0.3, 0.4, 0.4, 0.5],  # Asia
    [0.4, 0.5, 0.5, 0.6, 0.7],  # North America
    [0.3, 0.4, 0.4, 0.5, 0.6],  # South America
    [0.3, 0.4, 0.5, 0.6, 0.7],  # Europe
    [0.5, 0.6, 0.7, 0.8, 0.9]   # Australia
])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(temperature_data, cmap='YlOrRd', aspect='auto', interpolation='nearest')

# Add color bar
cbar = fig.colorbar(cax, ax=ax)
cbar.set_label('Temperature Anomaly (°C)', fontsize=12)

# Set axis labels
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)

# Set a multi-line title
plt.title('Global Temperature Anomalies\nAcross Regions (2015-2019)', fontsize=14, fontweight='bold')

# Annotate each cell with the temperature anomaly value
for i in range(len(regions)):
    for j in range(len(years)):
        ax.text(j, i, f'{temperature_data[i, j]:.1f}', ha='center', va='center', color='black', fontsize=10)

# Adjust layout to prevent clipping of tick-labels and titles
plt.tight_layout()

# Display the plot
plt.show()