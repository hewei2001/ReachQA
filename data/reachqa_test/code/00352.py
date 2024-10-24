import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data
age_groups = ['18-20', '21-23', '24-26', '27-29', '30-32']
fields = ['History', 'Philosophy', 'Psychology', 'Sociology', 'Linguistics']

history = [25, 30, 28, 22, 20]
philosophy = [15, 18, 20, 25, 22]
psychology = [30, 32, 35, 30, 28]
sociology = [20, 22, 25, 28, 30]
linguistics = [10, 12, 15, 18, 20]

data = np.array([history, philosophy, psychology, sociology, linguistics])

# Create figure and axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a grid of X and Y coordinates
x = np.arange(len(age_groups))
y = np.arange(len(fields))
x, y = np.meshgrid(x, y)

# Plot the bars
width = 0.5
depth = 0.5
bar_colors = plt.cm.tab20(np.linspace(0, 1, len(fields)))
for i in range(len(fields)):
    for j in range(len(age_groups)):
        ax.bar3d(x[j], y[i], 0, width, depth, data[i, j], color=bar_colors[i])

# Set axis labels and title
ax.set_xlabel('Age Groups')
ax.set_ylabel('Fields of Social Sciences and Humanities')
ax.set_zlabel('Percentage of Students')
ax.set_title("Pursuit of Social Sciences and Humanities:\nAge-wise Distribution of Students\n(Bar colors represent different fields)")

# Normalize the Z-axis to a 0-100 scale
ax.set_zlim(0, 100)

# Adjust the x-axis labels to avoid overlapping
plt.xticks(range(len(age_groups)), age_groups, rotation=45, ha='right')

# Experiment with different viewing angles and lighting conditions
ax.view_init(elev=30, azim=60)

# Add a legend for the bar colors
legend_labels = ['{} ({})'.format(field, score) for field, score in zip(fields, data[:, 0])]
legend_handles = [plt.Line2D([0], [0], marker='s', color='w', label=label, markerfacecolor=bar_colors[i], markersize=12) for i, label in enumerate(legend_labels)]
plt.legend(handles=legend_handles, loc='upper right', bbox_to_anchor=(1.15, 1), title="Fields (Initial Score)")

# Show the plot
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()