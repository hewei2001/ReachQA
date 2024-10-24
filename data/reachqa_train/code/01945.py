import matplotlib.pyplot as plt
import numpy as np

# Data: Life expectancy (years) for different animal groups
mammals = [7, 10, 12, 15, 20, 25, 30]
birds = [3, 5, 10, 15, 20, 25]
reptiles = [2, 5, 10, 20, 30, 40, 60]
amphibians = [1, 2, 3, 4, 5, 6, 8]
fish = [1, 2, 4, 7, 9, 12, 15]

# Compile data into a list
data = [mammals, birds, reptiles, amphibians, fish]
animal_groups = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish']

# Create horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))
box_colors = ['#a3c9a8', '#f7cac9', '#92a8d1', '#ffef96', '#c4e17f']

# Plot with custom box colors and styles
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Customize each box color
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

# Set y-axis labels to match the animal groups
ax.set_yticklabels(animal_groups, fontsize=11)
ax.set_xlabel('Life Expectancy (Years)', fontsize=12)
ax.set_title('Life Expectancy Across Animal Groups:\nAn Ecological Perspective', fontsize=14, pad=20)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap and enhance clarity
plt.tight_layout()

# Show plot
plt.show()