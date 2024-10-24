import matplotlib.pyplot as plt
import numpy as np

# Data: Number of books read per month by students in different grades
data = {
    'Grade 9': [1, 3, 4, 0, 5, 2, 1, 4, 3, 2],
    'Grade 10': [2, 1, 5, 2, 3, 4, 2, 6, 3, 1],
    'Grade 11': [6, 7, 5, 4, 6, 8, 9, 5, 6, 4],
    'Grade 12': [3, 2, 4, 1, 5, 3, 2, 4, 3, 2]
}

# Prepare data for plotting
grades = list(data.keys())
books_read = [data[grade] for grade in grades]
average_books = [np.mean(data[grade]) for grade in grades]

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Horizontal box plot
box = ax1.boxplot(books_read, vert=False, patch_artist=True, notch=True, whis=1.5)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize box plot
ax1.set_title("Reading Habits Among High School Students\n(Number of Books Read per Month)", fontsize=14, fontweight='bold')
ax1.set_xlabel('Number of Books Read', fontsize=12)
ax1.set_yticks(range(1, len(grades) + 1))
ax1.set_yticklabels(grades, fontsize=12)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Add median line labels
for median in box['medians']:
    ax1.text(median.get_xdata()[0], median.get_ydata()[0], f'{int(median.get_xdata()[0])}', 
             horizontalalignment='center', fontsize=10, color='black')

# Bar chart for average books read
ax2.bar(grades, average_books, color=colors, alpha=0.7)
ax2.set_title("Average Number of Books Read per Month by Grade", fontsize=14, fontweight='bold')
ax2.set_ylabel('Average Number of Books', fontsize=12)
ax2.set_ylim(0, max(average_books) + 2)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Add average labels above the bars
for i, avg in enumerate(average_books):
    ax2.text(i, avg + 0.1, f'{avg:.2f}', ha='center', fontsize=10)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()