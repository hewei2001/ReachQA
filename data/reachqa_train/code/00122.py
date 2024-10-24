import matplotlib.pyplot as plt
import numpy as np

# Define the categories and years
categories = ['IDEs', 'VCS', 'Code Editors', 'Package Managers']
years = np.array([2018, 2019, 2020, 2021, 2022])

# Hypothetical market share data (in percentages) for each category and year
market_share_data = np.array([
    [30, 32, 34, 31, 30],   # IDEs
    [25, 28, 29, 30, 31],   # VCS
    [20, 22, 24, 26, 28],   # Code Editors
    [25, 18, 13, 13, 11]    # Package Managers
])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Stacked area plot
ax.stackplot(years, market_share_data, labels=categories, colors=['#FFA07A', '#20B2AA', '#778899', '#FFD700'], alpha=0.85)

# Add title and labels
ax.set_title('Tech Trends in the Digital Age:\nThe Evolution of Software Development Tools', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)

# Set x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.5)

# Place the legend outside the plot to avoid overlap
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()