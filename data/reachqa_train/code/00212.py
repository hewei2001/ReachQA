import matplotlib.pyplot as plt
import squarify

# Define species and their respective areas in the forest (in hectares)
tree_species = [
    'Douglas Fir', 
    'Western Red Cedar', 
    'Sitka Spruce', 
    'Western Hemlock', 
    'Bigleaf Maple'
]

# Corresponding areas occupied by these species
species_area = [40, 30, 20, 15, 10]

# Normalize the area values for use in the treemap
total_area = sum(species_area)
sizes = [area / total_area * 100 for area in species_area]

# Define colors for each species
colors = ['#7f8c8d', '#2ecc71', '#3498db', '#e74c3c', '#9b59b6']

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=[f"{name}\n{size:.1f}%" for name, size in zip(tree_species, sizes)],
              color=colors, alpha=0.8, edgecolor="white", linewidth=2, 
              text_kwargs={'fontsize': 12, 'weight': 'bold', 'color': 'white'})

# Customize the title and layout
plt.title("Forest Biodiversity Distribution:\nTree Species in the Temperate Rainforest", fontsize=16, fontweight='bold')
plt.axis('off')  # Hide axes

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()