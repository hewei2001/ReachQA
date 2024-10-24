import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Market shares for each medium
print_books = [70, 68, 67, 65, 64, 62, 60, 58, 55, 53, 50, 48, 45, 43, 40, 38, 35, 33, 30, 28, 25]
ebooks = [5, 6, 7, 9, 10, 12, 14, 17, 20, 22, 25, 28, 30, 33, 35, 37, 40, 42, 43, 45, 48]
audio_books = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20]

# Create a new figure
plt.figure(figsize=(12, 7))

# Plotting each line with different styles and markers
plt.plot(years, print_books, label='Print Books', color='brown', linestyle='-', marker='o', linewidth=2)
plt.plot(years, ebooks, label='E-books', color='blue', linestyle='--', marker='s', linewidth=2)
plt.plot(years, audio_books, label='Audio Books', color='green', linestyle='-.', marker='d', linewidth=2)

# Title and axis labels
plt.title('The Evolution of Publishing Trends:\nFrom Manuscripts to Digital Platforms', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Market Share (%)', fontsize=12)

# Adding a legend
plt.legend(title='Publishing Mediums', loc='upper left', fontsize=10, title_fontsize=11)

# Adding grid lines for better visualization
plt.grid(True, linestyle='--', alpha=0.6)

# Set tick parameters for better clarity
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()