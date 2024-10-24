import matplotlib.pyplot as plt
import numpy as np

# Data for years and resource allocation from 2065 to 2075
years = np.arange(2065, 2076)
oxygen = np.array([50, 52, 54, 53, 55, 57, 56, 58, 59, 60, 61])
water = np.array([40, 42, 44, 46, 45, 47, 46, 48, 49, 50, 52])
energy = np.array([30, 32, 35, 34, 33, 35, 37, 39, 41, 43, 45])
food = np.array([20, 21, 23, 25, 26, 27, 28, 29, 30, 31, 32])
construction_materials = np.array([25, 24, 26, 28, 27, 29, 28, 27, 28, 29, 30])

# Data for technological index
tech_index = np.array([100, 105, 110, 117, 125, 130, 138, 145, 155, 160, 170])

# Stack data for the area plot
resource_data = np.vstack([oxygen, water, energy, food, construction_materials])

# Create the figure and primary y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stackplot for resource allocation
ax1.stackplot(years, resource_data, labels=['Oxygen', 'Water', 'Energy', 'Food', 'Construction Materials'],
              colors=['#76B041', '#4B9CD3', '#F5C342', '#FF6347', '#8A2BE2'], alpha=0.85)

# Setup for secondary y-axis
ax2 = ax1.twinx()
ax2.plot(years, tech_index, color='black', linestyle='-', linewidth=2.0, marker='o', label='Tech Index')
ax2.set_ylabel('Technological Index', fontsize=14)

# Add titles and labels
ax1.set_title('Resource Allocation & Technological Advancement: \nA Decade of Balance and Innovation (2065-2075)', 
              fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Allocation Units', fontsize=14)

# Customize the legends
ax1.legend(loc='upper left', fontsize=12, title='Resources', frameon=False)
ax2.legend(loc='upper right', fontsize=12, title='Tech Innovation', frameon=False)

# Customize grid and background
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_facecolor('#f0f0f0')

# Annotate notable points
ax1.text(2066, 60, 'Water Recycling\nTechnologies', fontsize=10, color='darkblue', style='italic', va='center')
ax1.text(2071, 150, 'New Solar Arrays', fontsize=10, color='darkorange', style='italic', va='center')
ax2.text(2070, 160, 'Tech Surge', fontsize=10, color='black', style='italic', va='bottom')

# Rotate x-axis labels for clarity
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Adjust layout for readability
fig.tight_layout()

# Show the plot
plt.show()