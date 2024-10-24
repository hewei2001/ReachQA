import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Define years and ocean regions
years = np.arange(2010, 2021)
ocean_regions = ["North Atlantic", "South Atlantic", "North Pacific", "South Pacific", "Indian Ocean"]

# Temperature anomalies data (°C)
temperature_anomalies = np.array([
    [0.12, 0.15, 0.16, 0.18, 0.21, 0.24, 0.28, 0.30, 0.33, 0.35, 0.37],  # North Atlantic
    [0.08, 0.10, 0.11, 0.13, 0.16, 0.18, 0.20, 0.23, 0.25, 0.28, 0.30],  # South Atlantic
    [0.14, 0.16, 0.18, 0.21, 0.23, 0.26, 0.29, 0.31, 0.34, 0.36, 0.39],  # North Pacific
    [0.10, 0.12, 0.13, 0.15, 0.18, 0.20, 0.22, 0.25, 0.27, 0.29, 0.32],  # South Pacific
    [0.09, 0.11, 0.12, 0.14, 0.17, 0.19, 0.21, 0.24, 0.26, 0.28, 0.31]   # Indian Ocean
])

# Create a figure and axis
plt.figure(figsize=(14, 7))

# Plotting with imshow
heatmap = plt.imshow(temperature_anomalies, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Adding a color bar
cbar = plt.colorbar(heatmap)
cbar.set_label('Temperature Anomaly (°C)', rotation=270, labelpad=20)

# Add title and labels
plt.title('Global Ocean Temperature Anomalies:\nA Decade of Climate Observation (2010-2020)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ocean Region', fontsize=12)

# Set ticks
plt.xticks(ticks=np.arange(len(years)), labels=years, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(ocean_regions)), labels=ocean_regions)

# Enable grid
plt.grid(False)  # Disable the grid overlay of imshow, but optional

# Annotations on heatmap
for i in range(len(ocean_regions)):
    for j in range(len(years)):
        plt.text(j, i, f'{temperature_anomalies[i, j]:.2f}', ha='center', va='center', color='black', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()