import matplotlib.pyplot as plt
import numpy as np

# Define decades and average sea surface temperatures for each region
decades = np.array(['1980s', '1990s', '2000s', '2010s', '2020s'])
north_atlantic_temps = np.array([12.5, 13.0, 13.5, 14.0, 14.7])
east_pacific_temps = np.array([14.0, 14.3, 14.6, 15.0, 15.5])
west_indian_ocean_temps = np.array([26.8, 27.0, 27.4, 27.9, 28.3])

# Create the plot
plt.figure(figsize=(12, 8))

# Plot data for each coastal region with different styles
plt.plot(decades, north_atlantic_temps, marker='o', linestyle='-', linewidth=2, color='teal', label='North Atlantic Coast')
plt.plot(decades, east_pacific_temps, marker='s', linestyle='--', linewidth=2, color='tomato', label='East Pacific Coast')
plt.plot(decades, west_indian_ocean_temps, marker='^', linestyle='-.', linewidth=2, color='gold', label='West Indian Ocean')

# Annotate notable points for analysis
notable_events = {
    '1990s': (north_atlantic_temps[1], "Warmest 1990s\nin history"),
    '2020s': (west_indian_ocean_temps[4], "Record high\nin West Indian Ocean"),
    '1980s': (east_pacific_temps[0], "Baseline year")
}
for decade, (y_value, event) in notable_events.items():
    plt.annotate(event, xy=(decade, y_value), xytext=(0, 10), textcoords="offset points",
                 ha='center', fontsize=9, color='darkgrey', arrowprops=dict(arrowstyle='->', color='black'))

# Customize plot
plt.title("Decadal Trends in Average Sea Surface Temperatures\nAcross Key Coastal Regions", fontsize=16, weight='bold')
plt.xlabel("Decades", fontsize=14)
plt.ylabel("Average Sea Surface Temperature (°C)", fontsize=14)
plt.xticks(decades, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()