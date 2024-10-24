import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average hours spent per week reading each format
books_hours = [5, 5.1, 5, 4.8, 4.5, 4.3, 4.2, 4.0, 3.8, 3.7, 3.5]
ebooks_hours = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.2, 5.5]
audiobooks_hours = [0.5, 0.7, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.7, 5.0]

# Data for total books published per year
total_books_published = [50000, 52000, 54000, 56000, 58000, 60000, 62000, 64000, 66000, 68000, 70000]

# Set up the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the reading habits with lines
ax1.plot(years, books_hours, marker='o', linestyle='-', color='#2E8B57', linewidth=2, label='Books')
ax1.plot(years, ebooks_hours, marker='s', linestyle='--', color='#4682B4', linewidth=2, label='E-books')
ax1.plot(years, audiobooks_hours, marker='^', linestyle='-.', color='#D2691E', linewidth=2, label='Audiobooks')

# Add a twin y-axis to plot the total books published
ax2 = ax1.twinx()
ax2.bar(years, total_books_published, color='grey', alpha=0.3, width=0.6, label='Books Published')

# Titles and labels
ax1.set_title("The Evolution of Reading Habits and Publishing Trends\n (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Average Hours per Week", fontsize=12)
ax2.set_ylabel("Total Books Published", fontsize=12)

# Adding legends
lines_labels = [ax1.get_legend_handles_labels(), ax2.get_legend_handles_labels()]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper left', title="Reading Formats & Publishing")

# Customizing grid and style
ax1.grid(True, linestyle='--', linewidth=0.5)

# Highlight significant points
ax1.annotate('Rise of E-books', xy=(2015, 3), xytext=(2013, 4),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='blue')

ax1.annotate('Audiobooks Gain Popularity', xy=(2018, 4), xytext=(2016, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='chocolate')

ax2.axhline(y=65000, color='red', linestyle=':', linewidth=1.5)
ax2.text(2011, 65500, 'Threshold: 65K Books', color='red', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()