import numpy as np
import matplotlib.pyplot as plt

# Define the categories and skill values for the radar chart
categories = ['Market Analysis', 'Risk Management', 'Innovation', 
              'Customer Service', 'Financial Stability', 
              'Data Security', 'Blockchain Utilization', 
              'AI Integration', 'Regulatory Compliance']
num_categories = len(categories)

# Skill scores for two different entities
entity_1_values = [8, 7, 9, 6, 8, 7, 8, 9, 6]
entity_2_values = [7, 8, 6, 7, 9, 8, 7, 6, 8]

# Repeat the first value to close the radar chart loop
entity_1_values += entity_1_values[:1]
entity_2_values += entity_2_values[:1]

# Calculate angle for each axis
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

# Set up the figure and polar plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Add category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='navy', size=9)

# Use non-linear scale with a custom transformation for challenging interpretation
ax.set_rscale('log')
ax.yaxis.set_ticks([1, 3, 5, 7, 10])
ax.yaxis.set_ticklabels(["1", "3", "5", "7", "10"])
ax.set_ylim(1, 10)

# Plot the data for both entities
ax.plot(angles, entity_1_values, linewidth=1.5, linestyle='solid', label="FinTech Innovations: Entity A", color='cyan')
ax.fill(angles, entity_1_values, color='cyan', alpha=0.25)

ax.plot(angles, entity_2_values, linewidth=1.5, linestyle='solid', label="FinTech Innovations: Entity B", color='orange')
ax.fill(angles, entity_2_values, color='orange', alpha=0.25)

# Add a title and legend
plt.title("Comparative Analysis of Strategic Skills\nAcross Different Entities in FinTech", size=14, fontweight='bold', va='bottom', ha='center', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=9)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()