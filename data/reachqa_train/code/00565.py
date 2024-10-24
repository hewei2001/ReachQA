import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Define categories and data
categories = ['Agriculture', 'Architecture', 'Military', 'Education', 'Trade']
num_categories = len(categories)

# Define resource allocations
mesopotamians = [35, 25, 15, 10, 15]
egyptians = [40, 30, 10, 10, 10]
indus_valley = [25, 20, 15, 20, 20]
mayans = [30, 20, 25, 15, 10]
chinese = [20, 25, 20, 25, 10]

# Extend to close radar loop
civilizations = [mesopotamians, egyptians, indus_valley, mayans, chinese]
for civ in civilizations:
    civ.append(civ[0])

# Calculate average allocation per category
average_allocation = np.mean(civilizations, axis=0)[:-1]

# Create angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

# Set up the figure and the GridSpec layout
fig = plt.figure(figsize=(14, 7))
gs = GridSpec(1, 2, figure=fig)

# Radar chart subplot
ax1 = fig.add_subplot(gs[0, 0], polar=True)
colors = ['darkorange', 'forestgreen', 'royalblue', 'crimson', 'purple']
labels = ['Mesopotamians', 'Egyptians', 'Indus Valley', 'Mayans', 'Chinese']

for i, civ in enumerate(civilizations):
    ax1.plot(angles, civ, color=colors[i], linewidth=2, label=labels[i])
    ax1.fill(angles, civ, color=colors[i], alpha=0.25)

ax1.set_yticklabels([])
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=11, color='gray')
ax1.set_title("Resource Allocation of Ancient Civilizations\nAcross Key Development Domains", size=14, fontweight='bold', pad=20)
ax1.legend(loc='upper right', bbox_to_anchor=(1.4, 1.1))

# Bar chart subplot for average allocation
ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(categories, average_allocation, color='c', alpha=0.6)
ax2.set_title("Average Resource Allocation\nAcross Civilizations", fontsize=14, fontweight='bold')
ax2.set_ylabel("Average Percentage")
ax2.set_ylim(0, max(average_allocation) + 5)
ax2.set_xticklabels(categories, rotation=45, ha='right')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()