import matplotlib.pyplot as plt
import numpy as np

# Define the centuries and mentions of islands
centuries = np.array([1300, 1350, 1400, 1450, 1500, 1550, 1600])
elusive_isle_mentions = [5, 8, 12, 10, 6, 4, 2]
mirage_land_mentions = [3, 4, 8, 14, 9, 5, 3]
phantom_archipelago_mentions = [1, 3, 6, 9, 11, 7, 5]

# Create a figure and axis
plt.figure(figsize=(12, 8))

# Plot each island's mentions over the centuries with distinct styles
plt.plot(centuries, elusive_isle_mentions, marker='o', linestyle='--', color='dodgerblue', linewidth=2, label='Elusive Isle')
plt.plot(centuries, mirage_land_mentions, marker='s', linestyle='-.', color='mediumseagreen', linewidth=2, label='Mirage Land')
plt.plot(centuries, phantom_archipelago_mentions, marker='^', linestyle='-', color='coral', linewidth=2, label='Phantom Archipelago')

# Add title and axis labels
plt.title("Chronicles of the Lost:\nMentions of Fabled Islands in Ancient Maps (1300-1600)", fontsize=16, fontweight='bold')
plt.xlabel("Century", fontsize=12)
plt.ylabel("Number of Mentions", fontsize=12)

# Set x-ticks with rotation for clarity
plt.xticks(centuries, [f"{cent}" for cent in centuries], rotation=45)

# Add legend to differentiate islands
plt.legend(title="Fabled Islands", loc='upper right', fontsize=10)

# Add grid for better readability
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Customize the background color for an ancient look
plt.gca().set_facecolor('#f5f5f5')

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()