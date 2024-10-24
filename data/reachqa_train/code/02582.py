import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(1900, 2001, 10)

# Visitor numbers in thousands for each library
nypl_visitors = [80, 120, 150, 170, 200, 220, 210, 180, 140, 130, 150]
british_library_visitors = [60, 70, 90, 110, 150, 160, 140, 120, 110, 100, 120]
bibliotheque_france_visitors = [50, 65, 80, 100, 130, 155, 135, 115, 90, 95, 110]

# Book acquisition data for each library
nypl_books = [30, 40, 55, 60, 70, 75, 80, 70, 50, 40, 50]
british_library_books = [20, 25, 30, 35, 50, 55, 50, 45, 40, 35, 40]
bibliotheque_france_books = [15, 18, 22, 28, 40, 45, 42, 38, 30, 28, 35]

# Create a new figure
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the visitor numbers as lines
ax1.plot(years, nypl_visitors, label='New York Public Library', color='navy', linestyle='-', marker='o', markersize=8, linewidth=2)
ax1.plot(years, british_library_visitors, label='British Library', color='crimson', linestyle='--', marker='s', markersize=8, linewidth=2)
ax1.plot(years, bibliotheque_france_visitors, label='Bibliothèque Nationale de France', color='darkgreen', linestyle='-.', marker='d', markersize=8, linewidth=2)

# Title and axis labels
ax1.set_title('Rise and Fall of the Great Libraries:\nA Journey Through Time (1900-2000)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Annual Visitors (thousands)', fontsize=14)

# Adding a secondary y-axis for book acquisition data
ax2 = ax1.twinx()
ax2.set_ylabel('Books Acquired (thousands)', fontsize=14)

# Plot the book acquisitions as bars
width = 3  # Width of the bars
ax2.bar(years - width, nypl_books, width=width, color='navy', alpha=0.4, label='NYPL Books Acquired')
ax2.bar(years, british_library_books, width=width, color='crimson', alpha=0.4, label='British Library Books Acquired')
ax2.bar(years + width, bibliotheque_france_books, width=width, color='darkgreen', alpha=0.4, label='BNF Books Acquired')

# Adding legends
ax1.legend(title='Library Visitors', loc='upper left', fontsize=12, title_fontsize=13)
ax2.legend(loc='upper right', fontsize=12, title_fontsize=13)

# Adding grid lines for better visualization
ax1.grid(True, linestyle='--', alpha=0.6)

# Set tick parameters for better clarity
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 301, 50))
ax2.set_yticks(np.arange(0, 101, 10))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()