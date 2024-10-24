import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from math import pi

# Skill categories
categories = ['Programming', 'Mathematics', 'Domain Expertise', 'Communication', 'Data Wrangling', 'Machine Learning']

# Number of categories
N = len(categories)

# Create data for each emerging data scientist (1-10 scale)
Alex_skills = [8, 6, 7, 5, 9, 7]
Bailey_skills = [7, 7, 6, 8, 8, 8]
Casey_skills = [6, 8, 8, 6, 7, 9]

# Combine the data and ensure the radar chart is closed
data = np.array([Alex_skills, Bailey_skills, Casey_skills])

# Define angles for the radar chart
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()

# The plot is a circle, so we need to complete the loop
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Draw one layer per data scientist
labels = ['Alex', 'Bailey', 'Casey']
colors = ['#FF6347', '#4682B4', '#32CD32']

for d, color, label in zip(data, colors, labels):
    ax.fill(angles, d, color=color, alpha=0.25, label=label)
    ax.plot(angles, d, color=color, linewidth=2)

# Add skill categories as labels
plt.xticks(angles[:-1], categories, color='grey', size=12)

# Set the range for each axis
ax.set_ylim(0, 10)

# Add a title
plt.title('Skills Composition of Emerging Data Scientists\n2023', size=16, color='darkslategray', y=1.1, fontweight='bold')

# Add a legend
legend_elements = [Patch(facecolor='#FF6347', edgecolor='#FF6347', label='Alex'),
                   Patch(facecolor='#4682B4', edgecolor='#4682B4', label='Bailey'),
                   Patch(facecolor='#32CD32', edgecolor='#32CD32', label='Casey')]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, frameon=False, title='Data Scientist')

# Customize the grid
ax.yaxis.grid(True, color='lightgrey', linestyle='--', linewidth=0.75)
ax.xaxis.grid(True, color='lightgrey', linestyle='--', linewidth=0.75)

# Enhance visibility of data points
ax.tick_params(axis='both', which='major', labelsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()