import matplotlib.pyplot as plt
import numpy as np

# Define data
professions = ['Software Devs', 'Doctors', 'Teachers', 'Artists']
work = [50, 60, 45, 35]
leisure = [20, 15, 25, 30]
other = [30, 25, 30, 35]

# Convert data to be used in a stacked horizontal bar chart
data = np.array([work, leisure, other])
labels = ['Work', 'Leisure', 'Other Activities']
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))

# Create stacked horizontal percentage bar chart
for i in range(len(labels)):
    ax.barh(professions, data[i], left=np.sum(data[:i], axis=0), color=colors[i], label=labels[i])

# Title and labels
ax.set_title('Work-Life Balance Across Professions', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Percentage of Time (%)', fontsize=12)
ax.set_xlim(0, 100)

# Add data labels inside the bars
for i, (category, color) in enumerate(zip(labels, colors)):
    for j in range(len(professions)):
        x = np.sum(data[:i+1, j]) - data[i, j]/2
        ax.text(x, j, f'{data[i, j]}%', va='center', ha='center', fontsize=10, color='white', fontweight='bold')

# Customizing the legend
ax.legend(title='Activity Type', loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()