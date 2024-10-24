import matplotlib.pyplot as plt
import numpy as np

# Data
coffee_shops = ['Java House', 'Brewed Awakening', 'The Grind', 'Caffeine Dreams', 
                'Espresso Express', 'The Daily Grind', 'Perk Up Cafe', 
                'Mocha Mornings', 'Latte Lounge', 'Bitter Sweet']

visit_times = np.array([45, 30, 50, 40, 35, 55, 25, 60, 20, 33])
ratings = np.array([7.8, 6.5, 8.5, 7.0, 7.2, 8.8, 5.8, 9.0, 6.0, 7.1])

# Colors for each coffee shop
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
          '#ffb3e6', '#c2f0c2', '#f0e68c', '#d3d3d3', '#ff6666']

# Create scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(visit_times, ratings, s=150, c=colors, alpha=0.8, edgecolors='black')

# Title and labels
plt.title('Correlation Between Coffee Shop Ratings\nand Average Customer Visit Time', fontsize=14)
plt.xlabel('Average Customer Visit Time (minutes)', fontsize=12)
plt.ylabel('Customer Ratings (out of 10)', fontsize=12)

# Annotating each point
for i, shop in enumerate(coffee_shops):
    plt.annotate(shop, (visit_times[i] + 0.5, ratings[i] + 0.1), fontsize=9)

# Custom legend handles
handles = [plt.Line2D([0], [0], marker='o', color='w', label=shop,
                      markersize=10, markerfacecolor=c) for shop, c in zip(coffee_shops, colors)]
plt.legend(title='Coffee Shops', handles=handles, bbox_to_anchor=(1.05, 1), loc='upper left')

# Add grid for readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent text from being cut off
plt.tight_layout()

# Show plot
plt.show()