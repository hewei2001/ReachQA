import numpy as np
import matplotlib.pyplot as plt

# Define the years and data for literary genre popularity (in arbitrary units)
years = np.arange(2010, 2021)

# Crafted data for each literary genre
fantasy = np.array([20, 25, 30, 45, 65, 80, 95, 110, 130, 145, 160])
mystery = np.array([30, 35, 40, 45, 50, 55, 65, 70, 75, 85, 90])
science_fiction = np.array([15, 20, 28, 35, 45, 55, 70, 85, 100, 115, 130])
romance = np.array([25, 30, 35, 40, 45, 50, 60, 70, 80, 85, 95])
non_fiction = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])

# Calculate a related dataset for overlay - Global Literary Interest Index
global_interest = fantasy * 0.4 + mystery * 0.3 + science_fiction * 0.2 + romance * 0.05 + non_fiction * 0.05

# Stack the data for the area plot
genre_data = np.vstack([fantasy, mystery, science_fiction, romance, non_fiction])

# Create the stacked area plot with an overlay line plot
fig, ax1 = plt.subplots(figsize=(14, 9))

colors = ['#8856a7', '#43a2ca', '#7fcdbb', '#a6d854', '#fdae61']
labels = ['Fantasy', 'Mystery', 'Science Fiction', 'Romance', 'Non-Fiction']

# Stacked area plot
ax1.stackplot(years, genre_data, labels=labels, colors=colors, alpha=0.85)

# Secondary y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(years, global_interest, 'k--', linewidth=2, label='Global Literary Interest Index')
ax2.set_ylabel('Interest Index', fontsize=14)
ax2.legend(loc='upper right', fontsize=12)

# Customize the plot
ax1.set_title("The Literary Wave: A Decade of Genre Popularity\nOn Novel Isle (2010-2020)", fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Popularity (Arbitrary Units)', fontsize=14)

# Add legend and grid
ax1.legend(loc='upper left', fontsize=12, title='Genre', frameon=False)
ax1.grid(linestyle='--', alpha=0.6)

# Annotate significant events or shifts
ax1.annotate('Fantasy Surge', xy=(2015, 85), xytext=(2011, 300),
             arrowprops=dict(facecolor='purple', arrowstyle='->', lw=1.5),
             fontsize=12, color='purple')

ax1.annotate('Rise of Sci-Fi', xy=(2018, 200), xytext=(2015, 380),
             arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5),
             fontsize=12, color='green')

# Add description box
props = dict(boxstyle='round', facecolor='lavender', alpha=0.3)
textstr = ('Novel Isle saw a dynamic shift in\n'
           'literary tastes with Fantasy and Sci-Fi\n'
           'gaining immense traction.')
ax1.text(0.02, 0.97, textstr, transform=ax1.transAxes, fontsize=12,
         verticalalignment='top', bbox=props)

# Highlight start and end values
for idx, genre in enumerate(labels):
    ax1.annotate(f'{genre_data[idx, 0]}', (2010, genre_data[idx, 0]), textcoords="offset points", xytext=(-15,5), ha='center')
    ax1.annotate(f'{genre_data[idx, -1]}', (2020, genre_data[idx, -1] + np.sum(genre_data[:idx, -1])), textcoords="offset points", xytext=(-15,-10), ha='center')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()