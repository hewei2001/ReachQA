import matplotlib.pyplot as plt
import numpy as np

# Define the labels for the radar chart
labels = ['Architecture', 'Mathematics', 'Philosophy', 'Art', 'Warfare', 'Trade']
num_vars = len(labels)

# Data for each civilization
data_egypt = [9, 5, 4, 8, 7, 9]
data_greece = [7, 8, 9, 9, 6, 7]
data_china = [8, 9, 7, 7, 8, 10]

# Close the data loop for the radar chart
data_egypt += data_egypt[:1]
data_greece += data_greece[:1]
data_china += data_china[:1]

# Angles for each axis, including a repeat at the end to close the loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Enhance grid and axes
ax.spines['polar'].set_visible(False)
ax.set_yticks([2, 4, 6, 8])
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color='darkslategray', size=13)

# Draw ylabels with enhanced visibility
ax.set_yticklabels(["2", "4", "6", "8"], color='gray', size=10)
ax.set_ylim(0, 10)

# Define color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
markers = ['o', 's', '^']

# Plot data with enhancements for Egypt
ax.plot(angles, data_egypt, linewidth=2, linestyle='-', label='Egypt', color=colors[0], marker=markers[0])
ax.fill(angles, data_egypt, colors[0], alpha=0.15)

# Plot data with enhancements for Greece
ax.plot(angles, data_greece, linewidth=2, linestyle='-', label='Greece', color=colors[1], marker=markers[1])
ax.fill(angles, data_greece, colors[1], alpha=0.15)

# Plot data with enhancements for China
ax.plot(angles, data_china, linewidth=2, linestyle='-', label='China', color=colors[2], marker=markers[2])
ax.fill(angles, data_china, colors[2], alpha=0.15)

# Title and legend
plt.title('Cultural Contributions\nof Ancient Civilizations', size=18, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15), fontsize=12)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()