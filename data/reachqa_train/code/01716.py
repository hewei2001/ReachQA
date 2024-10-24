import matplotlib.pyplot as plt

# Data: Return rates (in percentage) for each product category
return_rates = {
    'Electronics': [12, 15, 13, 17, 20],
    'Clothing': [22, 25, 30, 27, 29],
    'Home & Kitchen': [5, 7, 6, 8, 10],
    'Beauty & Health': [18, 15, 17, 19, 21],
    'Sports & Outdoors': [10, 12, 14, 11, 13],
    'Books': [3, 2, 4, 1, 5]
}

# List of categories and their corresponding data
categories = list(return_rates.keys())
data = list(return_rates.values())

# Creating the horizontal box plot
fig, ax = plt.subplots(figsize=(10, 7))
box = ax.boxplot(data, vert=False, patch_artist=True,
                 boxprops=dict(facecolor='lightblue', color='blue'),
                 whiskerprops=dict(color='blue'),
                 capprops=dict(color='blue'),
                 medianprops=dict(color='red'),
                 flierprops=dict(marker='o', color='orange', markersize=7, alpha=0.5),
                 notch=True)  # Adding notches for additional insight

# Color each box with a distinct color
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink', 'lightgrey']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding labels and title
ax.set_yticklabels(categories, fontsize=11)
ax.set_xlabel('Return Rate (%)', fontsize=12)
ax.set_title('Product Return Rates by Category\nE-commerce Analysis (Jan-Jun 2023)', fontsize=14, fontweight='bold', pad=15)

# Customizing grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()