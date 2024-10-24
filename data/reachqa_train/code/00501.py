import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average hours spent per week reading each format
books_hours = [5, 5.1, 5, 4.8, 4.5, 4.3, 4.2, 4.0, 3.8, 3.7, 3.5]
ebooks_hours = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.2, 5.5]
audiobooks_hours = [0.5, 0.7, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.7, 5.0]

# Set up the plot
plt.figure(figsize=(12, 7))

# Plot each reading format
plt.plot(years, books_hours, marker='o', linestyle='-', color='#2E8B57', linewidth=2, label='Books')
plt.plot(years, ebooks_hours, marker='s', linestyle='--', color='#4682B4', linewidth=2, label='E-books')
plt.plot(years, audiobooks_hours, marker='^', linestyle='-.', color='#D2691E', linewidth=2, label='Audiobooks')

# Titles and labels
plt.title("The Evolution of Reading Habits\nOver a Decade (2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Hours per Week", fontsize=12)

# Adding a legend
plt.legend(title="Reading Formats", loc='upper left')

# Customizing grid and style
plt.grid(True, linestyle='--', linewidth=0.5)

# Highlight significant points
plt.annotate('Rise of E-books', xy=(2015, 3), xytext=(2013, 4),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='blue')

plt.annotate('Audiobooks Gain Popularity', xy=(2018, 4), xytext=(2016, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='chocolate')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()