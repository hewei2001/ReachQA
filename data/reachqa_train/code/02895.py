import matplotlib.pyplot as plt
import numpy as np

# Define the labels for the radar chart
labels = ['Strength', 'Agility', 'Intelligence', 'Magic', 'Stealth', 'Wisdom', 'Courage', 'Charisma']
num_vars = len(labels)

# Data for each mythical creature
data_dragon = [9, 4, 7, 10, 6, 8, 9, 7]
data_unicorn = [5, 8, 6, 9, 4, 7, 6, 8]
data_phoenix = [4, 6, 9, 8, 5, 7, 8, 6]
data_fairy = [3, 9, 5, 7, 10, 6, 5, 9]
data_gryphon = [8, 7, 6, 5, 7, 8, 7, 8]
data_mermaid = [7, 5, 7, 8, 6, 5, 9, 6]

# Close the data loop for the radar chart
data_dragon += data_dragon[:1]
data_unicorn += data_unicorn[:1]
data_phoenix += data_phoenix[:1]
data_fairy += data_fairy[:1]
data_gryphon += data_gryphon[:1]
data_mermaid += data_mermaid[:1]

# Angles for each axis, including a repeat at the end to close the loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Enhance grid and axes
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color='midnightblue', size=10)

# Draw ylabels with enhanced visibility
ax.set_yticklabels(["2", "4", "6", "8", "10"], color='darkgray', size=8)
ax.set_ylim(0, 10)

# Define color scheme and markers
colors = ['#ff5733', '#33d9b2', '#ff9f1a', '#3c40c6', '#f7b731', '#1f618d']
markers = ['o', 's', 'D', '^', 'P', 'X']

# Plot data for each creature with enhancements
ax.plot(angles, data_dragon, linewidth=2, linestyle='-', label='Dragon', color=colors[0], marker=markers[0])
ax.fill(angles, data_dragon, colors[0], alpha=0.15)

ax.plot(angles, data_unicorn, linewidth=2, linestyle='-', label='Unicorn', color=colors[1], marker=markers[1])
ax.fill(angles, data_unicorn, colors[1], alpha=0.15)

ax.plot(angles, data_phoenix, linewidth=2, linestyle='-', label='Phoenix', color=colors[2], marker=markers[2])
ax.fill(angles, data_phoenix, colors[2], alpha=0.15)

ax.plot(angles, data_fairy, linewidth=2, linestyle='-', label='Fairy', color=colors[3], marker=markers[3])
ax.fill(angles, data_fairy, colors[3], alpha=0.15)

ax.plot(angles, data_gryphon, linewidth=2, linestyle='-', label='Gryphon', color=colors[4], marker=markers[4])
ax.fill(angles, data_gryphon, colors[4], alpha=0.15)

ax.plot(angles, data_mermaid, linewidth=2, linestyle='-', label='Mermaid', color=colors[5], marker=markers[5])
ax.fill(angles, data_mermaid, colors[5], alpha=0.15)

# Title and legend
plt.title('Comparative Analysis of Mythical Creatures\' Qualities\nAcross Different Attributes', size=14, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=9)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()