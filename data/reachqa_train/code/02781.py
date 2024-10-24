import matplotlib.pyplot as plt

# Define planets and their respective culinary preference breakdown
planets = ['Valoria', 'Zynthara', 'Eldoria', 'Quoran', 'Luminara', 'Frondor']
cuisine_types = ['Spicy', 'Sweet', 'Sour', 'Bitter', 'Savory']

# Data: each sublist corresponds to the culinary distribution for a planet
data = [
    [25, 15, 20, 10, 30],  # Valoria
    [15, 35, 25, 10, 15],  # Zynthara
    [20, 20, 25, 25, 10],  # Eldoria
    [30, 10, 15, 20, 25],  # Quoran
    [10, 30, 20, 30, 10],  # Luminara
    [20, 25, 15, 15, 25]   # Frondor
]

# Colors for each type of cuisine
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#8A2BE2', '#FF4500']

# Create subplots for each planet
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Intergalactic Cuisine Preferences:\nCulinary Trends Across Different Planets',
             fontsize=16, fontweight='bold', color='darkblue', y=1.05)

for i, ax in enumerate(axes.flat):
    if i < len(planets):
        wedges, texts, autotexts = ax.pie(
            data[i], labels=cuisine_types, autopct='%1.1f%%', startangle=90,
            colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'),
            textprops={'fontsize': 10}, pctdistance=0.85
        )
        # Enhance label colors
        for autotext in autotexts:
            autotext.set_color('black')
        ax.set_title(planets[i], fontsize=13, fontweight='bold', pad=20)
    else:
        ax.axis('off')  # Hide any extra subplot space

# Add a legend for cuisine types
fig.legend(cuisine_types, loc='center right', fontsize=11, title='Cuisine Types', bbox_to_anchor=(1.15, 0.5))

# Adjust layout to avoid overlap and optimize visibility
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Show the plot
plt.show()