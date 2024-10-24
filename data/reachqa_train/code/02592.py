import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and the respective scores for each company
categories = [
    'SEO', 'Social Media', 'Content Quality', 'Email Marketing', 
    'Paid Advertising', 'Market Analysis', 'Brand Awareness',
    'User Engagement', 'Lead Generation', 'Conversion Rate Optimization'
]

n_categories = len(categories)

# Weighted importance of each category (example weights)
weights = [1.2, 1.0, 1.1, 1.3, 0.9, 1.5, 1.4, 1.0, 1.3, 1.2]

# Data for each company, scaled with weights
techsoft_scores = [8, 7, 9, 6, 5, 9, 8, 7, 6, 9]
innovatech_scores = [7, 8, 7, 7, 9, 6, 8, 9, 7, 8]
nextgen_scores = [6, 9, 8, 8, 6, 7, 9, 6, 8, 7]

# Scale scores by weights
techsoft_scores = [score * weight for score, weight in zip(techsoft_scores, weights)]
innovatech_scores = [score * weight for score, weight in zip(innovatech_scores, weights)]
nextgen_scores = [score * weight for score, weight in zip(nextgen_scores, weights)]

# Append the first score to the end to close the radar chart
techsoft_scores += techsoft_scores[:1]
innovatech_scores += innovatech_scores[:1]
nextgen_scores += nextgen_scores[:1]

# Calculate the angles for each category
angles = np.linspace(start=0, stop=2 * pi, num=n_categories, endpoint=False).tolist()
angles += angles[:1]  # Ensure the plot closes by repeating the first angle

# Create radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each company's data with advanced styling
ax.fill(angles, techsoft_scores, color='blue', alpha=0.25, label='TechSoft')
ax.plot(angles, techsoft_scores, color='blue', linewidth=2, linestyle='--', marker='o')

ax.fill(angles, innovatech_scores, color='red', alpha=0.25, label='Innovatech')
ax.plot(angles, innovatech_scores, color='red', linewidth=2, linestyle='-', marker='x')

ax.fill(angles, nextgen_scores, color='green', alpha=0.25, label='NextGen Solutions')
ax.plot(angles, nextgen_scores, color='green', linewidth=2, linestyle='-.', marker='s')

# Add the category labels with better spacing for readability
plt.xticks(angles[:-1], categories, color='black', size=10)
ax.tick_params(axis='x', pad=10)  # Add padding to prevent text overlap

# Adjust the radial limits considering weighted scores
ax.set_ylim(0, 15)

# Add a title and a legend
plt.title('Digital Marketing Strategy Analysis\n'
          'Comparative Performance Across Key Aspects\n'
          'Weighted Score Evaluation', size=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Optimize layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()