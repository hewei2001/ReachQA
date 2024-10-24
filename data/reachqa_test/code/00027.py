import matplotlib.pyplot as plt
import numpy as np

# Data: Sizes of green spaces (in acres) across different districts
districts = ['Downtown', 'Uptown', 'Eastside', 'Westend', 'Suburbia']
green_spaces = [
    [3, 5, 7, 6, 10, 9, 12],    # Downtown
    [10, 12, 15, 14, 13, 17, 16], # Uptown
    [20, 21, 22, 19, 18, 24, 25], # Eastside
    [8, 7, 9, 10, 12, 15, 14],    # Westend
    [30, 28, 32, 31, 34, 33, 29]  # Suburbia
]

# Related dataset: Average annual increase of green spaces in percentage
annual_growth = [5, 3, 4, 2, 6]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# Plot 1: Horizontal Boxplot
boxes = ax1.boxplot(green_spaces, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='#98FB98', color='#3CB371'),
                   capprops=dict(color='#2E8B57'),
                   whiskerprops=dict(color='#2E8B57'),
                   flierprops=dict(markerfacecolor='#FFA07A', marker='o', markersize=5, linestyle='none', markeredgecolor='#CD5C5C'),
                   medianprops=dict(color='#FF4500'))

# Add colors to the boxes
colors = ['#98FB98', '#90EE90', '#8FBC8F', '#32CD32', '#228B22']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Title and labels for the first plot
ax1.set_title('Distribution of Green Spaces Across Districts\nin Greenopolis', fontsize=13, loc='center')
ax1.set_xlabel('Size of Green Space (Acres)', fontsize=11)
ax1.set_yticklabels(districts, fontsize=9)
ax1.grid(True, linestyle='--', alpha=0.6, which='both')

# Plot 2: Bar chart for average annual growth
ax2.barh(districts, annual_growth, color='#4682B4', edgecolor='black')
ax2.set_title('Average Annual Growth Rate\nof Green Spaces (%)', fontsize=13, loc='center')
ax2.set_xlabel('Growth Rate (%)', fontsize=11)
ax2.set_yticklabels([])  # Hide y-labels as they are shared
ax2.invert_yaxis()  # Invert y-axis to match order with boxplot
for index, value in enumerate(annual_growth):
    ax2.text(value + 0.1, index, f'{value}%', va='center', ha='left', fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()