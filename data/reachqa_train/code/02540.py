import numpy as np
import matplotlib.pyplot as plt

# Define the eco-regions
regions = ["Frozen Highlands", "Lush Forests", "Arid Deserts", "Coastal Plains", "Volcanic Lowlands"]

# Define the months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Construct the average temperature data (in Celsius)
# Values are designed to reflect unique climate patterns for each region
temperature_data = np.array([
    [-15, -12, -8, -5, 0, 5, 8, 6, 2, -4, -10, -13],  # Frozen Highlands
    [10, 12, 15, 18, 21, 25, 30, 29, 26, 20, 15, 11], # Lush Forests
    [18, 20, 24, 28, 32, 35, 37, 36, 33, 29, 24, 20], # Arid Deserts
    [15, 16, 18, 20, 22, 25, 28, 27, 24, 21, 18, 16], # Coastal Plains
    [25, 28, 30, 35, 38, 40, 42, 41, 39, 34, 30, 28]  # Volcanic Lowlands
])

# Create the heat map
plt.figure(figsize=(12, 7))
heatmap = plt.imshow(temperature_data, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Add color bar with label
cbar = plt.colorbar(heatmap)
cbar.set_label('Average Temperature (°C)', fontsize=12, labelpad=10)

# Set x and y ticks
plt.xticks(ticks=np.arange(len(months)), labels=months, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(regions)), labels=regions)

# Set title and labels
plt.title('Terra Nova Climate Study\nAverage Monthly Temperatures Across Eco-Regions', fontsize=16, weight='bold', pad=20)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Eco-Regions', fontsize=12)

# Add grid lines for better separation of data
plt.grid(False)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()