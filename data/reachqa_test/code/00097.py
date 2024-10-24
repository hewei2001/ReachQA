import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Define the years from 2015 to 2025
years = np.arange(2015, 2026)

# E-commerce sales growth percentages for each holiday season over the years
black_friday_growth = [5, 6, 7, 10, 15, 18, 20, 22, 25, 28, 30]
cyber_monday_growth = [4, 5, 6, 9, 13, 16, 19, 21, 23, 26, 29]
christmas_growth = [3, 4, 5, 8, 12, 14, 17, 19, 21, 24, 27]
new_year_growth = [2, 3, 4, 6, 9, 11, 14, 16, 18, 21, 24]

# Cumulative growth calculation for secondary y-axis
cumulative_growth = np.array(black_friday_growth) + np.array(cyber_monday_growth) + \
                    np.array(christmas_growth) + np.array(new_year_growth)

# Create a figure with two subplots (main plot + comparison plot)
fig, ax1 = plt.subplots(figsize=(14, 10))
ax2 = ax1.twinx()

# Plot each holiday season with distinctive line styles and markers
black_friday_line, = ax1.plot(years, black_friday_growth, marker='o', linestyle='-', color='navy', linewidth=2, label='Black Friday')
cyber_monday_line, = ax1.plot(years, cyber_monday_growth, marker='s', linestyle='--', color='darkorange', linewidth=2, label='Cyber Monday')
christmas_line, = ax1.plot(years, christmas_growth, marker='^', linestyle='-.', color='forestgreen', linewidth=2, label='Christmas')
new_year_line, = ax1.plot(years, new_year_growth, marker='d', linestyle=':', color='darkmagenta', linewidth=2, label='New Year')

# Adding a secondary y-axis for cumulative growth
cumulative_line, = ax2.plot(years, cumulative_growth, marker='x', linestyle='-', color='gray', linewidth=2, alpha=0.5, label='Cumulative Growth')

# Add title and axis labels
ax1.set_title("E-commerce Sales Growth During Key Holiday Seasons\nand Cumulative Growth (2015-2025)", fontsize=15, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=13)
ax1.set_ylabel("Growth (%)", fontsize=13)
ax2.set_ylabel("Cumulative Growth (%)", fontsize=13, color='gray')

# Add legends to identify the lines
ax1.legend(loc='upper left', fontsize=11)
ax2.legend(loc='upper right', fontsize=11)

# Add a grid for better readability
ax1.grid(True, linestyle='--', alpha=0.5)

# Set x-axis ticks and rotate labels for clarity
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Adjust layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()