import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Revised sales data
electronics_sales = [120, 150, 160, 170, 155, 145, 140, 165, 185, 200, 
                     210, 190, 175, 180, 220, 240, 230, 225, 210, 205, 
                     195, 190, 185, 180, 175, 170, 160, 155, 150, 145]

fashion_sales = [60, 65, 70, 75, 80, 85, 78, 72, 68, 64, 
                 62, 58, 55, 52, 49, 51, 54, 56, 59, 61, 
                 65, 70, 75, 78, 82, 86, 89, 85, 80, 77]

home_garden_sales = [90, 95, 100, 105, 102, 98, 96, 94, 93, 97, 
                     101, 110, 115, 112, 109, 107, 105, 103, 100, 98, 
                     95, 92, 89, 86, 88, 91, 94, 98, 102, 106]

books_sales = [40, 42, 45, 47, 50, 53, 55, 54, 52, 51, 
               49, 48, 46, 45, 47, 50, 52, 55, 58, 60, 
               62, 63, 61, 59, 56, 53, 50, 48, 45, 43]

# Additional statistical computations
sales_data = [electronics_sales, fashion_sales, home_garden_sales, books_sales]
means = [np.mean(category) for category in sales_data]

# Creating 3D plot data
months = np.arange(1, 31)
category_labels = ['Electronics', 'Fashion', 'Home & Garden', 'Books']
color_map = ['skyblue', 'pink', 'lightgreen', 'wheat']

# Figure setup
fig = plt.figure(figsize=(16, 8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d', azim=-110, elev=20)

# Box plot customization
boxprops = dict(facecolor='none', edgecolor='darkblue', linewidth=2)
medianprops = dict(color='firebrick', linewidth=2)
ax1.boxplot(sales_data, patch_artist=True, notch=True,
            boxprops=boxprops, medianprops=medianprops)
ax1.set_title("Monthly Sales Distribution Across Categories", fontsize=14, fontweight='bold')
ax1.set_ylabel("Sales (in thousands of $)")
ax1.set_xticklabels(category_labels)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotating mean values
for i, mean in enumerate(means):
    ax1.annotate(f'Mean: {mean:.1f}k', xy=(i+1, mean), xytext=(i+1.5, mean+10),
                 arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, ha='center')

# 3D bar plot
for i, (sales, color, label) in enumerate(zip(sales_data, color_map, category_labels)):
    ax2.bar(months, sales, zs=i, zdir='y', color=color, alpha=0.8, width=0.7, label=label)

ax2.set_xlabel('Days')
ax2.set_ylabel('Category')
ax2.set_zlabel('Sales (in thousands of $)')
ax2.set_yticks(range(len(category_labels)))
ax2.set_yticklabels(category_labels)
ax2.set_title("3D Sales Visualization Over Time", fontsize=14, fontweight='bold')

# Legend for the 3D plot
ax2.legend(loc='upper left', fontsize=9)

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()