import matplotlib.pyplot as plt
import numpy as np

# Data setup
activities = ['Relaxing', 'Exercising', 'Socializing', 'Working', 'Others']
data = np.array([
    [35, 20, 15, 20, 10],  # Group 1
    [25, 15, 30, 20, 10],  # Group 2
    [30, 25, 20, 15, 10],  # Group 3
    [40, 15, 10, 25, 10],  # Group 4
])
average_data = np.mean(data, axis=0)

groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Stacked Bar Chart (subplot 1)
bottoms = np.zeros(data.shape[0])
for i, (activity, color) in enumerate(zip(activities, colors)):
    bars = ax1.bar(groups, data[:, i], bottom=bottoms, label=activity, color=color)
    bottoms += data[:, i]
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax1.text(
                bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2, f'{int(height)}%',
                ha='center', va='center', color='black', fontsize=10, fontweight='bold'
            )

ax1.set_title('Weekend Activity Distribution\nAcross Different Groups', fontsize=14, weight='bold', pad=15)
ax1.set_xlabel('Groups', fontsize=12)
ax1.set_ylabel('Percentage of Time (%)', fontsize=12)
ax1.set_yticks(np.arange(0, 101, 10))
ax1.legend(title='Activities', bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_xticks(range(len(groups)))
ax1.set_xticklabels(groups, fontsize=11)

# Pie Chart for Average Data (subplot 2)
wedges, texts, autotexts = ax2.pie(
    average_data, labels=activities, autopct='%1.1f%%', startangle=140, colors=colors
)
for text in texts + autotexts:
    text.set_size(11)

ax2.set_title('Average Activity Distribution\nAcross All Groups', fontsize=14, weight='bold', pad=15)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()