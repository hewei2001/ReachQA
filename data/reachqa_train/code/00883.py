import matplotlib.pyplot as plt
import numpy as np

# Define the art movements and design styles
art_movements = ['Impressionism', 'Cubism', 'Art Deco', 'Minimalism', 'Surrealism']
design_styles = ['Futurism', 'Bauhaus', 'Brutalism', 'Eco Design', 'Postmodernism']

# Impact matrix: influence level of each art movement on the design style
influence_matrix = np.array([
    [7, 5, 3, 4, 6],  # Impressionism
    [6, 8, 2, 5, 7],  # Cubism
    [4, 7, 5, 3, 6],  # Art Deco
    [3, 4, 9, 8, 5],  # Minimalism
    [5, 6, 4, 7, 8],  # Surrealism
])

# Plotting the heat map
fig, ax = plt.subplots(figsize=(10, 8))

# Use imshow to display the heat map
cax = ax.imshow(influence_matrix, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Add a color bar with a label
colorbar = plt.colorbar(cax)
colorbar.set_label('Influence Level', fontsize=12, labelpad=10)

# Set axis ticks and labels
ax.set_xticks(np.arange(len(design_styles)))
ax.set_yticks(np.arange(len(art_movements)))
ax.set_xticklabels(design_styles, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(art_movements, fontsize=10)

# Title and labels
ax.set_title("Influence of Art Movements on Modern\nDesign Styles", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Modern Design Styles", fontsize=12, labelpad=20)
ax.set_ylabel("Historical Art Movements", fontsize=12, labelpad=20)

# Annotate each cell with its influence level
for i in range(len(art_movements)):
    for j in range(len(design_styles)):
        ax.text(j, i, influence_matrix[i, j], ha='center', va='center', color='darkred', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()