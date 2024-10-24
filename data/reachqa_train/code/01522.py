import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Culinary skill categories
categories = ['Knife Skills', 'Baking', 'Plating', 'Sauce Making', 'Food Safety', 'Creativity']
n_categories = len(categories)

# Chef proficiency data
chef_alex = [8, 6, 7, 9, 7, 6]
chef_jamie = [7, 7, 8, 6, 8, 9]
chef_taylor = [6, 8, 6, 8, 7, 7]

# Arrange data to form a complete circle by adding the first point at the end
data = np.array([chef_alex, chef_jamie, chef_taylor])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Calculate the angle for each category
angles = np.linspace(0, 2 * pi, n_categories, endpoint=False).tolist()
angles += angles[:1]  # Close the radar chart

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each chef's data
ax.plot(angles, data[0], label='Chef Alex', linewidth=2, linestyle='-', marker='o', color='b')
ax.plot(angles, data[1], label='Chef Jamie', linewidth=2, linestyle='-', marker='s', color='g')
ax.plot(angles, data[2], label='Chef Taylor', linewidth=2, linestyle='-', marker='^', color='r')

# Fill area for better visualization
ax.fill(angles, data[0], color='b', alpha=0.1)
ax.fill(angles, data[1], color='g', alpha=0.1)
ax.fill(angles, data[2], color='r', alpha=0.1)

# Customize the chart
ax.set_yticks(range(1, 11))
ax.set_yticklabels(map(str, range(1, 11)), fontsize=10, color='grey')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Add a title
plt.title('Culinary Skills Assessment\nfor Aspiring Chefs at Gourmet Academy', fontsize=14, pad=30)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10, title='Chefs')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the radar chart
plt.show()