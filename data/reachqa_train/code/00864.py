import matplotlib.pyplot as plt
import numpy as np

# Expanded dataset
genres = ['Fantasy', 'Mystery', 'Sci-Fi', 'Historical', 'Non-fiction', 'Biography', 'Thriller']

# Number of students preferring each genre for additional grades
grade_7 = [28, 26, 24, 10, 15, 18, 23]
grade_8 = [30, 24, 19, 15, 22, 27, 26]
grade_9 = [25, 29, 25, 20, 28, 24, 30]
grade_10 = [20, 18, 22, 30, 25, 29, 19]
grade_11 = [23, 21, 26, 18, 30, 22, 27]

# Calculate means and standard deviation
all_grades = np.array([grade_7, grade_8, grade_9, grade_10, grade_11])
mean_preference = np.mean(all_grades, axis=0)
std_deviation = np.std(all_grades, axis=0)

# Define the positions for bars
x = np.arange(len(genres))
width = 0.15  # Reduced width for more categories

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each grade's data
bars_7 = ax.bar(x - 2*width, grade_7, width, label='7th Grade', color='cornflowerblue')
bars_8 = ax.bar(x - width, grade_8, width, label='8th Grade', color='skyblue')
bars_9 = ax.bar(x, grade_9, width, label='9th Grade', color='limegreen')
bars_10 = ax.bar(x + width, grade_10, width, label='10th Grade', color='salmon')
bars_11 = ax.bar(x + 2*width, grade_11, width, label='11th Grade', color='coral')

# Overlay mean preferences with error bars
ax.errorbar(x, mean_preference, yerr=std_deviation, fmt='o', color='black', ecolor='grey', capsize=5, label='Mean ± SD')

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Number of Students', fontsize=12)
ax.set_title('Favorite Book Genres Among Students\nof Greenwood High School: Grade-wise Analysis with Statistical Metrics', 
             fontsize=14, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(genres, rotation=45, ha='right')
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Annotating the bars with data values
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

annotate_bars(bars_7)
annotate_bars(bars_8)
annotate_bars(bars_9)
annotate_bars(bars_10)
annotate_bars(bars_11)

# Enable grid and improve layout
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Use tight layout to ensure everything fits without overlapping
plt.tight_layout()

# Show the plot
plt.show()