import matplotlib.pyplot as plt
import numpy as np

# Criteria and shop names
categories = ['Coffee Quality', 'Ambiance', 'Customer Service', 'Pricing', 'Variety', 'Sustainability']
shops = ['Cafe Aroma', 'Brewed Awakening', 'Bean Bliss', 'The Roastery']

# Scores for each shop on each criterion (0-10 scale)
scores = np.array([
    [8, 7, 9, 6, 8, 7],  # Cafe Aroma
    [9, 8, 8, 5, 7, 8],  # Brewed Awakening
    [7, 6, 9, 7, 6, 6],  # Bean Bliss
    [8, 9, 7, 6, 9, 9]   # The Roastery
])

# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for the radar
scores = np.concatenate((scores, scores[:, [0]]), axis=1)
angles += angles[:1]

# Create plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Set color palette
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371']

# Plot each shop
for i, shop in enumerate(shops):
    ax.fill(angles, scores[i], color=colors[i], alpha=0.25)
    ax.plot(angles, scores[i], label=shop, color=colors[i])

# Add labels
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Add title and legend
ax.set_title("Gourmet Coffee Shop Evaluation:\nRadar Chart Analysis of Customer Satisfaction", size=15, pad=30)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()