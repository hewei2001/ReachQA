import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Define population data for each species (adjusted for clarity and storytelling)
blue_ridge_lynx = np.array([15, 18, 22, 27, 32, 40, 50, 65, 80, 95, 110])
golden_eagle = np.array([25, 28, 26, 30, 27, 29, 31, 28, 30, 32, 33])
river_dolphin = np.array([50, 48, 45, 42, 38, 35, 32, 30, 27, 24, 21])

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with distinct markers and lines
ax.plot(years, blue_ridge_lynx, label='Blue Ridge Lynx', color='dodgerblue', marker='o', linewidth=2, linestyle='-')
ax.plot(years, golden_eagle, label='Golden Eagle', color='gold', marker='s', linewidth=2, linestyle='--')
ax.plot(years, river_dolphin, label='River Dolphin', color='salmon', marker='^', linewidth=2, linestyle='-.')

# Enhance the plot with a title, labels, and legend
ax.set_title('Decade of Change:\nWildlife Populations in Green Haven Sanctuary (2010-2020)',
             fontsize=16, fontweight='bold', loc='center', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population Count', fontsize=12)
ax.legend(loc='upper right', fontsize=10, frameon=True)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Set x-axis ticks and rotate them for better visibility
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Highlight significant events with annotations
ax.annotate('Lynx Breeding Success', xy=(2018, 80), xytext=(2016, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Eagle Population Stabilizes', xy=(2015, 29), xytext=(2012, 35),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Dolphin Habitat Loss', xy=(2020, 21), xytext=(2017, 25),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()