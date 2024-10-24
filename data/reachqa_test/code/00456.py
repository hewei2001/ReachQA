import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data for the fruits
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Cherries', 'Pineapples', 'Kiwis', 'Peaches', 'Strawberries']
sizes = {
    'Apples': [7, 8, 6, 7.5, 8.2, 7.3, 7.8, 8.1, 7.9, 7.2],
    'Oranges': [8, 9, 7.5, 8.5, 9, 8.7, 9.1, 8.3, 9.5, 8.2],
    'Bananas': [15, 16, 14.5, 15.5, 16.5, 15.7, 16.2, 15.3, 15.9, 16.1],
    'Grapes': [2, 2.5, 2.2, 2.3, 2.4, 2.6, 2.1, 2.8, 2.7, 2.9],
    'Cherries': [2.5, 2.8, 2.7, 2.6, 2.9, 3.0, 2.4, 2.2, 2.1, 2.3],
    'Pineapples': [12, 13, 11.5, 12.5, 13.5, 12.8, 13.3, 12.1, 12.6, 13.1],
    'Kiwis': [5, 5.5, 4.5, 5.2, 5.8, 5.1, 5.6, 5.9, 5.3, 5.4],
    'Peaches': [8, 8.5, 7.5, 8.7, 9, 8.2, 8.4, 8.1, 8.9, 8.6],
    'Strawberries': [1.5, 1.7, 1.6, 1.8, 1.9, 1.4, 1.3, 1.5, 1.6, 1.8]
}

sweetness_levels = {
    'Apples': [7, 6, 8, 7, 8, 7.5, 7.8, 8.1, 7.4, 7.9],
    'Oranges': [8, 9, 7, 8, 9, 8.9, 9.2, 8.5, 9.1, 8.6],
    'Bananas': [9, 8, 9, 10, 9, 9.2, 8.7, 9.1, 9.4, 9.5],
    'Grapes': [6, 5, 6, 5, 6, 5.5, 5.3, 5.7, 5.6, 5.2],
    'Cherries': [9, 10, 9, 10, 10, 9.5, 10, 9.2, 9.4, 9.8],
    'Pineapples': [7, 8, 9, 8, 7.5, 8.3, 8.7, 7.8, 8.5, 8.1],
    'Kiwis': [8, 8.5, 7.5, 8, 8.2, 8.4, 8.1, 8.3, 8.6, 8.7],
    'Peaches': [9, 9.2, 9.5, 9.3, 9.1, 9.4, 9.7, 9.8, 9.6, 9.9],
    'Strawberries': [7, 7.5, 7.2, 7.3, 7.1, 7.8, 7.6, 7.4, 7.7, 7.9]
}

# Price data for bubble sizes
price_data = {
    'Apples': [2, 2.5, 2.2, 2.3, 2.8, 2.6, 2.5, 2.4, 2.7, 2.9],
    'Oranges': [2.5, 3, 2.8, 3.2, 3.1, 3.4, 3.3, 3.0, 3.2, 3.5],
    'Bananas': [1.5, 1.8, 1.6, 2.0, 1.9, 2.1, 2.2, 2.3, 2.4, 2.5],
    'Grapes': [4, 4.5, 4.2, 4.0, 4.3, 4.4, 4.1, 4.6, 4.5, 4.3],
    'Cherries': [3, 3.5, 3.2, 3.0, 3.8, 3.7, 3.9, 3.4, 3.6, 3.1],
    'Pineapples': [3.5, 4, 4.2, 4.1, 4.0, 4.3, 4.4, 4.2, 4.5, 4.6],
    'Kiwis': [2, 2.2, 2.1, 2.0, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8],
    'Peaches': [3, 3.3, 3.1, 3.2, 3.5, 3.4, 3.7, 3.6, 3.8, 3.9],
    'Strawberries': [5, 5.5, 5.2, 5.3, 5.1, 5.4, 5.6, 5.8, 5.7, 5.9]
}

# Color mapping corresponding to fruits
fruit_colors = {
    'Apples': 'red',
    'Oranges': 'orange',
    'Bananas': 'yellow',
    'Grapes': 'purple',
    'Cherries': 'darkred',
    'Pineapples': 'gold',
    'Kiwis': 'green',
    'Peaches': 'peachpuff',
    'Strawberries': 'crimson'
}

plt.figure(figsize=(14, 10))

for fruit in fruits:
    plt.scatter(sizes[fruit], sweetness_levels[fruit], 
                label=fruit, 
                s=np.array(price_data[fruit]) * 80,  # Bubble sizes based on price, reduced to avoid overlap
                alpha=0.8, 
                color=fruit_colors[fruit],
                edgecolor='black')

    # Linear regression for each fruit
    X = np.array(sizes[fruit]).reshape(-1, 1)
    y = np.array(sweetness_levels[fruit])
    model = LinearRegression().fit(X, y)
    x_range = np.linspace(min(X), max(X), 100)
    y_fit = model.predict(x_range.reshape(-1, 1))
    plt.plot(x_range, y_fit, linestyle='--', color=fruit_colors[fruit], linewidth=1)

# Customizing the plot
plt.title("Fruit Size vs. Sweetness Levels\nWith Bubble Sizes Representing Market Price", 
          fontsize=16, weight='bold', pad=20)
plt.xlabel("Size (cm)", fontsize=14)
plt.ylabel("Sweetness Level (1-10)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Fruits', fontsize=10, title_fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()