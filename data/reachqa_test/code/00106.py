import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.colors import LinearSegmentedColormap

# Define labels and data
labels = ['Range', 'Precision', 'Autonomy', 'Durability', 'Cost-Effectiveness']
technologies = ['Sonar Imaging', 'ROVs', 'AUVs', 'Subsea Comm', 'Deep-Sea Sampling']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

sonar_imaging = [8, 7, 3, 8, 5]
rovs = [6, 8, 5, 9, 6]
auvs = [7, 6, 8, 7, 5]
subsea_comm = [5, 5, 4, 7, 8]
deep_sea_sampling = [4, 7, 6, 8, 7]

data = np.array([sonar_imaging, rovs, auvs, subsea_comm, deep_sea_sampling])
num_vars = len(labels)

# Prepare angles and complete the loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

# Create radar chart with improved layout
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Configure grid and background
ax.set_facecolor('#f7f9f9')
gridlines = np.linspace(0, 10, 6)[1:]
ax.set_yticks(gridlines)
ax.set_yticklabels(map(str, gridlines), color='gray', size=8)
ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
ax.xaxis.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

# Plot each technology
for i, (tech, color) in enumerate(zip(technologies, colors)):
    ax.plot(angles, data[i], label=tech, color=color, linewidth=2, linestyle='--')
    ax.fill(angles, data[i], color=color, alpha=0.15, edgecolor=color)

# Add concentric circles for scale indication
for radius in gridlines:
    ax.add_patch(Circle((0, 0), radius, transform=ax.transData._b, color='gray', fill=False, linewidth=0.5, alpha=0.3))

# Highlight specific data points
for i, (tech, color) in enumerate(zip(technologies, colors)):
    for angle, value in zip(angles, data[i]):
        ax.plot(angle, value, 'o', color=color)

# Setup axis labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12, fontweight='bold', color='black')
ax.set_ylim(0, 10)

# Enhance title and legend
title = 'Comparative Analysis\nof Underwater Exploration Technologies'
plt.title(title, size=16, color='navy', pad=40, fontweight='bold', horizontalalignment='center')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, frameon=True, framealpha=0.3)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()