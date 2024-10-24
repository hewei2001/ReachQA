import matplotlib.pyplot as plt
import numpy as np

# Define cities and days
cities = ["New York", "Los Angeles", "London", "Beijing", "Tokyo", "Mumbai", "Sydney", "Rio de Janeiro"]
days = np.array([f'Day {i+1}' for i in range(14)])

# Create a matrix for AQI values corresponding to cities and days
aqi_values = np.array([
    [50, 55, 45, 60, 70, 68, 66, 64, 62, 70, 74, 73, 72, 75],  # New York
    [60, 80, 70, 65, 75, 78, 82, 79, 76, 73, 75, 80, 85, 90],  # Los Angeles
    [40, 45, 30, 50, 55, 58, 60, 59, 54, 53, 52, 51, 50, 48],  # London
    [150, 200, 180, 190, 210, 220, 230, 240, 245, 250, 260, 255, 250, 245],  # Beijing
    [45, 50, 40, 55, 60, 62, 64, 61, 59, 58, 57, 56, 55, 54],  # Tokyo
    [100, 110, 90, 95, 85, 80, 78, 76, 74, 70, 72, 75, 77, 80],  # Mumbai
    [30, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16],  # Sydney
    [75, 80, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48]   # Rio de Janeiro
])

# Calculate averages for AQI
aqi_avg = np.mean(aqi_values, axis=1)

# Create the main figure
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# Heatmap
heatmap = axs[0].imshow(aqi_values, cmap='YlOrRd', aspect='auto', interpolation='nearest')
axs[0].set_title('Heat Map of Air Quality Index (AQI) Across Major Cities\n2023', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Days', fontsize=12)
axs[0].set_ylabel('Cities', fontsize=12)
axs[0].set_xticks(np.arange(len(days)))
axs[0].set_xticklabels(days, rotation=45)
axs[0].set_yticks(np.arange(len(cities)))
axs[0].set_yticklabels(cities)

# Add a color bar
cbar = plt.colorbar(heatmap, ax=axs[0], orientation='vertical')
cbar.set_label('Air Quality Index (µg/m³)', rotation=270, labelpad=20)

# Annotate each cell with the numeric value
for (i, j), value in np.ndenumerate(aqi_values):
    axs[0].text(j, i, value, ha='center', va='center', color='black', fontsize=8)

# Line plot for AQI averages
axs[1].plot(cities, aqi_avg, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)
axs[1].set_title('Average AQI per City Over 14 Days\n2023', fontsize=16, fontweight='bold')
axs[1].set_ylabel('Average AQI (µg/m³)', fontsize=12)
axs[1].set_xlabel('Cities', fontsize=12)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Add horizontal line at common AQI thresholds
thresholds = [50, 100, 150, 200, 300]
for th in thresholds:
    axs[1].axhline(y=th, color='red', linestyle='--', alpha=0.5)
    axs[1].text(len(cities) - 0.5, th + 2, f'AQI {th}', color='red', ha='right')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()