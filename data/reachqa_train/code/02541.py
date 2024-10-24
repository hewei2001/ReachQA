import numpy as np
import matplotlib.pyplot as plt

# Define the eco-regions
regions = ["Frozen Highlands", "Lush Forests", "Arid Deserts", "Coastal Plains", "Volcanic Lowlands"]

# Define the months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Average temperature data (in Celsius)
temperature_data = np.array([
    [-15, -12, -8, -5, 0, 5, 8, 6, 2, -4, -10, -13],  # Frozen Highlands
    [10, 12, 15, 18, 21, 25, 30, 29, 26, 20, 15, 11], # Lush Forests
    [18, 20, 24, 28, 32, 35, 37, 36, 33, 29, 24, 20], # Arid Deserts
    [15, 16, 18, 20, 22, 25, 28, 27, 24, 21, 18, 16], # Coastal Plains
    [25, 28, 30, 35, 38, 40, 42, 41, 39, 34, 30, 28]  # Volcanic Lowlands
])

# Average precipitation data (in mm)
precipitation_data = np.array([
    [60, 52, 45, 30, 25, 20, 18, 22, 30, 40, 55, 65],  # Frozen Highlands
    [120, 110, 95, 80, 75, 70, 65, 80, 90, 100, 110, 115], # Lush Forests
    [5, 7, 8, 10, 5, 3, 2, 3, 4, 7, 8, 5], # Arid Deserts
    [90, 85, 80, 75, 70, 65, 60, 70, 80, 85, 90, 95], # Coastal Plains
    [20, 18, 15, 12, 10, 8, 6, 8, 10, 14, 18, 20]  # Volcanic Lowlands
])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Heatmap for temperature
heatmap = ax1.imshow(temperature_data, cmap='coolwarm', aspect='auto', interpolation='nearest')
cbar = plt.colorbar(heatmap, ax=ax1)
cbar.set_label('Avg Temperature (°C)', fontsize=12, labelpad=10)

# Set x and y ticks for the heatmap
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(regions)))
ax1.set_yticklabels(regions)

# Line plot for precipitation
ax2 = ax1.twinx()
for i in range(len(regions)):
    ax2.plot(months, precipitation_data[i], label=regions[i], linestyle='--', marker='o')

ax2.set_ylabel('Avg Precipitation (mm)', fontsize=12)

# Set title and labels
plt.title('Terra Nova Climate Study\nTemperature and Precipitation Patterns Across Eco-Regions', 
          fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Eco-Regions', fontsize=12)

# Legend for precipitation lines
ax2.legend(loc='upper left', bbox_to_anchor=(1.1, 1), title='Eco-Regions')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()