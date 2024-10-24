import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2020
years = np.arange(1990, 2021)

# Number of books for each genre over the years
fiction_books = np.array([300, 320, 350, 380, 420, 470, 520, 590, 640, 700, 750, 800, 850, 890, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500])
non_fiction_books = np.array([200, 210, 230, 250, 280, 310, 340, 380, 420, 460, 500, 550, 600, 650, 720, 800, 870, 940, 1020, 1100, 1180, 1270, 1360, 1450, 1540, 1630, 1720, 1810, 1900, 1990, 2080])
science_fiction_books = np.array([50, 60, 70, 80, 100, 120, 150, 180, 210, 250, 290, 340, 400, 450, 500, 570, 650, 720, 800, 880, 950, 1020, 1100, 1180, 1250, 1330, 1400, 1480, 1550, 1620, 1700])
historical_novels = np.array([70, 75, 80, 85, 95, 110, 130, 150, 180, 210, 240, 270, 310, 350, 400, 450, 500, 560, 630, 700, 770, 840, 920, 1000, 1080, 1170, 1260, 1350, 1440, 1530, 1620])

# Calculate total books and yearly percentage growth
total_books = fiction_books + non_fiction_books + science_fiction_books + historical_novels
percentage_growth = np.diff(total_books) / total_books[:-1] * 100

# Create the main plot and subplot
fig, (ax_main, ax_inset) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Main area plot
ax_main.stackplot(years, fiction_books, non_fiction_books, science_fiction_books, historical_novels,
                  labels=['Fiction', 'Non-Fiction', 'Science Fiction', 'Historical Novels'],
                  colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Overlay line plot for total books
ax_main.plot(years, total_books, color='black', linewidth=2, label='Total Books')

# Annotate key points
for i, y in enumerate([fiction_books, non_fiction_books, science_fiction_books, historical_novels]):
    ax_main.annotate(f'{y[-1]:,}', xy=(years[-1], y[-1]), xytext=(years[-1]+0.5, y[-1]),
                     textcoords='offset points', va='center', fontsize=9)

# Main plot settings
ax_main.set_title('Evolution of Book Genres and Total Books in City Library\n(1990-2020)', fontsize=16, fontweight='bold', pad=20)
ax_main.set_xlabel('Year', fontsize=14)
ax_main.set_ylabel('Number of Books', fontsize=14)
ax_main.set_xticks(years[::2])
ax_main.set_xticklabels(years[::2], rotation=45, fontsize=10)
ax_main.tick_params(axis='y', labelsize=10)  # Correctly set the fontsize for y-ticks
ax_main.legend(loc='upper left', title='Genres', fontsize=10)
ax_main.grid(axis='y', linestyle='--', alpha=0.7)

# Inset subplot for percentage growth
ax_inset.bar(years[1:], percentage_growth, color='gray', alpha=0.7)
ax_inset.set_title('Yearly Percentage Growth of Total Books', fontsize=12, pad=10)
ax_inset.set_xlabel('Year', fontsize=10)
ax_inset.set_ylabel('Growth (%)', fontsize=10)
ax_inset.set_xticks(years[::2])
ax_inset.set_xticklabels(years[::2], rotation=45, fontsize=8)
ax_inset.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()