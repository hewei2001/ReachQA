import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and scores for each continent
categories = ['Air Pollution', 'Water Scarcity', 'Deforestation', 'Waste Management', 'Climate Change Vulnerability']
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']

# Intensity scores for each continent (scale 1-10)
scores = {
    'Africa': [7, 9, 8, 6, 8],
    'Asia': [8, 7, 6, 7, 9],
    'Europe': [5, 4, 3, 5, 6],
    'North America': [6, 5, 4, 7, 7],
    'South America': [6, 8, 7, 5, 8],
    'Oceania': [4, 5, 6, 3, 7]
}

# Number of variables/categories
num_vars = len(categories)

# Create a radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Plot setup
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plot each continent
for i, (continent, color) in enumerate(zip(continents, colors)):
    values = scores[continent]
    values += values[:1]  # Close the loop
    ax.fill(angles, values, color=color, alpha=0.25, label=continent)
    ax.plot(angles, values, color=color, linewidth=2)

# Add category labels
plt.xticks(angles[:-1], categories, color='black', size=12)

# Set y-axis limits and labels
ax.set_ylim(0, 10)
ax.set_yticks(range(1, 11))
ax.set_yticklabels(map(str, range(1, 11)), color='grey', size=10)

# Title
plt.title("Environmental Challenges Across Continents:\nA Comparative Analysis", 
          size=14, color='darkgreen', pad=20)

# Adding legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title="Continents")

# Adjust layout
plt.tight_layout()

# Show the radar chart
plt.show()