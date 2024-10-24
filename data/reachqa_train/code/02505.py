import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2020
years = np.arange(1990, 2021)

# Number of books for each genre over the years
fiction_books = [300, 320, 350, 380, 420, 470, 520, 590, 640, 700, 750, 800, 850, 890, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
non_fiction_books = [200, 210, 230, 250, 280, 310, 340, 380, 420, 460, 500, 550, 600, 650, 720, 800, 870, 940, 1020, 1100, 1180, 1270, 1360, 1450, 1540, 1630, 1720, 1810, 1900, 1990, 2080]
science_fiction_books = [50, 60, 70, 80, 100, 120, 150, 180, 210, 250, 290, 340, 400, 450, 500, 570, 650, 720, 800, 880, 950, 1020, 1100, 1180, 1250, 1330, 1400, 1480, 1550, 1620, 1700]
historical_novels = [70, 75, 80, 85, 95, 110, 130, 150, 180, 210, 240, 270, 310, 350, 400, 450, 500, 560, 630, 700, 770, 840, 920, 1000, 1080, 1170, 1260, 1350, 1440, 1530, 1620]

# Create the area plot
plt.figure(figsize=(14, 7))

plt.stackplot(years, fiction_books, non_fiction_books, science_fiction_books, historical_novels, 
              labels=['Fiction', 'Non-Fiction', 'Science Fiction', 'Historical Novels'],
              colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Set plot title and labels
plt.title('Evolution of Book Genres in City Library\n(1990-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Books', fontsize=14)
plt.xticks(years[::2], rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper left', title='Genres', fontsize=10)

# Enhance gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust plot to ensure no element is clipped
plt.tight_layout()

# Display the plot
plt.show()