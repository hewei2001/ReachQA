import matplotlib.pyplot as plt
import numpy as np

# Define decades and genre popularity data
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
action_popularity = [20, 25, 30, 28, 35]
drama_popularity = [30, 35, 32, 30, 25]
comedy_popularity = [25, 20, 20, 22, 18]
sci_fi_popularity = [10, 8, 15, 18, 20]
horror_popularity = [15, 12, 3, 2, 2]

# Average movie ratings data
action_ratings = [6.5, 6.8, 7.2, 7.0, 7.4]
drama_ratings = [7.0, 7.5, 7.8, 7.6, 7.2]
comedy_ratings = [6.0, 6.3, 6.5, 6.7, 6.6]
sci_fi_ratings = [7.2, 7.0, 7.5, 7.8, 8.0]
horror_ratings = [5.5, 5.8, 6.0, 5.5, 5.2]

# Bar width and index for x positions
bar_width = 0.15
index = np.arange(len(decades))

# Create the plot with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# First subplot: Bar chart of genre popularity
ax1.bar(index - 2*bar_width, action_popularity, bar_width, label='Action', color='#FF5733', edgecolor='black')
ax1.bar(index - bar_width, drama_popularity, bar_width, label='Drama', color='#C70039', edgecolor='black')
ax1.bar(index, comedy_popularity, bar_width, label='Comedy', color='#900C3F', edgecolor='black')
ax1.bar(index + bar_width, sci_fi_popularity, bar_width, label='Sci-Fi', color='#581845', edgecolor='black')
ax1.bar(index + 2*bar_width, horror_popularity, bar_width, label='Horror', color='#2E4053', edgecolor='black')

ax1.set_xlabel('Decades', fontsize=12)
ax1.set_ylabel('Percentage of Movies (%)', fontsize=12)
ax1.set_title("Evolving Trends in Movie Genres\n1980s to 2020s", fontsize=14, fontweight='bold')
ax1.set_xticks(index)
ax1.set_xticklabels(decades)
ax1.legend(title="Genres", loc='upper right', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Add data labels above bars
def add_labels(bars_data, x_offset, axis):
    for i, value in enumerate(bars_data):
        axis.text(i + x_offset, value + 1, f'{value}%', ha='center', va='bottom', fontsize=9)

add_labels(action_popularity, -2*bar_width, ax1)
add_labels(drama_popularity, -bar_width, ax1)
add_labels(comedy_popularity, 0, ax1)
add_labels(sci_fi_popularity, bar_width, ax1)
add_labels(horror_popularity, 2*bar_width, ax1)

# Second subplot: Line plot of average ratings
ax2.plot(decades, action_ratings, marker='o', label='Action', color='#FF5733', linewidth=2)
ax2.plot(decades, drama_ratings, marker='s', label='Drama', color='#C70039', linewidth=2)
ax2.plot(decades, comedy_ratings, marker='^', label='Comedy', color='#900C3F', linewidth=2)
ax2.plot(decades, sci_fi_ratings, marker='D', label='Sci-Fi', color='#581845', linewidth=2)
ax2.plot(decades, horror_ratings, marker='x', label='Horror', color='#2E4053', linewidth=2)

ax2.set_xlabel('Decades', fontsize=12)
ax2.set_ylabel('Average Ratings', fontsize=12)
ax2.set_title("Trends in Average Movie Ratings\nby Genre (1980s to 2020s)", fontsize=14, fontweight='bold')
ax2.legend(title="Genres", loc='lower right', fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()