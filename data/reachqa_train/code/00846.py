import matplotlib.pyplot as plt
import numpy as np

# Data for culinary delights at food festivals in various cities
cities = ['New York', 'Paris', 'Tokyo', 'Mexico City', 'Mumbai']
cuisine_dishes = {
    'Italian': [45, 35, 40, 20, 25],
    'Japanese': [30, 20, 55, 15, 50],
    'Mexican': [15, 10, 5, 70, 25],
    'Indian': [20, 15, 25, 25, 55],
    'French': [25, 50, 20, 10, 30]
}

# Setup the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define the position for each bar group
index = np.arange(len(cities))
bar_width = 0.5

# Initialize bottom stack values for stacking
bottom_stack = np.zeros(len(cities))
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#FF69B4']

# Plot each cuisine's dishes on top of the previous ones
for (cuisine, dishes), color in zip(cuisine_dishes.items(), colors):
    ax.bar(index, dishes, bar_width, bottom=bottom_stack, label=cuisine, color=color, alpha=0.8)
    bottom_stack += dishes

# Set labels and title
ax.set_xlabel('Cities Hosting Festivals', fontsize=12, weight='bold')
ax.set_ylabel('Number of Dishes Presented', fontsize=12, weight='bold')
ax.set_title('Culinary Delights Around the World\nCuisines at Food Festivals', fontsize=16, weight='bold', pad=20)
ax.set_xticks(index)
ax.set_xticklabels(cities, fontsize=11, weight='bold', rotation=15)

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend to distinguish each cuisine
ax.legend(title='Cuisines', loc='upper right', bbox_to_anchor=(1.15, 1), fontsize=10, title_fontsize='11')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()