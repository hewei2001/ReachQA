import matplotlib.pyplot as plt
import numpy as np

# List of films nominated for the Best Film category
films = [
    'The Enchanted Voyage',
    'City of Echoes',
    'Chronicles of the Unknown',
    'Whispers of the Forest',
    'The Last Frontier'
]

# Number of votes received by each film
votes = [4250, 3175, 2900, 2380, 1875]

# Calculating percentage of total votes
total_votes = sum(votes)
percentages = [vote / total_votes * 100 for vote in votes]

# Color scheme gradient based on vote count
norm_votes = np.array(votes) / max(votes)
colors = plt.cm.viridis(norm_votes)

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(films, votes, color=colors, height=0.6, edgecolor='grey', linewidth=0.8, alpha=0.85)

# Set title and labels
ax.set_title("Fictional Film Awards 2023\nBest Film Category: Votes and Percentages", 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Number of Votes", fontsize=12, labelpad=10)
ax.set_ylabel("Films", fontsize=12, labelpad=10)

# Adding data labels to the bars
for bar, percentage in zip(bars, percentages):
    width = bar.get_width()
    ax.annotate(f'{width:,} ({percentage:.1f}%)',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 5 points horizontal offset
                textcoords="offset points",
                ha='left', va='center', fontsize=10, color='black')

# Customize the ticks and grid
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax.xaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(0, max(votes) * 1.1)

# Add average line and annotation
average_votes = np.mean(votes)
ax.axvline(average_votes, color='red', linestyle='dashed', linewidth=1)
ax.text(average_votes * 1.05, len(films) - 0.5, f'Average: {int(average_votes):,}', 
        color='red', fontsize=10, verticalalignment='center')

# Ensure labels are clear and aligned
ax.set_yticks(range(len(films)))
ax.set_yticklabels(films, fontsize=11)
ax.tick_params(axis='y', pad=10)

# Adjust layout to avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()