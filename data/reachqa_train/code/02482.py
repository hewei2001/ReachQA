import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
concern_levels = np.array([4.0, 4.3, 4.7, 5.5, 5.9, 6.3, 6.8, 7.1, 7.5, 7.7, 8.0])
error_margins = np.array([0.5, 0.4, 0.6, 0.4, 0.5, 0.6, 0.7, 0.5, 0.4, 0.5, 0.6])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))

# Plot line chart with error bars
ax.errorbar(years, concern_levels, yerr=error_margins, fmt='-o', color='green', ecolor='lightgray',
            elinewidth=2, capsize=4, capthick=2, alpha=0.9)

# Set plot labels and title
ax.set_title("Climate Change Awareness\nA Decade of Public Concern and Data Uncertainty (2010-2020)",
             fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Level of Concern (0-10)", fontsize=12)

# Customize the grid
ax.grid(True, linestyle='--', alpha=0.6)

# Add an annotation for a significant event
ax.annotate('Paris Agreement Signed', xy=(2015, 6.3), xytext=(2012, 7.8),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Add legend
ax.legend(["Average Concern Level"], loc='upper left', fontsize=10)

# Set axes limits
ax.set_xlim([2009, 2021])
ax.set_ylim([3, 9])

# Use tight layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()