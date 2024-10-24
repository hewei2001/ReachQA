import matplotlib.pyplot as plt
import numpy as np

# Define additional categories to increase complexity
categories = [
    'Nutritional Algae', 'Medicinal Plants', 'Exotic Fish', 'Rare Minerals', 'Renewable Energy Sources',
    'Biodiversity', 'Coral Reefs', 'Underwater Vents', 'Marine Life Habitats', 'Sea Temperature Variability'
]

num_categories = len(categories)

# Scores for each ocean's resource richness, plus a new ocean: Arctic Ocean
pacific_scores = [8, 7, 9, 6, 5, 8, 7, 6, 7, 5]
atlantic_scores = [6, 8, 7, 7, 6, 6, 5, 8, 7, 6]
indian_scores = [7, 6, 5, 8, 7, 5, 7, 7, 6, 8]
arctic_scores = [6, 5, 6, 7, 8, 5, 8, 6, 5, 7]

# Complete the loop for radar chart by adding the starting category again at the end
pacific_scores += pacific_scores[:1]
atlantic_scores += atlantic_scores[:1]
indian_scores += indian_scores[:1]
arctic_scores += arctic_scores[:1]
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart with polar coordinates
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each ocean's data on the radar chart
ax.plot(angles, pacific_scores, color='blue', linewidth=2, label='Pacific Ocean')
ax.fill(angles, pacific_scores, color='blue', alpha=0.25)

ax.plot(angles, atlantic_scores, color='green', linewidth=2, label='Atlantic Ocean')
ax.fill(angles, atlantic_scores, color='green', alpha=0.25)

ax.plot(angles, indian_scores, color='red', linewidth=2, label='Indian Ocean')
ax.fill(angles, indian_scores, color='red', alpha=0.25)

ax.plot(angles, arctic_scores, color='purple', linewidth=2, label='Arctic Ocean')
ax.fill(angles, arctic_scores, color='purple', alpha=0.25)

# Add category labels to each spoke
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, fontweight='bold', ha='center')

# Add a descriptive title with line breaks
plt.title("Flavors of the Ocean:\nA Complex Radar Exploration of Oceanic Resources\nAcross Multiple Dimensions", fontsize=15, fontweight='bold', pad=20)

# Add legend to differentiate the oceans
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=9)

# Enhance layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()