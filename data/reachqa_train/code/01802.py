import matplotlib.pyplot as plt

# Expanded spell categories
categories = [
    'Elemental', 'Healing', 'Illusion', 'Divination', 
    'Transmutation', 'Necromancy', 'Conjuration', 'Enchantment'
]
category_sizes = [20, 15, 15, 10, 10, 10, 10, 10]

# Subcategories within each main category
subcategories = [
    ['Fire', 'Water', 'Earth', 'Air'],               # Elemental
    ['Minor Heal', 'Major Heal', 'Regeneration'],    # Healing
    ['Mirage', 'Invisibility', 'Sound'],             # Illusion
    ['Foresight', 'Detection'],                      # Divination
    ['Morph', 'Alchemy', 'Shape Change'],            # Transmutation
    ['Soul Trap', 'Resurrection', 'Curse'],          # Necromancy
    ['Summon Creature', 'Bind', 'Portal'],           # Conjuration
    ['Charm', 'Sleep', 'Confuse']                    # Enchantment
]

subcategory_sizes = [
    [5, 5, 5, 5],        # Elemental
    [7, 5, 3],           # Healing
    [6, 5, 4],           # Illusion
    [6, 4],              # Divination
    [4, 3, 3],           # Transmutation
    [4, 4, 2],           # Necromancy
    [4, 3, 3],           # Conjuration
    [4, 3, 3]            # Enchantment
]

# Colors for categories
category_colors = ['#FF7F50', '#4682B4', '#FFD700', '#8A2BE2', '#5F9EA0', '#8B0000', '#FF1493', '#32CD32']

# Nested colors for subcategories
subcategory_colors = [
    ['#FFA07A', '#B0E0E6', '#FFFACD', '#E0FFFF'],
    ['#87CEFA', '#B0C4DE', '#7FFFD4'],
    ['#D8BFD8', '#DDA0DD', '#DA70D6'],
    ['#EE82EE', '#DDA0DD'],
    ['#AFEEEE', '#B0E0E6', '#98FB98'],
    ['#C71585', '#800080', '#8B008B'],
    ['#FF4500', '#FF6347', '#FFD700'],
    ['#3CB371', '#32CD32', '#98FB98']
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 12))

# Plot main donut pie chart
wedges, texts, autotexts = ax.pie(
    category_sizes, labels=categories, colors=category_colors, startangle=90, pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'), autopct='%1.1f%%', textprops={'fontsize': 10, 'color': 'black'}
)

# Plot the inner ring for subcategories
subcat_startangle = 90
for i, subcat_size in enumerate(subcategory_sizes):
    ax.pie(
        subcat_size, colors=subcategory_colors[i], startangle=subcat_startangle,
        radius=0.7, wedgeprops=dict(width=0.3, edgecolor='w')
    )
    subcat_startangle += 360 * (category_sizes[i] / 100)

# Title and central label
ax.set_title("IAAM: Detailed Spell Category Distribution\nComprising Eight Arcane Schools", fontsize=14, fontweight='bold', pad=20)
ax.text(0, 0, 'Spell Types', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black', fontweight='bold')

# Ensure the pie is drawn as a circle
ax.axis('equal')

# Add legend with category labels
ax.legend(wedges, categories, title='Spell Categories', loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Ensure layout is tidy
plt.tight_layout()

# Display the plot
plt.show()