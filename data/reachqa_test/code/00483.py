import matplotlib.pyplot as plt
import numpy as np

# Cuisines and ingredients
cuisines = ['Italian', 'Indian', 'Mexican', 'Chinese']
ingredients = ['Tomato', 'Cilantro', 'Cumin', 'Ginger', 'Garlic']

# Constructing popularity data (arbitrary scores from 0 to 100)
popularity_data = np.array([
    [90, 20, 10, 30, 50],  # Italian
    [30, 90, 70, 40, 80],  # Indian
    [60, 50, 40, 20, 30],  # Mexican
    [20, 30, 30, 80, 60]   # Chinese
])

# Constructing recipe data (sums of popularity scores per ingredient)
recipe_data = np.array([sum(popularity_data[:, i]) for i in range(popularity_data.shape[1])])

# Creating the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# Heatmap
heatmap = ax1.imshow(popularity_data, aspect='auto', cmap='YlOrRd')
cbar = plt.colorbar(heatmap, ax=ax1)
cbar.set_label('Popularity Score (0-100)', rotation=270, labelpad=15)

ax1.set_xticks(np.arange(len(ingredients)))
ax1.set_yticks(np.arange(len(cuisines)))
ax1.set_xticklabels(ingredients)
ax1.set_yticklabels(cuisines)
ax1.set_title('Popularity of Culinary Ingredients\nin Global Cuisines', fontsize=16, fontweight='bold')
ax1.set_xlabel('Ingredients', fontsize=12)
ax1.set_ylabel('Cuisines', fontsize=12)

for (i, j), value in np.ndenumerate(popularity_data):
    ax1.text(j, i, f'{value}', ha='center', va='center', color='black', fontsize=10)

# Bar plot
ax2.bar(ingredients, recipe_data, color='lightblue')
ax2.set_title('Total Number of Recipes\nUsing Each Ingredient', fontsize=16, fontweight='bold')
ax2.set_xlabel('Ingredients', fontsize=12)
ax2.set_ylabel('Number of Recipes', fontsize=12)

# Adding value annotations on the bars
for i, value in enumerate(recipe_data):
    ax2.text(i, value + 1, f'{value}', ha='center', va='bottom', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()