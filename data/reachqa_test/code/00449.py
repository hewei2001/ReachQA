import matplotlib.pyplot as plt
import numpy as np

# Expanded dataset for continents and sub-regions
regions = [
    'North America', 'South America', 'Western Europe', 'Eastern Europe', 
    'East Asia', 'South Asia', 'North Africa', 'Sub-Saharan Africa'
]
coffee_consumption_data = [
    [42, 44, 40, 41, 46, 51, 37, 40, 43, 42, 48, 46, 45, 47, 50, 52, 51, 53, 48, 49, 44, 45, 47, 44, 43],  # North America
    [31, 36, 34, 32, 35, 30, 36, 38, 37, 33, 31, 35, 32, 33, 31, 30, 34, 35, 36, 32, 38, 37, 33, 31, 30],  # South America
    [46, 48, 51, 49, 50, 52, 47, 53, 49, 51, 50, 55, 56, 57, 52, 54, 50, 53, 52, 48, 51, 53, 55, 51, 50],  # Western Europe
    [43, 45, 49, 47, 46, 48, 44, 50, 46, 48, 50, 47, 49, 46, 45, 44, 47, 48, 49, 50, 46, 44, 45, 47, 49],  # Eastern Europe
    [21, 23, 19, 22, 25, 20, 23, 24, 26, 21, 20, 22, 19, 24, 25, 20, 21, 23, 22, 26, 25, 24, 20, 21, 22],  # East Asia
    [18, 22, 20, 19, 21, 18, 20, 19, 21, 23, 19, 20, 22, 21, 20, 19, 20, 23, 18, 19, 21, 22, 20, 21, 19],  # South Asia
    [16, 19, 15, 17, 18, 16, 17, 16, 19, 18, 15, 14, 16, 17, 19, 18, 17, 19, 18, 16, 17, 15, 14, 18, 16],  # North Africa
    [14, 17, 13, 15, 16, 14, 15, 14, 17, 16, 12, 14, 15, 13, 15, 16, 14, 17, 13, 12, 15, 14, 16, 13, 17]   # Sub-Saharan Africa
]

# Create the figure with multiple subplots
fig, ax = plt.subplots(figsize=(15, 10))

# Boxplot properties
boxprops = dict(linestyle='-', linewidth=1.5, color='black')
whiskerprops = dict(linestyle='--', linewidth=1, color='gray')
capprops = dict(linestyle='-', linewidth=1, color='black')
medianprops = dict(linestyle='-', linewidth=2, color='firebrick')

# Create vertical boxplot with notches
bp = ax.boxplot(coffee_consumption_data, vert=True, patch_artist=True, labels=regions,
                boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops, 
                medianprops=medianprops, notch=True)

# Assign colors to each box for visual distinction
colors = ['#8B4513', '#DEB887', '#D2B48C', '#A0522D', '#F4A460', '#8B0000', '#FFD700', '#DAA520']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

# Add mean points
means = [np.mean(data) for data in coffee_consumption_data]
ax.plot(np.arange(1, len(regions) + 1), means, 'o', color='blue', label='Mean')

# Set title and labels
ax.set_title('Global Coffee Consumption Trends in 2023 by Region\n(A Detailed Statistical Analysis)', fontsize=16, fontweight='bold', color='brown')
ax.set_ylabel('Cups per Person per Month', fontsize=12, color='black')
ax.set_xlabel('Regions', fontsize=12, color='black')

# Customize the grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='upper right', fontsize=10)

# Adjust the layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()