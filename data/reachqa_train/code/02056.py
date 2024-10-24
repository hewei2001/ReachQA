import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for reading habits in percentages
print_books = np.array([70, 65, 60, 58, 55, 50, 45, 40, 35, 30, 25])
ebooks = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
online_articles = np.array([20, 20, 20, 17, 15, 15, 15, 15, 15, 15, 15])

# Total reading percentage over the years
total_reading = print_books + ebooks + online_articles

# Calculate bottom positions for stacking
bottom_ebooks = print_books
bottom_online_articles = bottom_ebooks + ebooks

# Color scheme
colors = ['#8A2BE2', '#5F9EA0', '#FF6347']

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))
fig.suptitle('The Evolution of Reading Habits in the Digital Age\n2010-2020', fontsize=16, fontweight='bold', ha='center')

# Stacked bar chart for reading habits
ax1.bar(years, print_books, label='Print Books', color=colors[0], width=0.6, alpha=0.8)
ax1.bar(years, ebooks, bottom=bottom_ebooks, label='E-books', color=colors[1], width=0.6, alpha=0.8)
ax1.bar(years, online_articles, bottom=bottom_online_articles, label='Online Articles', color=colors[2], width=0.6, alpha=0.8)

# Line plot for total reading
ax2 = ax1.twinx()
ax2.plot(years, total_reading, label='Total Reading', color='black', linestyle='-', marker='o', markersize=8, linewidth=2)

# Axis labeling and limits
ax1.set_ylabel('Reading Time Proportion (%)', fontsize=12)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha="right")
ax1.set_ylim(0, 100)
ax1.yaxis.set_major_formatter(lambda x, _: f'{int(x)}%')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

ax2.set_ylabel('Total Reading (%)', fontsize=12)
ax2.set_ylim(0, 100)
ax2.yaxis.set_major_formatter(lambda x, _: f'{int(x)}%')

# Legends
ax1.legend(loc='upper left', title='Reading Format', fontsize=10, title_fontsize='12')
ax2.legend(loc='upper right', fontsize=10)

# Annotate data values on bars
for year, pb, eb, oa in zip(years, print_books, ebooks, online_articles):
    ax1.text(year, pb / 2, f'{pb}%', ha='center', va='center', color='white', fontsize=9)
    ax1.text(year, bottom_ebooks[np.where(years == year)][0] + eb / 2, f'{eb}%', ha='center', va='center', color='white', fontsize=9)
    ax1.text(year, bottom_online_articles[np.where(years == year)][0] + oa / 2, f'{oa}%', ha='center', va='center', color='white', fontsize=9)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()