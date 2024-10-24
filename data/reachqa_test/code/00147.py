import numpy as np
import matplotlib.pyplot as plt

# Define the days of the week and household types
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
household_types = ["Single\nHousehold", "Couple\nHousehold", "Family\nHousehold", "Shared\nApartment"]

# Water usage data (in liters)
water_usage_data = np.array([
    [70, 72, 68, 75, 78, 82, 80],  # Single Household
    [120, 115, 118, 123, 130, 135, 128],  # Couple Household
    [250, 240, 245, 260, 270, 280, 265],  # Family Household
    [180, 175, 170, 185, 190, 195, 185]   # Shared Apartment
])

# Create the heat map
plt.figure(figsize=(12, 7))
cax = plt.imshow(water_usage_data, aspect='auto', cmap='coolwarm', interpolation='nearest', alpha=0.9)

# Add gridlines
plt.grid(which='minor', color='white', linestyle='-', linewidth=1.5)
plt.gca().set_xticks(np.arange(-.5, len(days), 1), minor=True)
plt.gca().set_yticks(np.arange(-.5, len(household_types), 1), minor=True)

# Title and labels
plt.title('Water Usage Patterns\nDaily Consumption Across Household Types', fontsize=16, fontweight='bold')
plt.xlabel('Days of the Week', fontsize=12)
plt.ylabel('Household Types', fontsize=12)

# Add a color bar with segmented ticks
cbar = plt.colorbar(cax, extend='both', ticks=[50, 100, 150, 200, 250, 300])
cbar.ax.set_yticklabels(['<50', '100', '150', '200', '250', '>300'])
cbar.set_label('Average Water Usage (Liters)', fontsize=12)

# Set tick labels for x and y axes
plt.xticks(ticks=np.arange(len(days)), labels=days, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(household_types)), labels=household_types)

# Add annotations inside the heatmap cells
for i in range(len(household_types)):
    for j in range(len(days)):
        plt.text(j, i, f'{water_usage_data[i, j]}', ha='center', va='center', color='black', fontsize=9)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()