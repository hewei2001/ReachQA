import matplotlib.pyplot as plt
import numpy as np

# Define the data
national_parks = ['Yellowstone', 'Yosemite', 'Grand Canyon', 'Zion', 'Rocky Mountain']
tree_species = ['Oak', 'Pine', 'Maple', 'Birch', 'Spruce']
tree_counts = [
    [500, 400, 350, 150, 300],  # Yellowstone
    [350, 450, 200, 250, 300],  # Yosemite
    [400, 300, 300, 200, 400],  # Grand Canyon
    [450, 350, 250, 300, 200],  # Zion
    [300, 500, 400, 350, 250]   # Rocky Mountain
]

# Define the width of each bar and the positions for the x-axis labels
bar_width = 0.15
index = np.arange(len(national_parks))

# Set up the figure
plt.figure(figsize=(14, 8))

# Plot each species as a grouped bar
colors = ['#8B4513', '#228B22', '#FFA07A', '#BDB76B', '#4682B4']
for i, species in enumerate(tree_species):
    plt.bar(index + i * bar_width, [counts[i] for counts in tree_counts], bar_width, label=species, color=colors[i])

# Title and labels
plt.title('Tree Species Diversity\nin Major National Parks (2023)', fontsize=16, fontweight='bold')
plt.xlabel('National Parks', fontsize=12)
plt.ylabel('Number of Trees', fontsize=12)

# Set x-ticks to be in the middle of the grouped bars
plt.xticks(index + bar_width * 2, national_parks, rotation=15)

# Adding annotations for each bar
for i, counts in enumerate(tree_counts):
    for j, count in enumerate(counts):
        plt.text(index[i] + j * bar_width, count + 10, str(count), ha='center', va='bottom', fontsize=9, color='black')

# Add a legend
plt.legend(title="Species", fontsize=10, loc='upper left')

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust subplot parameters
plt.tight_layout()

# Display the plot
plt.show()