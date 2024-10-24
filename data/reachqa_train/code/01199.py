import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Wind intensity data for each island in arbitrary units
aeolus_winds = np.array([20, 35, 50, 30])
zephyros_winds = np.array([25, 40, 55, 35])
boreas_winds = np.array([30, 45, 65, 50])
notus_winds = np.array([15, 25, 35, 20])
eurus_winds = np.array([10, 30, 40, 25])

# Key milestone annotations
annotations = {
    (0, 30): "Summer Peak\non Eurus",
    (1, 55): "Autumn Storm\non Boreas",
    (2, 50): "Winter Calm\non Aeolus",
    (3, 35): "Winter Surge\non Zephyros"
}

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each island's data with different styles and markers
ax.plot(seasons, aeolus_winds, marker='o', linestyle='-', color='c', linewidth=2, label='Aeolus')
ax.plot(seasons, zephyros_winds, marker='s', linestyle='--', color='m', linewidth=2, label='Zephyros')
ax.plot(seasons, boreas_winds, marker='^', linestyle='-.', color='r', linewidth=2, label='Boreas')
ax.plot(seasons, notus_winds, marker='D', linestyle=':', color='g', linewidth=2, label='Notus')
ax.plot(seasons, eurus_winds, marker='*', linestyle='-', color='b', linewidth=2, label='Eurus')

# Annotate significant milestones
for (x, y), label in annotations.items():
    ax.annotate(label,
                (seasons[x], y),
                textcoords="offset points",
                xytext=(0, 10),
                ha='center',
                fontsize=9,
                arrowprops=dict(arrowstyle='->', color='gray'))

# Setting up the labels and title
ax.set_title("Harmony of the Winds:\nSeasonal Breeze Patterns Across Fictional Islands", fontsize=14, fontweight='bold')
ax.set_xlabel("Season", fontsize=12)
ax.set_ylabel("Wind Intensity (Arbitrary Units)", fontsize=12)

# Customizing the grid and legends
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Adjust layout to fit text
plt.tight_layout()

# Display the chart
plt.show()