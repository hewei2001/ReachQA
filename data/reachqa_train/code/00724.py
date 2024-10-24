import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the genres and their appeal scores for the radar chart
genres = ['Mystery', 'Science Fiction', 'Historical Fiction', 'Fantasy', 'Romance', 'Non-Fiction']
appeal_scores = [80, 70, 65, 85, 75, 60]

# Additional dataset for radar chart comparison
comparison_scores = [78, 72, 68, 82, 70, 65]

# Create angles for radar chart
num_vars = len(genres)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]
appeal_scores += appeal_scores[:1]
comparison_scores += comparison_scores[:1]

# Additional data for the bar chart
average_reading_times = [30, 45, 50, 40, 35, 55]  # in minutes

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7), subplot_kw=dict(polar=True))
fig.suptitle('Literary Genre Analysis', fontsize=16, fontweight='bold', y=1.05)

# Radar chart
ax = axes[0]
ax.set_ylim(0, 100)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(genres, color='grey', fontsize=12)
ax.plot(angles, appeal_scores, linewidth=1.5, linestyle='solid', color='blue', marker='o', label='Reader Scores')
ax.fill(angles, appeal_scores, 'blue', alpha=0.1)
ax.plot(angles, comparison_scores, linewidth=1.5, linestyle='--', color='green', marker='x', label='Comparison Scores')
ax.fill(angles, comparison_scores, 'green', alpha=0.1)
ax.set_title('Genre Appeal Scores', fontsize=14, fontweight='bold')
ax.yaxis.grid(True)
ax.spines['polar'].set_visible(False)
ax.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.2, 1))

# Bar chart
ax2 = axes[1]
bars = ax2.bar(genres, average_reading_times, color='skyblue', edgecolor='black')
ax2.set_ylim(0, 60)
ax2.set_ylabel('Average Reading Time (minutes)', fontsize=12, color='grey')
ax2.set_title('Average Reading Time per Genre', fontsize=14, fontweight='bold')
ax2.tick_params(axis='x', labelrotation=45)
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, yval, ha='center', va='bottom', fontsize=10, color='black')

# Adjust layout for better readability
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plots
plt.show()