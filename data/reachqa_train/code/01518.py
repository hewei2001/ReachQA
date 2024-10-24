import matplotlib.pyplot as plt

# Define years from 1990 to 2010
years = list(range(1990, 2011))

# Sales data for each novel in millions
pride_prejudice_sales = [0.5, 0.6, 0.8, 1.1, 1.5, 1.7, 2.0, 2.3, 2.6, 3.0, 3.4, 4.0, 4.5, 4.8, 5.0, 5.2, 5.4, 5.5, 5.6, 5.7, 5.9]
mockingbird_sales = [1.0, 1.2, 1.4, 1.6, 2.0, 2.3, 2.5, 2.8, 3.2, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 6.8, 7.0, 7.2, 7.3, 7.5]
nineteen_eighty_four_sales = [0.7, 0.9, 1.0, 1.3, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.2, 3.5, 3.8, 4.1, 4.4, 4.7, 5.0, 5.3, 5.5, 5.7, 5.9]
moby_dick_sales = [0.3, 0.4, 0.5, 0.6, 0.8, 0.9, 1.1, 1.2, 1.5, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.2, 3.5, 3.7, 3.9, 4.0, 4.1]
gatsby_sales = [0.4, 0.6, 0.7, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.3, 4.5, 4.7, 4.9, 5.0]

# Create the figure and axis
plt.figure(figsize=(12, 6))
plt.plot(years, pride_prejudice_sales, marker='o', linestyle='-', color='purple', linewidth=2, label='Pride and Prejudice')
plt.plot(years, mockingbird_sales, marker='s', linestyle='--', color='green', linewidth=2, label='To Kill a Mockingbird')
plt.plot(years, nineteen_eighty_four_sales, marker='^', linestyle='-.', color='blue', linewidth=2, label='1984')
plt.plot(years, moby_dick_sales, marker='D', linestyle=':', color='red', linewidth=2, label='Moby Dick')
plt.plot(years, gatsby_sales, marker='x', linestyle='-', color='orange', linewidth=2, label='The Great Gatsby')

# Title and labels
plt.title('Impact of Famous Historical Novels\non Literary Interest (1990-2010)', fontsize=14, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Book Sales (Millions)', fontsize=12)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(range(0, 9, 1))

# Legend
plt.legend(title='Novels', fontsize=10)

# Grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()