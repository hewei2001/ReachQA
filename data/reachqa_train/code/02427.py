import matplotlib.pyplot as plt
import numpy as np

# Define the categories for superhero powers
categories = ['Strength', 'Speed', 'Intelligence', 'Durability', 'Energy Projection', 'Combat Skills']
n_categories = len(categories)

# Superhero data: scores from 1 to 10
superman = [10, 9, 7, 10, 10, 8]
batman = [4, 6, 10, 4, 2, 10]
wonder_woman = [8, 7, 7, 9, 7, 9]
flash = [4, 10, 6, 5, 6, 7]
green_lantern = [6, 7, 8, 6, 9, 8]

# Combine all data
hero_data = np.array([superman, batman, wonder_woman, flash, green_lantern])

labels = ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Green Lantern']

# Prepare angles for the radar chart
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
hero_data = np.concatenate((hero_data, hero_data[:, [0]]), axis=1)  # Close the radar chart loop
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Radar chart plotting function
def plot_radar(ax, data, colors):
    for idx, d in enumerate(data):
        ax.fill(angles, d, color=colors[idx], alpha=0.25, label=labels[idx])
        ax.plot(angles, d, color=colors[idx], linewidth=2)

# Plot radar chart
colors = ['#ff5733', '#334fff', '#28a745', '#ffc107', '#17a2b8']
plot_radar(ax, hero_data, colors)

# Configure radar chart details
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, fontweight='bold', ha='center')
ax.set_yticklabels([])
ax.set_title('Superhero Powers Analysis\nComparative Chart of Iconic Heroes', size=14, fontweight='bold', pad=30)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=9)

# Automatically adjust the subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()