import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
fantasy_readership = [2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]
mystery_readership = [3, 3.2, 3.5, 4, 4.2, 5, 5.5, 6, 7, 7.5, 8]
non_fiction_readership = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
romance_readership = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
sci_fi_readership = [2, 2.2, 2.5, 3, 3.2, 4, 4.5, 5, 5.5, 6, 7]

# Summing up readership to create overlay data
total_readership = np.array(fantasy_readership) + np.array(mystery_readership) + \
                   np.array(non_fiction_readership) + np.array(romance_readership) + \
                   np.array(sci_fi_readership)

# Related data: Number of new book titles (fictional)
new_titles_released = [10, 12, 15, 20, 22, 25, 28, 30, 35, 40, 45]

# Prepare the data matrix for the stacked area chart
readership_data = np.vstack([fantasy_readership, mystery_readership, non_fiction_readership, romance_readership, sci_fi_readership])
genres = ['Fantasy', 'Mystery', 'Non-Fiction', 'Romance', 'Science Fiction']

# Plotting setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked area plot for readership data
ax1.stackplot(years, readership_data, labels=genres, colors=['#8fbc8f', '#20b2aa', '#ffcccb', '#ffd700', '#6a5acd'], alpha=0.7)
ax1.set_title('The Evolution of Book Genres Over a Decade\nwith New Titles Release Trend', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Readership (in Millions)', fontsize=12)
ax1.grid(linestyle='--', alpha=0.6)

# Secondary axis for the number of new titles released
ax2 = ax1.twinx()
ax2.plot(years, new_titles_released, color='coral', linestyle='--', marker='o', linewidth=2, label='New Titles Released')
ax2.set_ylabel('New Titles Released', fontsize=12, color='coral')
ax2.tick_params(axis='y', labelcolor='coral')

# Annotations for significant trends
ax1.annotate('Spike in Fantasy\ndue to Popular Series', xy=(2015, 5), xytext=(2013, 10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.7))
ax2.annotate('Increase in New Titles', xy=(2018, 30), xytext=(2016, 37),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='coral'), fontsize=10, ha='center', color='coral')

# Adjust layout and legend
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
ax1.legend(loc='upper left', frameon=True, bbox_to_anchor=(0, 1), borderaxespad=0., title='Genres')
ax2.legend(loc='upper right', frameon=True)

# Show plot
plt.show()