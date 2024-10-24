import matplotlib.pyplot as plt
import numpy as np

# Define the years and categories
years = np.array([2022, 2023, 2024, 2025, 2026])
categories = ['Electric Buses', 'Bicycle Lanes', 'Carpooling Programs']

# New initiative data for each category
electric_buses = np.array([5, 7, 9, 11, 13])
bicycle_lanes = np.array([10, 12, 15, 17, 19])
carpooling_programs = np.array([8, 10, 12, 13, 15])

# Calculate percentage increase year-over-year
electric_buses_percent_increase = np.diff(electric_buses) / electric_buses[:-1] * 100
bicycle_lanes_percent_increase = np.diff(bicycle_lanes) / bicycle_lanes[:-1] * 100
carpooling_programs_percent_increase = np.diff(carpooling_programs) / carpooling_programs[:-1] * 100

# Set up the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(18, 8))
fig.suptitle('Analysis of Eco-friendly Transportation Initiatives\nin Greenville (2022-2026)', fontsize=16, weight='bold', y=1.02)

# Subplot 1: Stacked Bar Chart
axs[0].bar(years, electric_buses, color='royalblue', edgecolor='white', label='Electric Buses', alpha=0.9)
axs[0].bar(years, bicycle_lanes, bottom=electric_buses, color='limegreen', edgecolor='white', label='Bicycle Lanes', alpha=0.9)
axs[0].bar(years, carpooling_programs, bottom=electric_buses+bicycle_lanes, color='gold', edgecolor='white', label='Carpooling Programs', alpha=0.9)
axs[0].set_title('Total New Initiatives', fontsize=14, weight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Number of New Initiatives', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(0, 50, step=5))
axs[0].legend(loc='upper left', fontsize=10, title='Initiatives', frameon=False)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Subplot 2: Line Plot for Percentage Increases
axs[1].plot(years[1:], electric_buses_percent_increase, marker='o', color='royalblue', linestyle='-', label='Electric Buses')
axs[1].plot(years[1:], bicycle_lanes_percent_increase, marker='s', color='limegreen', linestyle='--', label='Bicycle Lanes')
axs[1].plot(years[1:], carpooling_programs_percent_increase, marker='^', color='gold', linestyle=':', label='Carpooling Programs')
axs[1].set_title('Year-over-Year Percentage Increase', fontsize=14, weight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Percentage Increase (%)', fontsize=12)
axs[1].set_xticks(years[1:])
axs[1].legend(loc='upper left', fontsize=10, title='Initiatives', frameon=False)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()