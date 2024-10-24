import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Data: Years from 2050 to 2060
years = np.arange(2050, 2061)

# Trade volume data for each goods category (in million units)
minerals = [20, 25, 23, 30, 28, 35, 40, 38, 45, 42, 50]
tech_devices = [15, 18, 22, 25, 30, 34, 38, 42, 45, 48, 52]
exotic_foods = [10, 12, 12, 13, 15, 15, 16, 17, 18, 20, 22]

# Compile the data
trade_volumes = np.vstack([minerals, tech_devices, exotic_foods])

# Colors for each area with colorblind-friendly palette
colors = ['#E69F00', '#56B4E9', '#009E73']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create the stacked area chart
ax.stackplot(years, trade_volumes, labels=['Minerals', 'Tech Devices', 'Exotic Foods'], colors=colors, alpha=0.8)

# Title and labels
ax.set_title("Galactic Commerce:\nSpace Goods Trade Volume from 2050 to 2060", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Trade Volume (Million Units)", fontsize=14)

# Legend with custom location
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1, 1))

# Customize ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 131, 10))

# Gridlines
ax.grid(True, linestyle='--', alpha=0.6)

# Add annotations for the peak years
peak_years = [2050 + i for i in range(len(years)) if trade_volumes.sum(axis=0)[i] in [trade_volumes.sum(axis=0).max(), trade_volumes.sum(axis=0).min()]]
for year in peak_years:
    ax.annotate(f"Peak year: {year}",
                xy=(year, trade_volumes.sum(axis=0)[year-2050]),
                xytext=(year, trade_volumes.sum(axis=0)[year-2050]+15),
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10, ha='center')

# Background and style enhancements
fig.patch.set_facecolor('#f5f5f5')
ax.set_facecolor('#ffffff')

# Add transparency to markers for clarity
ax.scatter(years, minerals, color=colors[0], s=100, edgecolor='black', alpha=0.5)
ax.scatter(years, tech_devices, color=colors[1], s=100, edgecolor='black', alpha=0.5)
ax.scatter(years, exotic_foods, color=colors[2], s=100, edgecolor='black', alpha=0.5)

# Additional plot with simple bar chart to show percentage share of each category in 2060
shares_2060 = [50, 52, 22]
fig2, ax2 = plt.subplots(figsize=(6, 6))
ax2.bar(['Minerals', 'Tech Devices', 'Exotic Foods'], shares_2060, color=colors, alpha=0.8)
ax2.set_title('Trade Volume Shares in 2060', fontsize=14, fontweight='bold')
ax2.set_ylabel('Trade Volume (Million Units)', fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()