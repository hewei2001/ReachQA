import matplotlib.pyplot as plt
import numpy as np

# Mythical creatures and their folklore popularity scores
creatures = ['Dragons', 'Phoenix', 'Unicorns', 'Kraken', 'Griffins', 'Mermaids', 'Minotaurs']
popularity_scores = [85, 70, 90, 60, 75, 65, 55]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Generate positions for each bar on the x-axis
x_pos = np.arange(len(creatures))

# Plot the bars
bars = ax.bar(x_pos, popularity_scores, color=['#FF5733', '#FFC300', '#FF33FF', '#33DFFF', '#DAF7A6', '#33FF57', '#8E44AD'], edgecolor='black')

# Set the title and labels
ax.set_title("Ancient Mythical Creatures\nFolklore Legend Popularity", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Mythical Creatures", fontsize=13)
ax.set_ylabel("Popularity Score (Out of 100)", fontsize=13)

# Customize x-axis tick labels and rotate them for better readability
ax.set_xticks(x_pos)
ax.set_xticklabels(creatures, fontsize=11, rotation=30, ha='right')

# Annotate each bar with its popularity score
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Offset text by 3 units vertically
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='white')

# Add grid lines along the y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust y-axis limits to give space for annotations
ax.set_ylim(0, 100)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()