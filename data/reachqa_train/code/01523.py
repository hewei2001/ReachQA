import matplotlib.pyplot as plt

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

# Color scheme for the bars
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(films, votes, color=colors, height=0.5, edgecolor='grey')

# Set title and labels
ax.set_title("Fictional Film Awards 2023: Best Film Category\nVotes Received by Nominees",
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Number of Votes", fontsize=12)
ax.set_ylabel("Films", fontsize=12)

# Adding data labels to the bars
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width:,}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),  # 3 points horizontal offset
                textcoords="offset points",
                ha='left', va='center', fontsize=10, color='black')

# Customize the ticks and grid
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax.xaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(0, max(votes) + 500)

# Ensure labels are clear and aligned
ax.set_yticks(range(len(films)))
ax.set_yticklabels(films, fontsize=11)
ax.tick_params(axis='y', pad=10)

# Adjust layout to avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()