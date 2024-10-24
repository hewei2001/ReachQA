import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Number of e-books published each year for different genres
fiction = [300, 310, 320, 330, 350, 370, 390, 410, 430, 450, 470]
non_fiction = [250, 260, 270, 280, 290, 300, 315, 330, 340, 350, 360]
sci_fi = [100, 105, 110, 120, 140, 160, 180, 210, 240, 270, 300]
fantasy = [80, 85, 90, 95, 110, 125, 140, 160, 180, 200, 225]
self_help = [50, 55, 65, 75, 90, 110, 130, 155, 180, 205, 230]

# Stack the data
stacked_data = np.vstack([fiction, non_fiction, sci_fi, fantasy, self_help])

# Colors for each genre
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Plotting the area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, stacked_data, labels=['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Self-Help'], colors=colors, alpha=0.8)

# Adding title, labels, and legend
plt.title('The Digital Odyssey: Evolution of E-Book Genres\nOver a Decade', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of E-Books Published', fontsize=14)
plt.legend(loc='upper left', title='Genres', fontsize=12, frameon=False)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1600, 200))

# Add minor grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()