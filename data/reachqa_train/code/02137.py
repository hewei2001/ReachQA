import matplotlib.pyplot as plt
import numpy as np

# Define coffee types
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha', 'Flat White']

# Artificial consumption data for each coffee type (cups per month)
consumption_data = [
    [30, 28, 35, 32, 40, 38, 34, 33, 42, 36],  # Espresso
    [22, 25, 23, 27, 29, 24, 26, 28, 21, 23],  # Latte
    [18, 19, 17, 20, 16, 22, 18, 20, 19, 21],  # Cappuccino
    [25, 27, 30, 28, 32, 26, 29, 31, 33, 27],  # Americano
    [15, 17, 14, 16, 18, 13, 19, 20, 12, 15],  # Mocha
    [10, 12, 11, 13, 14, 9, 10, 15, 13, 12]    # Flat White
]

# Create the horizontal box plot
plt.figure(figsize=(12, 8))
box = plt.boxplot(consumption_data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Customizing the plot with colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Enhancing the plot's readability
plt.title('Global Coffee Consumption Variability by Type\n(Cups Per Month, 2023)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Cups per Month', fontsize=12)
plt.yticks(ticks=np.arange(1, len(coffee_types) + 1), labels=coffee_types)

# Adding a grid to improve readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Applying tight layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()