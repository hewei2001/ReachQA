import matplotlib.pyplot as plt
import numpy as np

# Define data
professions = ['Software Devs', 'Doctors', 'Teachers', 'Artists']
work = np.array([50, 60, 45, 35])
leisure = np.array([20, 15, 25, 30])
other = np.array([30, 25, 30, 35])

# Calculate additional data
total_time = np.array([np.sum(work), np.sum(leisure), np.sum(other)])
labels = ['Work', 'Leisure', 'Other Activities']
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Setup subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 1: Stacked Horizontal Bar Chart
axs[0].set_title('Work-Life Balance Across Professions', fontsize=14, fontweight='bold')
for i in range(len(labels)):
    axs[0].barh(professions, [work, leisure, other][i], 
                left=np.sum([work, leisure, other][:i], axis=0),
                color=colors[i], label=labels[i])

# Add labels and limits
axs[0].set_xlabel('Percentage of Time (%)', fontsize=12)
axs[0].set_xlim(0, 100)
for i, color in enumerate(colors):
    for j in range(len(professions)):
        x = np.sum([work, leisure, other][:i+1], axis=0)[j] - [work, leisure, other][i][j]/2
        axs[0].text(x, j, f'{[work, leisure, other][i][j]}%', va='center', ha='center', 
                    fontsize=10, color='white', fontweight='bold')
axs[0].legend(title='Activity Type', loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize=10)

# Subplot 2: Pie Chart for Overall Distribution
axs[1].set_title('Overall Time Distribution', fontsize=14, fontweight='bold')
axs[1].pie(total_time, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, 
           wedgeprops=dict(edgecolor='w'))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()