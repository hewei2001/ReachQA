import matplotlib.pyplot as plt
import numpy as np

# E-commerce categories
categories = ['Electronics', 'Apparel', 'Home Goods', 'Beauty Products', 'Books']

# Fictional annual revenue growth data for each category (2010-2020)
electronics_growth = [12, 14, 15, 11, 13, 16, 18, 20, 22, 21, 19]
apparel_growth = [10, 12, 14, 13, 15, 17, 16, 18, 19, 21, 23]
home_goods_growth = [8, 9, 7, 6, 8, 10, 11, 9, 12, 14, 15]
beauty_products_growth = [5, 6, 8, 7, 9, 10, 12, 11, 13, 14, 13]
books_growth = [3, 4, 5, 5, 6, 7, 8, 9, 10, 9, 11]

# Calculating average growth per year across all categories for the line plot
average_growth = np.mean([electronics_growth, apparel_growth, home_goods_growth, beauty_products_growth, books_growth], axis=0)
years = list(range(2010, 2021))

# Plotting the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Box plot for each category
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#8D33FF']
medianprops = dict(color='orange')

bp = ax1.boxplot([electronics_growth, apparel_growth, home_goods_growth, beauty_products_growth, books_growth],
                 patch_artist=True, vert=True,
                 whiskerprops=dict(color='black', linestyle='--'),
                 capprops=dict(color='black'),
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 medianprops=medianprops, notch=False)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_xticklabels(categories, fontsize=11, fontweight='bold', rotation=45)
ax1.set_ylabel("Annual Revenue Growth (%)", fontsize=12, fontweight='bold')
ax1.set_title("E-Commerce Growth Dynamics (2010-2020):\nCategory-Wise Analysis", fontsize=14, fontweight='bold', pad=20)
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)

handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax1.legend(handles, categories, title='E-Commerce Categories', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Line plot for average growth over years
ax2.plot(years, average_growth, marker='o', linestyle='-', color='blue', label='Average Growth')
ax2.set_title("Average Annual Revenue Growth (2010-2020)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12, fontweight='bold')
ax2.set_ylabel("Average Growth (%)", fontsize=12, fontweight='bold')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()