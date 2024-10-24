import matplotlib.pyplot as plt
import numpy as np

# Extended list of coffee types
coffee_types = [
    'Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha', 'Flat White', 
    'Cortado', 'Macchiato', 'Ristretto', 'Affogato'
]

# Expanded artificial consumption data over 24 months for each coffee type
consumption_data = [
    [30, 28, 35, 32, 40, 38, 34, 33, 42, 36, 41, 39, 37, 38, 42, 43, 35, 40, 38, 36, 45, 44, 37, 41],  # Espresso
    [22, 25, 23, 27, 29, 24, 26, 28, 21, 23, 25, 30, 22, 24, 27, 26, 29, 28, 21, 23, 30, 25, 26, 29],  # Latte
    [18, 19, 17, 20, 16, 22, 18, 20, 19, 21, 17, 20, 21, 19, 18, 22, 23, 17, 21, 20, 19, 18, 22, 21],  # Cappuccino
    [25, 27, 30, 28, 32, 26, 29, 31, 33, 27, 32, 30, 28, 29, 34, 33, 31, 30, 28, 34, 32, 31, 33, 29],  # Americano
    [15, 17, 14, 16, 18, 13, 19, 20, 12, 15, 14, 17, 18, 16, 13, 17, 14, 19, 15, 18, 20, 14, 16, 15],  # Mocha
    [10, 12, 11, 13, 14, 9, 10, 15, 13, 12, 14, 11, 13, 12, 11, 9, 13, 15, 10, 12, 11, 13, 14, 12],   # Flat White
    [5, 6, 7, 6, 8, 9, 5, 7, 9, 6, 8, 7, 6, 9, 5, 7, 8, 6, 5, 9, 8, 7, 6, 9],                         # Cortado
    [7, 9, 8, 10, 11, 9, 8, 9, 10, 7, 9, 10, 8, 11, 7, 9, 10, 8, 11, 7, 8, 9, 10, 11],                # Macchiato
    [4, 5, 6, 5, 7, 8, 6, 4, 6, 7, 5, 8, 4, 5, 6, 7, 8, 5, 6, 7, 8, 4, 5, 6],                         # Ristretto
    [3, 4, 4, 5, 6, 3, 4, 4, 5, 3, 5, 4, 3, 6, 5, 4, 3, 6, 5, 4, 5, 3, 4, 5]                          # Affogato
]

# Create a larger and more detailed box plot
plt.figure(figsize=(14, 10))
box = plt.boxplot(consumption_data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Customizing colors for each coffee type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffdab9', '#a9a9a9', '#ffdead', '#dda0dd']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add mean points and lines
means = [np.mean(data) for data in consumption_data]
for i, mean in enumerate(means):
    plt.scatter(mean, i+1, color='black', marker='o', label='Mean' if i == 0 else "")

# Improve readability
plt.title('Detailed Global Coffee Consumption Analysis\n(Cups Per Month Over 24 Months, 2023)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Cups per Month', fontsize=12)
plt.yticks(ticks=np.arange(1, len(coffee_types) + 1), labels=coffee_types, fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adding a legend for the mean points
plt.legend(loc='upper right', fontsize=10)

# Applying tight layout for optimal text display
plt.tight_layout()

# Display the plot
plt.show()