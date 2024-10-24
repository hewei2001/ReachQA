import matplotlib.pyplot as plt
import numpy as np

# Years from 2200 to 2220
years = np.arange(2200, 2221)

# Resource allocation in percentages (over the years)
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

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax.stackplot(years, oxygen_production, water_recycling, food_growth,
             labels=['Oxygen Production', 'Water Recycling', 'Food Growth'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

# Add titles and labels
ax.set_title('Resource Allocation in Lunar Colonies\n(2200-2220)', fontsize=16, weight='bold')
ax.set_ylabel('Percentage of Total Resources (%)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)

# Add a legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate significant changes with vertical lines and text
ax.axvline(2210, color='grey', linestyle='--', alpha=0.6)
ax.text(2211, 60, 'Stabilization\nPhase Begins', fontsize=9, color='black', rotation=90, va='center')

ax.axvline(2215, color='grey', linestyle='--', alpha=0.6)
ax.text(2216, 50, 'Expansion\nPhase Initiated', fontsize=9, color='black', rotation=90, va='center')

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)

# Adjust layout to prevent overlap and clipping
plt.tight_layout(rect=[0, 0, 0.9, 1])  # Leave space for the legend on the right

# Show the plot
plt.show()