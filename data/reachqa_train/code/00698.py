import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import LinearSegmentedColormap

# Skill categories
categories = ['Technical Expertise', 'Communication', 'Problem Solving', 'Teamwork', 'Leadership']

# Number of variables
num_vars = len(categories)

# Skill levels for each department
R_and_D = [9, 7, 8, 6, 5]
Product_Dev = [8, 6, 9, 7, 6]
Marketing = [6, 8, 7, 9, 7]
Customer_Support = [5, 9, 6, 8, 7]
Sales = [7, 8, 7, 7, 8]

# Combine all data into one array and append the first value to the end to close the radar chart
values = np.array([R_and_D, Product_Dev, Marketing, Customer_Support, Sales])
values = np.concatenate([values, values[:, [0]]], axis=1)

# Calculate angles for the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create custom color map for gradients
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', ['#97C8EB', '#023E8A'])

# Setup the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Add the background gradient
ax.set_facecolor((0.95, 0.95, 0.95))

# Title
plt.title('Skill Set Analysis\nby Department at Tech Innovations Corp.', size=14, weight='bold', pad=20, color='#1a1a1a')

# Plot each department's data with gradients and markers
departments = ['R&D', 'Product Development', 'Marketing', 'Customer Support', 'Sales']
colors = ['#4682B4', '#32CD32', '#FFA500', '#FF4500', '#800080']
markers = ['o', 's', 'd', '^', '*']

for i, (values_row, color, marker) in enumerate(zip(values, colors, markers)):
    ax.plot(angles, values_row, linewidth=2, linestyle='solid', label=departments[i], color=color, marker=marker)
    ax.fill(angles, values_row, color=color, alpha=0.15, edgecolor=None)

# Customizing the grid lines
ax.yaxis.grid(True, color='grey', linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, color='grey', linestyle='--', linewidth=0.5)

# Set axis labels and radial ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, weight='bold', color='#1a1a1a')
ax.set_yticklabels([])

# Create custom legend
legend_elements = [Patch(facecolor=color, edgecolor='w', label=department, alpha=0.7) for color, department in zip(colors, departments)]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()