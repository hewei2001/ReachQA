import matplotlib.pyplot as plt

# E-commerce categories
categories = ['Electronics', 'Apparel', 'Home Goods', 'Beauty Products', 'Books']

# Fictional annual revenue growth data for each category
electronics_growth = [12, 14, 15, 11, 13, 16, 18, 20, 22, 21, 19]
apparel_growth = [10, 12, 14, 13, 15, 17, 16, 18, 19, 21, 23]
home_goods_growth = [8, 9, 7, 6, 8, 10, 11, 9, 12, 14, 15]
beauty_products_growth = [5, 6, 8, 7, 9, 10, 12, 11, 13, 14, 13]
books_growth = [3, 4, 5, 5, 6, 7, 8, 9, 10, 9, 11]

# Grouping the data into a list
data = [
    electronics_growth,
    apparel_growth,
    home_goods_growth,
    beauty_products_growth,
    books_growth
]

# Plot the vertical box plot
fig, ax = plt.subplots(figsize=(12, 7))

# Creating the box plots for each category
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#8D33FF']
boxprops = dict(color='black')
medianprops = dict(color='orange')

bp = ax.boxplot(data, patch_artist=True, vert=True, 
                boxprops=dict(facecolor=colors[0], color='black'), 
                whiskerprops=dict(color='black', linestyle='--'),
                capprops=dict(color='black'), 
                flierprops=dict(marker='o', color='red', alpha=0.5),
                medianprops=medianprops, notch=False)

# Customizing the box fill colors
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting x-axis and y-axis labels
ax.set_xticklabels(categories, fontsize=11, fontweight='bold', rotation=45)
ax.set_ylabel("Annual Revenue Growth (%)", fontsize=12, fontweight='bold')
ax.set_title("E-Commerce Growth Dynamics (2010-2020):\nA Category-Wise Analysis", fontsize=14, fontweight='bold', pad=20)

# Enabling grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Adding a legend for better clarity
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, categories, title='E-Commerce Categories', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()