import numpy as np
import matplotlib.pyplot as plt

# Define decades and renewable energy sources
decades = np.arange(1990, 2031, 5)
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal']

# Hypothetical data for each energy source
solar = np.array([2, 3, 5, 10, 15, 22, 28, 35, 40])
wind = np.array([3, 4, 7, 12, 18, 25, 32, 38, 44])
hydroelectric = np.array([50, 48, 45, 42, 40, 38, 35, 33, 30])
geothermal = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10])

# Combine the data for stacking
data = np.vstack([solar, wind, hydroelectric, geothermal])

# Create a figure for the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(decades, data, labels=energy_sources, alpha=0.8,
             colors=['#FFCC00', '#66CCFF', '#99FF99', '#FF6666'])

# Title and labels
ax.set_title('Evolution of Renewable Energy Sources\n(1990-2030)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Energy Production', fontsize=12)

# Set x-ticks to avoid overlap and rotate them
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=45)

# Add grid and legend
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title='Renewable Sources', fontsize=10)

# Add a line at 100% for reference
ax.axhline(100, color='gray', linewidth=1.5, linestyle='--', alpha=0.6)

# Ensure the layout is adjusted for better readability
plt.tight_layout()

# Show the plot
plt.show()