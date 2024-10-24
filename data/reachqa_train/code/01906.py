import matplotlib.pyplot as plt
import numpy as np

# Years from 2050 to 2060
years = np.arange(2050, 2061)

# Trade volume data for each goods category (in million units)
minerals = [20, 25, 23, 30, 28, 35, 40, 38, 45, 42, 50]
tech_devices = [15, 18, 22, 25, 30, 34, 38, 42, 45, 48, 52]
exotic_foods = [10, 12, 12, 13, 15, 15, 16, 17, 18, 20, 22]

# Compile the data into a list
trade_volumes = np.vstack([minerals, tech_devices, exotic_foods])

# Colors for each area
colors = ['#FFD700', '#00BFFF', '#FF69B4']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, trade_volumes, labels=['Minerals', 'Tech Devices', 'Exotic Foods'], colors=colors, alpha=0.8)

# Set the title with line breaks for better readability
ax.set_title("Galactic Commerce:\nSpace Goods Trade Volume from 2050 to 2060", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Trade Volume (Million Units)", fontsize=12)

# Add a legend with location adjustments
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Customize the x and y ticks for better readability
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 121, 20))

# Gridlines for clarity
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust subplot params for a clean layout
plt.tight_layout()

# Display the plot
plt.show()