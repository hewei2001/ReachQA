import matplotlib.pyplot as plt
import numpy as np

# Define years from 1990 to 2010
years = np.array(range(1990, 2011))

# Sales data for each novel in millions
pride_prejudice_sales = np.array([0.5, 0.6, 0.8, 1.1, 1.5, 1.7, 2.0, 2.3, 2.6, 3.0, 3.4, 4.0, 4.5, 4.8, 5.0, 5.2, 5.4, 5.5, 5.6, 5.7, 5.9])
mockingbird_sales = np.array([1.0, 1.2, 1.4, 1.6, 2.0, 2.3, 2.5, 2.8, 3.2, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 6.8, 7.0, 7.2, 7.3, 7.5])
nineteen_eighty_four_sales = np.array([0.7, 0.9, 1.0, 1.3, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.2, 3.5, 3.8, 4.1, 4.4, 4.7, 5.0, 5.3, 5.5, 5.7, 5.9])
moby_dick_sales = np.array([0.3, 0.4, 0.5, 0.6, 0.8, 0.9, 1.1, 1.2, 1.5, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.2, 3.5, 3.7, 3.9, 4.0, 4.1])
gatsby_sales = np.array([0.4, 0.6, 0.7, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.3, 4.5, 4.7, 4.9, 5.0])

# Sales growth rate calculation
pride_prejudice_growth = np.diff(pride_prejudice_sales, prepend=0)
mockingbird_growth = np.diff(mockingbird_sales, prepend=0)
nineteen_eighty_four_growth = np.diff(nineteen_eighty_four_sales, prepend=0)
moby_dick_growth = np.diff(moby_dick_sales, prepend=0)
gatsby_growth = np.diff(gatsby_sales, prepend=0)

# Create the figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# First subplot: Sales over time
axs[0].plot(years, pride_prejudice_sales, marker='o', linestyle='-', color='purple', linewidth=2, label='Pride and Prejudice')
axs[0].plot(years, mockingbird_sales, marker='s', linestyle='--', color='green', linewidth=2, label='To Kill a Mockingbird')
axs[0].plot(years, nineteen_eighty_four_sales, marker='^', linestyle='-.', color='blue', linewidth=2, label='1984')
axs[0].plot(years, moby_dick_sales, marker='D', linestyle=':', color='red', linewidth=2, label='Moby Dick')
axs[0].plot(years, gatsby_sales, marker='x', linestyle='-', color='orange', linewidth=2, label='The Great Gatsby')

axs[0].set_title('Novel Sales Over Time (1990-2010)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Book Sales (Millions)', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(range(0, 9, 1))
axs[0].legend(title='Novels', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Second subplot: Sales growth rate over time
axs[1].bar(years - 0.3, pride_prejudice_growth, width=0.15, label='Pride and Prejudice', color='purple', alpha=0.7)
axs[1].bar(years - 0.15, mockingbird_growth, width=0.15, label='To Kill a Mockingbird', color='green', alpha=0.7)
axs[1].bar(years, nineteen_eighty_four_growth, width=0.15, label='1984', color='blue', alpha=0.7)
axs[1].bar(years + 0.15, moby_dick_growth, width=0.15, label='Moby Dick', color='red', alpha=0.7)
axs[1].bar(years + 0.3, gatsby_growth, width=0.15, label='The Great Gatsby', color='orange', alpha=0.7)

axs[1].set_title('Yearly Growth Rate in Novel Sales (1990-2010)', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth in Sales (Millions)', fontsize=12)
axs[1].set_xticks(years)
axs[1].set_xticklabels(years, rotation=45)
axs[1].legend(title='Novels', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()