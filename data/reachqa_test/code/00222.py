import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Biography']
borrowing_percentages = [35, 25, 15, 10, 15]

# Data for the pie chart (average reading time in hours)
average_reading_time = [6, 5, 8, 7, 4]  # in hours

# Colors for the bars and pie chart
bar_colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']
pie_colors = ['#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f', '#cab2d6']

# Create the figure and a 1x2 subplot layout
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Bar chart
ax1 = axes[0]
bars = ax1.bar(genres, borrowing_percentages, color=bar_colors)
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10)

ax1.set_title("Literature Genre Popularity in Public Library\nBorrowing Trends of 2023", fontsize=14, pad=20)
ax1.set_xlabel("Genres", fontsize=12)
ax1.set_ylabel("Percentage of Total Borrows", fontsize=12)
ax1.set_ylim(0, 40)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Pie chart
ax2 = axes[1]
wedges, texts, autotexts = ax2.pie(average_reading_time, labels=genres, autopct='%1.1f%%', startangle=90, colors=pie_colors, pctdistance=0.85, wedgeprops=dict(width=0.4))
ax2.set_title("Average Reading Time per Genre", fontsize=14, pad=20)
ax2.set_aspect('equal')

# Beautify the text labels for the pie chart
for text in texts:
    text.set_size(10)
for autotext in autotexts:
    autotext.set_size(10)
    autotext.set_color('white')

# Overall layout adjustments
plt.tight_layout()

# Display the plot
plt.show()