import matplotlib.pyplot as plt
import numpy as np

# Define the categories and corresponding data
categories = ['Nutritional Algae', 'Medicinal Plants', 'Exotic Fish', 'Rare Minerals', 'Renewable Energy Sources']
num_categories = len(categories)

# Scores for each ocean's resource richness
pacific_scores = [8, 7, 9, 6, 5]
atlantic_scores = [6, 8, 7, 7, 6]
indian_scores = [7, 6, 5, 8, 7]

# Calculate angles for each category
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

# Complete the loop for radar chart by adding the starting category again at the end
pacific_scores += pacific_scores[:1]
atlantic_scores += atlantic_scores[:1]
indian_scores += indian_scores[:1]
angles += angles[:1]

# Initialize the radar chart with polar coordinates
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each ocean's data on the radar chart
ax.plot(angles, pacific_scores, color='blue', linewidth=2, label='Pacific Ocean')
ax.fill(angles, pacific_scores, color='blue', alpha=0.25)

ax.plot(angles, atlantic_scores, color='green', linewidth=2, label='Atlantic Ocean')
ax.fill(angles, atlantic_scores, color='green', alpha=0.25)

ax.plot(angles, indian_scores, color='red', linewidth=2, label='Indian Ocean')
ax.fill(angles, indian_scores, color='red', alpha=0.25)

# Add category labels to each spoke
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Add a descriptive title
plt.title("Flavors of the Ocean:\nA Radar Exploration of Oceanic Resources", fontsize=16, fontweight='bold', pad=20)

# Add legend to differentiate the oceans
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=10)

# Enhance layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()