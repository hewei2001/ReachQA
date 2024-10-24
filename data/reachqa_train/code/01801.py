import matplotlib.pyplot as plt

# Main spell categories
categories = ['Elemental', 'Healing', 'Illusion', 'Divination', 'Transmutation']
# Corresponding size (percentage) of the main spell categories
category_sizes = [30, 20, 25, 15, 10]

# Subcategories within each main category, reflecting sub-spell types
subcategories = [
    ['Fire', 'Water', 'Earth', 'Air'],        # Elemental
    ['Minor Heal', 'Major Heal'],             # Healing
    ['Mirage', 'Invisibility', 'Sound'],      # Illusion
    ['Foresight', 'Detection'],               # Divination
    ['Morph', 'Alchemy']                      # Transmutation
]

# Corresponding size (percentage) of subcategories
subcategory_sizes = [
    [10, 8, 7, 5],  # Elemental
    [12, 8],        # Healing
    [10, 9, 6],     # Illusion
    [9, 6],         # Divination
    [6, 4]          # Transmutation
]

# Colors for categories
category_colors = ['#FF7F50', '#4682B4', '#FFD700', '#8A2BE2', '#5F9EA0']

# Nested colors for subcategories
subcategory_colors = [
    ['#FFA07A', '#B0E0E6', '#FFFACD', '#E0FFFF'],  # Elemental
    ['#87CEFA', '#B0C4DE'],                        # Healing
    ['#D8BFD8', '#DDA0DD', '#DDA0DD'],             # Illusion
    ['#EE82EE', '#DDA0DD'],                        # Divination
    ['#AFEEEE', '#B0E0E6']                         # Transmutation
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the main donut pie chart for spell categories
wedges, texts, autotexts = ax.pie(
    category_sizes, labels=categories, colors=category_colors, startangle=90, pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'), autopct='%1.1f%%', textprops={'fontsize': 10, 'color': 'black'}
)

# Plot the inner ring for subcategories
subcat_startangle = 90  # Initial start angle for subcategories
for i, subcat_size in enumerate(subcategory_sizes):
    ax.pie(
        subcat_size, colors=subcategory_colors[i], startangle=subcat_startangle,
        radius=0.7, wedgeprops=dict(width=0.3, edgecolor='w')
    )
    subcat_startangle += 360 * (category_sizes[i] / 100)  # Adjust start angle for next category

# Title and central label
ax.set_title("IAAM: Spell Category Distribution", fontsize=16, fontweight='bold', pad=20)
ax.text(0, 0, 'Spell Types', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black', fontweight='bold')

# Ensure the pie is drawn as a circle
ax.axis('equal')

# Add legend with category labels
ax.legend(wedges, categories, title='Spell Categories', loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure layout is tidy
plt.tight_layout()

# Display the plot
plt.show()