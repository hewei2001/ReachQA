import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Define the sales data for each fantasy genre
high_fantasy_sales = np.array([20, 23, 25, 28, 30, 35, 40, 44, 50, 55, 60])
urban_fantasy_sales = np.array([15, 16, 18, 20, 22, 25, 27, 30, 32, 33, 34])
dark_fantasy_sales = np.array([10, 12, 15, 18, 20, 23, 24, 25, 28, 30, 32])

# Define the number of fantasy books adapted into movies
adaptations = np.array([2, 3, 3, 4, 4, 5, 7, 10, 12, 14, 16])

# Set up the figure and axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Plot the stacked area chart on the first subplot
axes[0].stackplot(years, high_fantasy_sales, urban_fantasy_sales, dark_fantasy_sales,
                  labels=['High Fantasy', 'Urban Fantasy', 'Dark Fantasy'],
                  colors=['#FFD700', '#C71585', '#8B4513'], alpha=0.8)
axes[0].set_title('The Great Fantasy Book Boom:\nSales Trends in Imaginary Genres (2010-2020)',
                  fontsize=16, fontweight='bold', pad=15)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Book Sales (Thousands)', fontsize=12)
axes[0].legend(loc='upper left', fontsize=10, frameon=True)
axes[0].grid(True, which='major', linestyle='--', alpha=0.5)
axes[0].set_xticks(years)
axes[0].set_xticklabels(years, rotation=45, ha='right')
axes[0].annotate('Rise of Streaming Series', (2015, 80), 
                 textcoords="offset points", xytext=(30, 10), ha='center', fontsize=10,
                 arrowprops=dict(arrowstyle='->', color='black'))
axes[0].annotate('Fantasy Literature Awards Boost', (2018, 115),
                 textcoords="offset points", xytext=(-20, 10), ha='center', fontsize=10,
                 arrowprops=dict(arrowstyle='->', color='black'))

# Plot the line chart for adaptations on the second subplot
axes[1].plot(years, adaptations, marker='o', linestyle='-', color='teal', label='Movie Adaptations')
axes[1].set_title('Fantasy Books Adapted into Movies (2010-2020)', fontsize=16, fontweight='bold', pad=15)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Number of Adaptations', fontsize=12)
axes[1].legend(loc='upper left', fontsize=10, frameon=True)
axes[1].grid(True, which='major', linestyle='--', alpha=0.5)
axes[1].set_xticks(years)
axes[1].set_xticklabels(years, rotation=45, ha='right')
axes[1].annotate('Peak in Adaptations', (2019, 14),
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10,
                 arrowprops=dict(arrowstyle='->', color='black'))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()