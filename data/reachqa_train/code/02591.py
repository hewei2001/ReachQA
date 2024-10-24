import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and the respective scores for each company
categories = ['SEO', 'Social Media', 'Content Quality', 'Email Marketing', 'Paid Advertising']
n_categories = len(categories)

# Data for each company
techsoft_scores = [7, 8, 6, 9, 5]
innovatech_scores = [6, 7, 8, 7, 9]
nextgen_scores = [8, 5, 7, 8, 6]

# Append the first score to the end to close the radar chart
techsoft_scores += techsoft_scores[:1]
innovatech_scores += innovatech_scores[:1]
nextgen_scores += nextgen_scores[:1]

# Calculate the angles for each category
angles = np.linspace(start=0, stop=2 * pi, num=n_categories, endpoint=False).tolist()
angles += angles[:1]  # Ensure the plot closes by repeating the first angle

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each company's data
ax.fill(angles, techsoft_scores, color='blue', alpha=0.25, label='TechSoft')
ax.plot(angles, techsoft_scores, color='blue', linewidth=2)

ax.fill(angles, innovatech_scores, color='red', alpha=0.25, label='Innovatech')
ax.plot(angles, innovatech_scores, color='red', linewidth=2)

ax.fill(angles, nextgen_scores, color='green', alpha=0.25, label='NextGen Solutions')
ax.plot(angles, nextgen_scores, color='green', linewidth=2)

# Add the category labels
plt.xticks(angles[:-1], categories, color='black', size=10)

# Adjust the radial limits
ax.set_ylim(0, 10)

# Add a title and a legend
plt.title('Digital Marketing Strategy Analysis\nComparative Performance Across Key Aspects', size=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Optimize layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()