import matplotlib.pyplot as plt
import numpy as np

# Years from 2065 to 2075
years = np.arange(2065, 2076)

# Resource allocation data in arbitrary units (for illustrative purposes)
oxygen = np.array([50, 52, 54, 53, 55, 57, 56, 58, 59, 60, 61])
water = np.array([40, 42, 44, 46, 45, 47, 46, 48, 49, 50, 52])
energy = np.array([30, 32, 35, 34, 33, 35, 37, 39, 41, 43, 45])
food = np.array([20, 21, 23, 25, 26, 27, 28, 29, 30, 31, 32])
construction_materials = np.array([25, 24, 26, 28, 27, 29, 28, 27, 28, 29, 30])

# Stack the data for plotting
data = np.vstack([oxygen, water, energy, food, construction_materials])

# Create the area plot
plt.figure(figsize=(14, 8))
plt.stackplot(years, data, labels=['Oxygen', 'Water', 'Energy', 'Food', 'Construction Materials'],
              colors=['#76B041', '#4B9CD3', '#F5C342', '#FF6347', '#8A2BE2'], alpha=0.85)

# Add title and labels
plt.title('Resource Allocation in Lunaris: \nA Decade of Balance (2065-2075)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Allocation Units', fontsize=14)

# Customize the legend
plt.legend(loc='upper left', fontsize=12, title='Resources', frameon=False)

# Customize grid and background
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().set_facecolor('#f0f0f0')

# Annotate notable points
plt.text(2066, 60, 'Water Recycling\nTechnologies', fontsize=10, color='darkblue', style='italic', va='center')
plt.text(2071, 150, 'New Solar Arrays', fontsize=10, color='darkorange', style='italic', va='center')

# Rotate x-axis labels for clarity
plt.xticks(rotation=45)

# Adjust layout to make the plot more readable
plt.tight_layout()

# Show the plot
plt.show()