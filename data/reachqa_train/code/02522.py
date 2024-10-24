import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Fictional readership data in millions for each genre
fantasy_readership = [2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]
mystery_readership = [3, 3.2, 3.5, 4, 4.2, 5, 5.5, 6, 7, 7.5, 8]
non_fiction_readership = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
romance_readership = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
sci_fi_readership = [2, 2.2, 2.5, 3, 3.2, 4, 4.5, 5, 5.5, 6, 7]

# Compile the data into a matrix for stacking
readership_data = np.vstack([fantasy_readership, mystery_readership, non_fiction_readership, romance_readership, sci_fi_readership])

# Genre labels
genres = ['Fantasy', 'Mystery', 'Non-Fiction', 'Romance', 'Science Fiction']

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot setup
ax.stackplot(years, readership_data, labels=genres, colors=['#8fbc8f', '#20b2aa', '#ffcccb', '#ffd700', '#6a5acd'], alpha=0.7)

# Titles and labels
ax.set_title('The Evolution of Book Genres Over a Decade\nin Digital Libraries', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Readership (in Millions)', fontsize=12)

# Customize grid
ax.grid(linestyle='--', alpha=0.6)

# Adding a legend
ax.legend(loc='upper left', frameon=True, bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# Annotate significant changes or trends
ax.annotate('Spike in Fantasy\ndue to Popular Series', xy=(2015, 5), xytext=(2013, 8),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.7))

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()