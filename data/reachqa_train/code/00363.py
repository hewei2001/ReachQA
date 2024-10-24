import matplotlib.pyplot as plt
import numpy as np

# Define months and water sources
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sources = ['Groundwater', 'Rainwater Harvesting', 'River Water']

# Artificial data representing water consumption in thousands of gallons
groundwater = [80, 75, 70, 65, 60, 55, 50, 55, 60, 65, 70, 75]
rainwater_harvesting = [10, 15, 20, 40, 60, 80, 110, 130, 100, 70, 30, 15]
river_water = [50, 55, 60, 50, 40, 35, 40, 50, 60, 65, 70, 60]

# Stack the data for the area chart
water_data = np.array([groundwater, rainwater_harvesting, river_water])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart using fill_between for customization
ax.fill_between(months, 0, groundwater, label=sources[0], color='#1f77b4', alpha=0.7)
ax.fill_between(months, groundwater, np.array(groundwater) + np.array(rainwater_harvesting), label=sources[1], color='#2ca02c', alpha=0.7)
ax.fill_between(months, np.array(groundwater) + np.array(rainwater_harvesting), np.sum(water_data, axis=0), label=sources[2], color='#ff7f0e', alpha=0.7)

# Set the title and labels with appropriate styling
ax.set_title("Monthly Water Consumption by Source\nin a Small Town", fontsize=14, weight='bold')
ax.set_ylabel("Water Consumption (Thousands of Gallons)", fontsize=12)
ax.set_xlabel("Month", fontsize=12)

# Enable grid with customized style for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Add legend and adjust label positions
ax.legend(loc='upper left', title="Water Source")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent clipping and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()