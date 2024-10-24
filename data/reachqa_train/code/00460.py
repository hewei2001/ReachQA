import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Market shares for each medium
print_books = [70, 68, 67, 65, 64, 62, 60, 58, 55, 53, 50, 48, 45, 43, 40, 38, 35, 33, 30, 28, 25]
ebooks = [5, 6, 7, 9, 10, 12, 14, 17, 20, 22, 25, 28, 30, 33, 35, 37, 40, 42, 43, 45, 48]
audio_books = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20]

# Calculate cumulative market share
total_market = np.array(print_books) + np.array(ebooks) + np.array(audio_books)

# Create a figure and a 1x2 grid of subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Original line plot
ax[0].plot(years, print_books, label='Print Books', color='brown', linestyle='-', marker='o', linewidth=2)
ax[0].plot(years, ebooks, label='E-books', color='blue', linestyle='--', marker='s', linewidth=2)
ax[0].plot(years, audio_books, label='Audio Books', color='green', linestyle='-.', marker='d', linewidth=2)
ax[0].set_title('The Evolution of Publishing Trends\nFrom Manuscripts to Digital Platforms', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Market Share (%)', fontsize=12)
ax[0].legend(title='Publishing Mediums', loc='upper right', fontsize=9, title_fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].set_xticks(years)
ax[0].set_xticklabels(years, rotation=45)
ax[0].set_yticks(np.arange(0, 101, 10))

# Additional stacked bar chart
ax[1].bar(years, print_books, color='brown', label='Print Books')
ax[1].bar(years, ebooks, bottom=print_books, color='blue', label='E-books')
ax[1].bar(years, audio_books, bottom=np.array(print_books) + np.array(ebooks), color='green', label='Audio Books')
ax[1].set_title('Cumulative Market Share Across Years', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Total Market Share (%)', fontsize=12)
ax[1].legend(title='Publishing Mediums', loc='upper right', fontsize=9, title_fontsize=10)
ax[1].set_xticks(years)
ax[1].set_xticklabels(years, rotation=45)
ax[1].set_yticks(np.arange(0, 101, 10))
ax[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plots
plt.show()