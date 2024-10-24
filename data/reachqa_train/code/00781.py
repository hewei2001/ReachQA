import matplotlib.pyplot as plt
import numpy as np

# Define the years and regions
years = np.arange(2013, 2024)
regions = ['North', 'South', 'East', 'West']

# Power generation data in Gigawatts for each region over the years
north_power = [1, 2, 3, 5, 7, 10, 13, 17, 22, 28, 35]
south_power = [1.5, 3, 4.5, 6.5, 9, 12, 15, 19, 24, 30, 37]
east_power = [0.5, 1.5, 3, 5, 8, 12, 16, 21, 27, 34, 42]
west_power = [2, 3.5, 5, 7.5, 10, 13, 17, 22, 28, 35, 43]

# Stack the data for plotting the area chart
power_data = np.vstack([north_power, south_power, east_power, west_power])

# Calculate the average power generation across all regions per year
average_power = np.mean(power_data, axis=0)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the stacked area chart
ax.stackplot(years, power_data, labels=regions, colors=['#FFA07A', '#20B2AA', '#778899', '#FFD700'], alpha=0.8)

# Overlay line plot for the average power generation
ax.plot(years, average_power, label='Average Power Generation', color='black', linewidth=2.5, marker='o')

# Set titles and labels
ax.set_title('Tracking Solar Power Generation Over a Decade:\nRegional and Average Trends in SunnyLand', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Cumulative Power Output (GW)', fontsize=12)

# Adding legend
ax.legend(loc='upper left', title='Legend', fontsize=10)

# Enhance readability
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 181, 20))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()