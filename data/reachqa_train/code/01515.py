import matplotlib.pyplot as plt
import numpy as np

# Define music genres
genres = ["Electronic", "Jazz", "Classical", "Pop", "Rock", "Final Total"]

# Audience votes for each genre, with the final total computed manually
votes = [150, 180, -60, 200, -90, 120]

# Calculate cumulative votes at each step
cumulative = np.cumsum([0] + votes[:-1])
end_values = cumulative + votes

# Colors to represent positive and negative changes
colors = ["#66b3ff" if val >= 0 else "#ff9999" for val in votes]

# Plotting the Waterfall Chart
fig, ax = plt.subplots(figsize=(12, 7))

# Create bars and plot connectors
for i in range(len(votes)):
    # Draw bar for current genre
    ax.bar(genres[i], votes[i], bottom=cumulative[i], color=colors[i], edgecolor='black')
    # Connectors for visualization
    if i < len(votes) - 1:
        ax.plot([i, i + 1], [end_values[i], end_values[i]], color='black', linewidth=1.5)

# Title and labels
ax.set_title("Synth Symphony:\nEvolution of Genres in the Robotic Music Festival (2030)",
             fontsize=14, weight='bold', pad=20)
ax.set_ylabel("Audience Votes (in thousands)", fontsize=12)
ax.set_xlabel("Music Genre", fontsize=12)

# Add total labels above each bar
for i, total in enumerate(end_values):
    ax.text(i, total + (5 if votes[i] >= 0 else -10), f'{total}', ha='center', 
            va='bottom' if votes[i] >= 0 else 'top', fontsize=10, color='black')

# Improve x-axis label visibility
plt.xticks(rotation=45, ha="right")

# Add grid for better readability
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.6)

# Make layout fit within the canvas
plt.tight_layout()

# Display the plot
plt.show()