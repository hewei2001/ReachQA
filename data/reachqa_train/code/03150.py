import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

# Define the tree species and their distribution percentages
tree_species = ['Oak', 'Maple', 'Pine', 'Cherry Blossom', 'Birch', 'Magnolia', 'Sycamore', 'Elm']
species_distribution = [25, 20, 15, 10, 10, 8, 7, 5]  # Total sums to 100%

# Define colors and textures for each tree species
colors = ['#8B4513', '#FFD700', '#228B22', '#FF69B4', '#D2B48C', '#FFB6C1', '#A0522D', '#3CB371']
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O']

# Create a figure for the pie chart
fig, ax = plt.subplots(figsize=(12, 9))

# Create wedges without the shadow keyword, as it is not valid
wedges, texts, autotexts = ax.pie(
    species_distribution, 
    labels=tree_species, 
    autopct='%1.1f%%', 
    startangle=140,
    colors=colors, 
    pctdistance=0.85, 
    explode=(0.1, 0, 0, 0, 0, 0, 0, 0),  # Highlight 'Oak'
    wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.8, hatch=hatches[0]),
    textprops=dict(color="black")
)

# Set custom font properties
plt.setp(autotexts, size=10, weight="bold")

# Title with line breaks for clarity
ax.set_title(
    "The Great Urban Flora Overview:\nDominant Tree Species in Urban Parks Worldwide", 
    fontsize=18, fontweight='bold', pad=30
)

# Draw circle for donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white', ec='white', linewidth=1.25)
fig.gca().add_artist(centre_circle)

# Annotate the chart with additional information
ax.annotate('Oaks lead the way', xy=(-0.7, 0.5), xytext=(-1.5, 0.7), fontsize=10, color='#8B4513',
            arrowprops=dict(facecolor='#8B4513', arrowstyle='->', linewidth=2))

# Add a legend with icons
legend_patches = [Wedge((0, 0), 1, 0, 360, facecolor=colors[i], hatch=hatches[i]) for i in range(len(tree_species))]
ax.legend(legend_patches, tree_species, loc='center left', bbox_to_anchor=(1, 0.5), title="Tree Species", title_fontsize='13')

# Background gradient effect
ax.set_facecolor('#f7f7f7')

# Automatically adjust layout to enhance readability
plt.tight_layout()

# Display the plot
plt.show()