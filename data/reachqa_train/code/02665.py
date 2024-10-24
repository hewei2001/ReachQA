import matplotlib.pyplot as plt
import numpy as np

# E-commerce platforms
marketplaces = ['ShopNow', 'MegaMart', 'QuickCart', 'EasyShop', 'BuyFast']

# Delivery times (in days) for each platform
delivery_times = [
    [2, 3, 5, 2, 3, 4, 5, 2, 3, 6, 2, 3, 4],      # ShopNow
    [4, 3, 5, 6, 4, 7, 3, 6, 4, 5, 7, 6, 8, 20],  # MegaMart (includes outlier)
    [1, 2, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2],         # QuickCart
    [3, 5, 4, 6, 5, 3, 4, 5, 6, 4, 5, 7, 3, 4],   # EasyShop
    [6, 8, 7, 9, 8, 10, 7, 6, 7, 11, 12, 10]      # BuyFast
]

# Calculate average delivery times for the line plot
average_delivery_times = [np.mean(times) for times in delivery_times]

# Colors for each box
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
bplot = ax.boxplot(delivery_times, vert=False, patch_artist=True, 
                   notch=True,
                   boxprops=dict(facecolor='skyblue', color='darkblue'),
                   whiskerprops=dict(color='darkblue'),
                   capprops=dict(color='darkblue'),
                   medianprops=dict(color='orange', linewidth=2),
                   flierprops=dict(marker='o', color='red', markersize=7))

# Customize each box with different colors
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Overlay a line plot for average delivery times
ax.plot(average_delivery_times, range(1, len(marketplaces) + 1), 
        linestyle='-', marker='o', color='black', linewidth=1.5, markersize=8, 
        label='Average Delivery Time')

# Gridlines for clarity
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Set the labels and title
ax.set_yticklabels(marketplaces, fontsize=10)
ax.set_title('Distribution of Delivery Times\nfor E-commerce Orders Across Marketplaces', 
             fontsize=16, fontweight='bold')
ax.set_xlabel('Delivery Time (Days)', fontsize=12)

# Add a legend
handles = [plt.Line2D([0], [0], color=c, lw=4) for c in colors] + [plt.Line2D([0], [0], color='black', lw=2, marker='o')]
legend_labels = ['ShopNow', 'MegaMart', 'QuickCart', 'EasyShop', 'BuyFast', 'Average Delivery Time']
ax.legend(handles, legend_labels, loc='upper right', title='E-commerce Platforms', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()