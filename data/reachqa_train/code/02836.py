import matplotlib.pyplot as plt
import numpy as np

# Define the years and categories
years = np.array([2022, 2023, 2024, 2025, 2026])
categories = ['Electric Buses', 'Bicycle Lanes', 'Carpooling Programs']

# New initiative data for each category
electric_buses = np.array([5, 7, 9, 11, 13])
bicycle_lanes = np.array([10, 12, 15, 17, 19])
carpooling_programs = np.array([8, 10, 12, 13, 15])

# Compute cumulative initiatives for stacking
bicycle_cumulative = electric_buses + bicycle_lanes
carpooling_cumulative = bicycle_cumulative + carpooling_programs

# Set up the figure
plt.figure(figsize=(12, 8))

# Plot the stacked bar chart
plt.bar(years, electric_buses, color='royalblue', edgecolor='white', label='Electric Buses', alpha=0.9)
plt.bar(years, bicycle_lanes, bottom=electric_buses, color='limegreen', edgecolor='white', label='Bicycle Lanes', alpha=0.9)
plt.bar(years, carpooling_programs, bottom=bicycle_cumulative, color='gold', edgecolor='white', label='Carpooling Programs', alpha=0.9)

# Add title and labels
plt.title('Growth of Eco-friendly Transportation Initiatives in Greenville\n(2022-2026)', fontsize=14, weight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of New Initiatives', fontsize=12)

# Adjust x-axis ticks and labels for better readability
plt.xticks(years)
plt.yticks(np.arange(0, 50, step=5))
plt.ylim(0, 50)

# Add legend and grid
plt.legend(loc='upper left', fontsize=10, title='Initiatives', frameon=False)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()