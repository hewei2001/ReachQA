import matplotlib.pyplot as plt
import numpy as np

# Expanded data for culinary delights at food festivals in various cities
cities = ['New York', 'Paris', 'Tokyo', 'Mexico City', 'Mumbai', 'Cape Town', 'Sydney', 'Moscow']
cuisine_dishes = {
    'Italian': [45, 35, 40, 20, 25, 30, 55, 25],
    'Japanese': [30, 20, 55, 15, 50, 25, 40, 45],
    'Mexican': [15, 10, 5, 70, 25, 20, 10, 30],
    'Indian': [20, 15, 25, 25, 55, 50, 35, 40],
    'French': [25, 50, 20, 10, 30, 35, 20, 15],
    'Chinese': [35, 45, 15, 25, 40, 30, 60, 50]
}

# Setup the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Define the position for each bar group
index = np.arange(len(cities))
bar_width = 0.35  # Reduced for more bars

# Initialize bottom stack values for stacking
bottom_stack = np.zeros(len(cities))
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#FF69B4', '#8A2BE2']

# Plot each cuisine's dishes on top of the previous ones
for (cuisine, dishes), color in zip(cuisine_dishes.items(), colors):
    ax.bar(index, dishes, bar_width, bottom=bottom_stack, label=cuisine, color=color, alpha=0.9)
    bottom_stack += dishes

# Set labels and title
ax.set_xlabel('Cities Hosting Festivals', fontsize=12, weight='bold')
ax.set_ylabel('Number of Dishes Presented', fontsize=12, weight='bold')
ax.set_title('Culinary Delights Around the World\nExploring Cuisines at Food Festivals Across Eight Major Cities', 
             fontsize=16, weight='bold', pad=20)
ax.set_xticks(index)
ax.set_xticklabels(cities, fontsize=11, weight='bold', rotation=30, ha='right')

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend to distinguish each cuisine
ax.legend(title='Cuisines', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize='11')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Create a subplot for the cumulative distribution
fig2, ax2 = plt.subplots(figsize=(14, 4))
cumulative_dishes = np.cumsum([sum(dishes) for dishes in zip(*cuisine_dishes.values())])

# Plot the cumulative number of dishes
ax2.plot(cities, cumulative_dishes, marker='o', color='#FF4500', linewidth=2.5)
ax2.set_xlabel('Cities', fontsize=12, weight='bold')
ax2.set_ylabel('Cumulative Number of Dishes', fontsize=12, weight='bold')
ax2.set_title('Cumulative Distribution of Dishes Across Cities', fontsize=14, weight='bold', pad=15)
ax2.grid(axis='both', linestyle=':', alpha=0.6)

# Adjust the layout for subplot
plt.tight_layout()

# Show both plots
plt.show()