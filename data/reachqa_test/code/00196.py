import matplotlib.pyplot as plt
import numpy as np

# Expanded genres with communities and reading format
genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Historical Fiction', 'Thriller', 'Non-Fiction', 'Adventure']
communities = {
    'Fantasy': ['Elf Grove', 'Wizards Hub'],
    'Mystery': ["Detective's Domain", "Sherlock's Society"],
    'Romance': ["Lover's Lane", "Heart's Haven"],
    'Science Fiction': ['Sci-Fi City', 'Galactic Guild'],
    'Historical Fiction': ['Ancient Archives', 'Time Travelers'],
    'Thriller': ['Suspense Street', 'Edge End'],
    'Non-Fiction': ['Fact Focus', 'Knowledge Knoll'],
    'Adventure': ['Quest Quarters', 'Voyage Village']
}
books_read = np.array([
    [30, 20],  # Fantasy
    [25, 15],  # Mystery
    [35, 10],  # Romance
    [20, 10],  # Science Fiction
    [15, 10],  # Historical Fiction
    [22, 8],   # Thriller
    [18, 12],  # Non-Fiction
    [28, 15]   # Adventure
])  # books read (digital, print)

# Setup plot
fig, ax = plt.subplots(figsize=(14, 9))

x_pos = np.arange(len(genres))
width = 0.35

# Stacked bar chart: Digital vs Print
bars_digital = ax.bar(x_pos, books_read[:, 0], width, label='Digital', color='#4682B4')
bars_print = ax.bar(x_pos, books_read[:, 1], width, bottom=books_read[:, 0], label='Print', color='#DA70D6')

# Add line plot: Total reading hours
reading_hours = np.array([70, 55, 60, 45, 40, 50, 45, 60])
ax2 = ax.twinx()
ax2.plot(x_pos, reading_hours, marker='o', color='#FF4500', linewidth=2, label='Reading Hours')

# Annotation and data labels
for i, (bar_digital, bar_print) in enumerate(zip(bars_digital, bars_print)):
    height_digital = bar_digital.get_height()
    height_print = bar_print.get_height() + height_digital
    ax.text(bar_digital.get_x() + bar_digital.get_width() / 2, height_print + 1, 
            f"{communities[genres[i]][0]}\n{communities[genres[i]][1]}\nTotal: {int(height_print)} Books", 
            ha='center', va='bottom', fontsize=9, color='black')

# Title and axis labels
ax.set_title("Diverse Book Genre Popularity in Fiction Wonderland\nAnalyzing Reading Formats and Hours", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Genres", fontsize=12)
ax.set_ylabel("Avg. Books Read per Month", fontsize=12)
ax2.set_ylabel("Total Reading Hours", fontsize=12)

# X-axis customization
ax.set_xticks(x_pos)
ax.set_xticklabels(genres, rotation=30, ha='right', fontsize=11)

# Grid and aesthetics
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_facecolor('#F5F5F5')

# Legends for clarity
ax.legend(loc='upper left', bbox_to_anchor=(0, -0.1), fontsize=11)
ax2.legend(loc='upper right', bbox_to_anchor=(1, -0.1), fontsize=11)

# Adjust layout to ensure all elements fit well
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()