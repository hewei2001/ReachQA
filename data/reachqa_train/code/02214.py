import matplotlib.pyplot as plt

# Material categories and their respective market share percentages
materials = [
    'Organic Cotton', 'Recycled Polyester', 'Bamboo Fiber', 'Hemp', 
    'Tencel/Lyocell', 'Cork', 'Linen', 'Eucalyptus Fiber', 
    'Soy Silk', 'Pineapple Fiber', 'Ramie', 'Recycled Nylon'
]

# Expanded data - percentage of use in sustainable fashion
percentages = [20, 15, 10, 8, 7, 5, 5, 5, 4, 3, 3, 15]

# Make sure the percentages sum up to 100
assert sum(percentages) == 100

# Colors for each sector
colors = [
    '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', 
    '#ffd92f', '#e5c494', '#b3b3b3', '#ccebc5', '#ffed6f', 
    '#bc80bd', '#ff9896'
]

# Explode setting to emphasize certain sections
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)  # Emphasize Organic Cotton and Recycled Nylon

# Create a donut chart (nested pie chart)
fig, ax = plt.subplots(figsize=(12, 8), nrows=1, ncols=2, subplot_kw=dict(aspect="equal"))

# Main Pie Chart
wedges, texts, autotexts = ax[0].pie(
    percentages,
    labels=materials,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops=dict(edgecolor='black', linewidth=1.2)
)
plt.setp(autotexts, size=9, weight="bold", color="white")
ax[0].set_title('Sustainable Fashion Material Use Breakdown\n(2023)', fontsize=14, fontweight='bold', pad=20)

# Nested Pie Chart - Grouping materials by type
group_labels = ['Natural Fibers', 'Synthetic Fibers']
group_percentages = [62, 38]  # Sum up to 100%
group_colors = ['#b3de69', '#fb8072']

ax[1].pie(
    group_percentages,
    labels=group_labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=group_colors,
    wedgeprops=dict(edgecolor='black', linewidth=1.2)
)
ax[1].set_title('Material Types\nin Eco-Friendly Clothing', fontsize=14, fontweight='bold', pad=20)

# Use tight layout to ensure everything fits well
plt.tight_layout()

# Display the plot
plt.show()