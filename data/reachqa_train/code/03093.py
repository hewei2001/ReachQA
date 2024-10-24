import matplotlib.pyplot as plt
import numpy as np

# Define categories for the radar chart
categories = ['Health & Fitness', 'Career Satisfaction', 'Family & Relationships', 
              'Hobbies & Leisure', 'Personal Development']

# Fictional scores representing an individual's perceived balance
scores = [7, 6, 8, 5, 7]  # Keep scores between 0 and 10

# Calculate number of categories
num_vars = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop by adding the start value at the end
scores += scores[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill the area and plot line
ax.fill(angles, scores, color='skyblue', alpha=0.4)
ax.plot(angles, scores, color='blue', linewidth=2)

# Customize the radar chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='darkslategray')

# Add a title
ax.set_title('Personal Well-being and Life Balance\nAssessment Radar Chart', 
             fontsize=16, color='darkslateblue', weight='bold', pad=20)

# Show radial labels and make grid lines visible
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Add labels for each score
for i, score in enumerate(scores[:-1]):
    ax.text(angles[i], score + 0.3, f'{score}', horizontalalignment='center', fontsize=11, color='darkblue')

# Adjust layout to prevent any overlap
plt.tight_layout()

# Display the plot
plt.show()