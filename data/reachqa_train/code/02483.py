import matplotlib.pyplot as plt
import numpy as np

# Original Data Preparation
years = np.arange(2010, 2021)
concern_levels = np.array([4.0, 4.3, 4.7, 5.5, 5.9, 6.3, 6.8, 7.1, 7.5, 7.7, 8.0])
error_margins = np.array([0.5, 0.4, 0.6, 0.4, 0.5, 0.6, 0.7, 0.5, 0.4, 0.5, 0.6])

# New Overlay Data (e.g., number of climate change initiatives)
initiatives = np.array([2, 3, 3, 4, 5, 6, 8, 7, 9, 8, 10])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot line chart with error bars
ax1.errorbar(years, concern_levels, yerr=error_margins, fmt='-o', color='green', ecolor='lightgray',
             elinewidth=2, capsize=4, capthick=2, alpha=0.9, label='Average Concern Level')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Level of Concern (0-10)", fontsize=12, color='green')
ax1.tick_params(axis='y', labelcolor='green')

# Overlay bar chart on secondary y-axis
ax2 = ax1.twinx()
ax2.bar(years, initiatives, color='blue', alpha=0.5, label='Climate Initiatives')
ax2.set_ylabel("Number of Initiatives", fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Title and annotations
ax1.set_title("Climate Change Awareness and Action\nA Decade of Public Concern vs. Initiatives (2010-2020)",
              fontsize=16, fontweight='bold', pad=20)
ax1.annotate('Paris Agreement Signed', xy=(2015, 6.3), xytext=(2012, 8.0),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Grid and layout
ax1.grid(True, linestyle='--', alpha=0.6)
fig.tight_layout()

# Legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Set axes limits
ax1.set_xlim([2009, 2021])
ax1.set_ylim([3, 9])
ax2.set_ylim([0, 12])

# Show the plot
plt.show()