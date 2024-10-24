import matplotlib.pyplot as plt
import numpy as np

# Data: Popularity scores for different programming languages in 2023
languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'Ruby', 'Swift', 'PHP', 'Go', 'R']
popularity_scores = [89, 87, 85, 78, 77, 66, 65, 55, 53, 50]

# Colors for each language bar
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666', '#8fd3f4', '#d0bbff']

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(16, 10))
bars = ax.barh(languages, popularity_scores, color=colors, height=0.6, edgecolor='black')

# Title and labels
ax.set_title('The Evolution of Coding Languages:\nPopularity Trends Among Developers in 2023', 
             fontsize=20, weight='bold', pad=20)
ax.set_xlabel('Popularity Score', fontsize=14)
ax.set_ylabel('Programming Languages', fontsize=14)

# Adding a subtle grid with minor ticks
ax.xaxis.set_minor_locator(plt.MultipleLocator(2))
ax.xaxis.grid(True, linestyle='--', alpha=0.5)
ax.yaxis.grid(False)

# Annotate most popular language with enhanced visual detail
max_score_index = popularity_scores.index(max(popularity_scores))
ax.annotate('Most Popular', 
            xy=(popularity_scores[max_score_index], max_score_index), 
            xytext=(popularity_scores[max_score_index] + 5, max_score_index),
            arrowprops=dict(facecolor='black', arrowstyle='fancy'),
            fontsize=12, color='black', weight='bold')

# Adding icons (simulated with text) next to language labels for visual interest
for i, language in enumerate(languages):
    ax.text(-10, i, '🔹', fontsize=14, va='center', ha='right')

# Adding data labels at the end of each bar with background
for bar in bars:
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width()}', va='center', ha='left', fontsize=12, color='black',
            bbox=dict(facecolor='white', alpha=0.6, edgecolor='none', boxstyle="round,pad=0.3"))

# Enhanced tick parameters
ax.tick_params(axis='y', which='major', labelsize=12, pad=10)

# Customizing the background
ax.set_facecolor('#f5f5f5')

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()