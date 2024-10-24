import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2010, 2021)

# Artificial data for transportation modes (in thousands of trips)
bicycle_usage = np.array([10, 15, 20, 25, 35, 50, 70, 90, 110, 130, 155])
bus_usage = np.array([100, 102, 103, 105, 108, 110, 115, 120, 125, 130, 135])
metro_usage = np.array([50, 60, 70, 85, 100, 115, 130, 145, 160, 175, 190])

# Stack the data
usage_data = np.vstack([bicycle_usage, bus_usage, metro_usage])

# Plot the stacked area chart
plt.figure(figsize=(12, 7))
plt.stackplot(years, usage_data, labels=['Bicycle', 'Bus', 'Metro'], colors=['#FFD700', '#87CEEB', '#32CD32'], alpha=0.8)

# Add titles and labels
plt.title('Transportation Transformation in Transopolis\n(2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Trips (Thousands)', fontsize=12)

# Customize the x-ticks and y-ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 501, 50))

# Add a legend and customize its position
plt.legend(loc='upper left', fontsize=10, title='Mode of Transport')

# Enable grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to ensure there is no overlap
plt.tight_layout()

# Display the chart
plt.show()