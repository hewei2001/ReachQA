import matplotlib.pyplot as plt
import numpy as np

# Data
genres = ['Pop', 'Rock', 'Hip-Hop/Rap', 'Electronic/Dance', 'Country', 'R&B', 'Classical', 'Jazz', 'Folk']
awards = [35, 28, 20, 18, 15, 12, 8, 7, 5]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot horizontal bar chart
ax.barh(genres, awards, height=0.5, color=plt.cm.tab20(range(len(genres))), edgecolor='black')

# Set title and labels
ax.set_title("Genre Breakdown of Grammy Award Winners: 2010-2020\n"
             "(Number of Awards in Each Genre)", fontsize=12, fontweight='bold')
ax.set_xlabel('Number of Awards')
ax.set_ylabel('Genre')

# Add value labels on the end of each bar
for i, value in enumerate(awards):
    ax.text(value + 1, i, f"  {value}", va='center', ha='left')

# Align category labels directly with the center of each bar
ax.tick_params(axis='y', which='both', length=0)
ax.yaxis.set_tick_params(pad=5)

# Add grid lines vertically
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add a vertical line to highlight the average awards
avg_awards = sum(awards) / len(awards)
ax.axvline(avg_awards, color='r', linestyle='dashed', linewidth=1, label='Average Awards')
ax.legend(loc='upper right')

# Automatically adjust the image layout
plt.tight_layout()

# Show the plot
plt.show()