import matplotlib.pyplot as plt
import numpy as np

# Book genres
genres = ['Fantasy', 'Mystery', 'Sci-Fi', 'Historical', 'Non-fiction']

# Data: Number of students who prefer each genre for each grade
grade_8 = [30, 24, 19, 15, 22]
grade_9 = [25, 29, 25, 20, 28]
grade_10 = [20, 18, 22, 30, 25]

# Define the positions for bars
x = np.arange(len(genres))
width = 0.25  # Width of the bars

# Create the bar chart with annotations
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting each grade's data
bars_8 = ax.bar(x - width, grade_8, width, label='8th Grade', color='skyblue')
bars_9 = ax.bar(x, grade_9, width, label='9th Grade', color='limegreen')
bars_10 = ax.bar(x + width, grade_10, width, label='10th Grade', color='salmon')

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Number of Students', fontsize=12)
ax.set_title('Favorite Book Genres Among Students\nof Greenwood High School: A Grade-wise Analysis', 
             fontsize=14, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(genres)
ax.legend(loc='upper right')

# Annotating the bars with data values
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset text by 3 points above the bar
                    textcoords="offset points",
                    ha='center', va='bottom')

annotate_bars(bars_8)
annotate_bars(bars_9)
annotate_bars(bars_10)

# Enable grid and improve layout
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()