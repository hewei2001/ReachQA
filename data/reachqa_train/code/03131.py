import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define metrics
metrics = ['Strength', 'Endurance', 'Flexibility', 'Balance', 'Nutrition', 'Mental Well-being']

# Example data
ideal_plan = [8, 8, 8, 8, 8, 8]
current_plan = [6, 7, 5, 9, 6, 7]

# Number of variables
num_vars = len(metrics)

# Compute angle for each variable
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop
ideal_plan += ideal_plan[:1]
current_plan += current_plan[:1]
angles += angles[:1]

# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], metrics, color='grey', size=12)

# Draw y-labels
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Plot the data
ax.plot(angles, ideal_plan, color='teal', linewidth=2, linestyle='dashed', label='Ideal Plan')
ax.fill(angles, ideal_plan, color='teal', alpha=0.1)

ax.plot(angles, current_plan, color='orange', linewidth=2, linestyle='solid', label='Current Plan')
ax.fill(angles, current_plan, color='orange', alpha=0.25)

# Add a title
plt.title("Balanced Fitness Regimen: Evaluating Wellness Metrics", size=16, color='black', weight='bold', pad=20)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.05))

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()