import matplotlib.pyplot as plt
import numpy as np

# Define skill categories
categories = ['Research Skills', 'Analytical Thinking', 'Writing Proficiency', 'Source Criticism', 'Cultural Understanding']
N = len(categories)

# Define skill levels for each historian
historian_a = [8, 7, 6, 9, 5]
historian_b = [6, 9, 7, 6, 8]

# Close the loop by repeating the first value
historian_a += historian_a[:1]
historian_b += historian_b[:1]

# Calculate angles for each category
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot data for Historian A
ax.fill(angles, historian_a, color='blue', alpha=0.25, label='Historian A')
ax.plot(angles, historian_a, color='blue', linewidth=2)

# Plot data for Historian B
ax.fill(angles, historian_b, color='green', alpha=0.25, label='Historian B')
ax.plot(angles, historian_b, color='green', linewidth=2)

# Add category labels to the plot
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='darkslategray', wrap=True)

# Title and legend
plt.title('Skills Competency Radar in Historical Analysis', fontsize=15, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Adjust layout to ensure everything fits
plt.tight_layout()

# Display the chart
plt.show()