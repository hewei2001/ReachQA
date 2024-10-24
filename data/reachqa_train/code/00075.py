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
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color='grey', size=12)

# Draw ylabels
plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color='grey', size=10)
plt.ylim(0, 10)

# Plot data and fill area for Egypt
ax.plot(angles, data_egypt, linewidth=2, linestyle='solid', label='Egypt', color='blue')
ax.fill(angles, data_egypt, 'blue', alpha=0.1)

# Plot data and fill area for Greece
ax.plot(angles, data_greece, linewidth=2, linestyle='solid', label='Greece', color='red')
ax.fill(angles, data_greece, 'red', alpha=0.1)

# Plot data and fill area for China
ax.plot(angles, data_china, linewidth=2, linestyle='solid', label='China', color='green')
ax.fill(angles, data_china, 'green', alpha=0.1)

# Title and legend
plt.title('Cultural Contributions of Ancient Civilizations', size=16, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()