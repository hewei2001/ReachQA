import numpy as np
import matplotlib.pyplot as plt

# Categories for the radar chart
categories = ['Camera', 'Battery', 'Display', 'Performance', 'Durability']

# Ratings for each smartphone model
smartphone_a = [9, 8, 9, 8, 7]  # Smartphone A ratings
smartphone_b = [8, 9, 8, 9, 6]  # Smartphone B ratings
smartphone_c = [7, 7, 8, 7, 8]  # Smartphone C ratings

# Number of variables
num_vars = len(categories)

# Compute the angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for the radar chart
ratings_a = smartphone_a + smartphone_a[:1]
ratings_b = smartphone_b + smartphone_b[:1]
ratings_c = smartphone_c + smartphone_c[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill areas and plot lines
ax.fill(angles, ratings_a, color='skyblue', alpha=0.4, label='Smartphone A')
ax.plot(angles, ratings_a, color='skyblue', linewidth=2)

ax.fill(angles, ratings_b, color='salmon', alpha=0.4, label='Smartphone B')
ax.plot(angles, ratings_b, color='salmon', linewidth=2)

ax.fill(angles, ratings_c, color='limegreen', alpha=0.4, label='Smartphone C')
ax.plot(angles, ratings_c, color='limegreen', linewidth=2)

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='black')

# Hide the radial labels and set the limit
ax.set_yticklabels([])
ax.set_ylim(0, 10)

# Title and legend
plt.title('Tech Savvy: Evaluating Key Features of Next-Gen Smartphones', 
          fontsize=16, fontweight='bold', pad=20, multialignment='center')
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Adjust layout for better readability
plt.tight_layout()

# Display the radar chart
plt.show()