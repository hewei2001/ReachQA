import matplotlib.pyplot as plt
import numpy as np

# Define the explorer's activities and their corresponding time allocations in hours
activities = ['Navigation', 'Documentation', 'Discovery', 'Rest', 'Social Interaction']
time_allocation = {
    'Explorer A': [3, 2, 5, 8, 6],
    'Explorer B': [4, 3, 4, 7, 6],
    'Explorer C': [2, 4, 6, 8, 4]
}

# Number of variables and angles for the radar chart
num_vars = len(activities)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart is a circular chart, so we need to "close the loop"
activities += activities[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each explorer's time allocation
colors = ['#FF6347', '#4682B4', '#32CD32']
for i, (explorer, allocation) in enumerate(time_allocation.items()):
    allocation += allocation[:1]  # Complete the loop
    ax.plot(angles, allocation, linewidth=2, linestyle='solid', label=explorer, color=colors[i])
    ax.fill(angles, allocation, color=colors[i], alpha=0.25)

# Adjust the labels for each axis
ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels(activities, fontsize=12, fontweight='bold')

# Title and legend
plt.title("A Day in the Life of a Modern Explorer\nTime Allocation Across Activities", 
          size=14, color='darkgreen', weight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Explorers')

# Automatically adjust the layout to prevent label and title clipping
plt.tight_layout()

# Show the radar chart
plt.show()