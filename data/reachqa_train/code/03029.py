import matplotlib.pyplot as plt
import numpy as np

# Define the decades and fruit consumption data in millions
decades = np.array([1980, 1990, 2000, 2010, 2020])
apples = np.array([30, 28, 35, 40, 45])
bananas = np.array([25, 30, 28, 26, 30])
cherries = np.array([10, 15, 20, 25, 30])
dates = np.array([5, 8, 10, 12, 15])
elderberries = np.array([3, 5, 7, 10, 12])

# Generate the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(decades, apples, bananas, cherries, dates, elderberries,
             labels=['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries'],
             colors=['#ff9999', '#ffcc66', '#66c2a5', '#8da0cb', '#e78ac3'],
             alpha=0.8)

# Title and labels
ax.set_title('Fruitopolis: A Five-Decade Journey\nThrough Fruity Delights', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Fruit Consumption (Millions)', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper left', title='Fruits', fontsize=10)

# Format the x-axis to display decades nicely
ax.set_xticks(decades)
ax.set_xticklabels([f"{decade}s" for decade in decades], fontsize=10)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Ensure labels are not cut off and fit the figure nicely
plt.tight_layout()

# Display the plot
plt.show()