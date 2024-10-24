import matplotlib.pyplot as plt

# Material categories and their respective market share percentages
materials = [
    'Organic Cotton',
    'Recycled Polyester',
    'Bamboo Fiber',
    'Hemp',
    'Tencel/Lyocell',
    'Cork',
    'Other Materials'
]

# Percentage of use in sustainable fashion
percentages = [30, 25, 15, 10, 10, 5, 5]

# Colors for each sector
colors = [
    '#66c2a5',  # Organic Cotton - Green
    '#fc8d62',  # Recycled Polyester - Orange
    '#8da0cb',  # Bamboo Fiber - Purple
    '#e78ac3',  # Hemp - Pink
    '#a6d854',  # Tencel/Lyocell - Lime
    '#ffd92f',  # Cork - Yellow
    '#e5c494'   # Other Materials - Beige
]

# Explode setting to emphasize certain sections
explode = (0.1, 0, 0, 0, 0, 0, 0)  # Emphasize Organic Cotton

# Creating the pie chart
plt.figure(figsize=(10, 7))
plt.pie(
    percentages,
    labels=materials,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops=dict(edgecolor='black', linewidth=1.5)
)

# Title and styling
plt.title('The Sustainable Fashion Revolution:\nMaterial Sources in Eco-Friendly Clothing (2023)', 
          fontsize=14, fontweight='bold', pad=20)

# Use tight layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()