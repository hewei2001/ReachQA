import matplotlib.pyplot as plt
import numpy as np

# Original data for the first plot
years = np.arange(2200, 2221)
oxygen_production = [
    60, 58, 55, 53, 50, 47, 45, 43, 40, 38, 
    35, 33, 31, 30, 28, 27, 25, 24, 23, 22, 20
]
water_recycling = [
    20, 22, 23, 25, 27, 29, 30, 32, 33, 35, 
    37, 38, 39, 40, 41, 43, 45, 46, 47, 48, 50
]
food_growth = [
    20, 20, 22, 22, 23, 24, 25, 25, 27, 27, 
    28, 29, 30, 30, 31, 30, 30, 30, 30, 30, 30
]

# Constructing new data for the second plot
# Hypothetical efficiency data (efficiency of each resource allocation)
efficiency_oxygen = [0.8, 0.79, 0.78, 0.76, 0.75, 0.74, 0.72, 0.70, 0.68, 0.66,
                     0.65, 0.64, 0.62, 0.61, 0.60, 0.60, 0.59, 0.58, 0.57, 0.56, 0.55]
efficiency_water = [0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.78, 0.79, 0.80,
                    0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91]
efficiency_food = [0.75, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80, 0.81, 0.82, 0.83,
                   0.84, 0.84, 0.85, 0.86, 0.86, 0.87, 0.87, 0.88, 0.88, 0.89, 0.89]

# Create the figure and axes with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# First plot: Stacked area chart for resource allocation
ax1.stackplot(years, oxygen_production, water_recycling, food_growth,
             labels=['Oxygen Production', 'Water Recycling', 'Food Growth'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)
ax1.set_title('Resource Allocation in Lunar Colonies\n(2200-2220)', fontsize=14, weight='bold')
ax1.set_ylabel('Percentage of Total Resources (%)', fontsize=12)
ax1.set_xlabel('Year', fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize=10)
ax1.axvline(2210, color='grey', linestyle='--', alpha=0.6)
ax1.text(2211, 60, 'Stabilization\nPhase Begins', fontsize=9, color='black', rotation=90, va='center')
ax1.axvline(2215, color='grey', linestyle='--', alpha=0.6)
ax1.text(2216, 50, 'Expansion\nPhase Initiated', fontsize=9, color='black', rotation=90, va='center')
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)

# Second plot: Line plot for efficiency over time
ax2.plot(years, efficiency_oxygen, label='Oxygen Efficiency', marker='o', linestyle='-', color='#1f77b4')
ax2.plot(years, efficiency_water, label='Water Efficiency', marker='s', linestyle='-', color='#ff7f0e')
ax2.plot(years, efficiency_food, label='Food Efficiency', marker='^', linestyle='-', color='#2ca02c')
ax2.set_title('Efficiency of Resource Utilization\n(2200-2220)', fontsize=14, weight='bold')
ax2.set_ylabel('Efficiency (%)', fontsize=12)
ax2.set_xlabel('Year', fontsize=12)
ax2.legend(loc='lower right', fontsize=10)
ax2.axvline(2210, color='grey', linestyle='--', alpha=0.6)
ax2.axvline(2215, color='grey', linestyle='--', alpha=0.6)
ax2.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)

# Adjust layout to prevent overlap and clipping
plt.tight_layout()

# Show the plots
plt.show()