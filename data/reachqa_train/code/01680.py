import matplotlib.pyplot as plt
import numpy as np

# Population density (people per square kilometer)
population_density = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000])

# Biodiversity index values for each wildlife category
bird_biodiversity = np.array([4.2, 3.9, 3.7, 3.5, 3.3, 3.0, 2.8, 2.5])
insect_biodiversity = np.array([2.5, 3.0, 3.5, 4.0, 4.5, 4.8, 5.0, 5.2])
mammal_biodiversity = np.array([3.8, 3.5, 3.2, 2.9, 2.7, 2.5, 2.2, 2.0])

# Plotting setup
plt.figure(figsize=(12, 8))

# Scatter plot for each category
plt.scatter(population_density, bird_biodiversity, color='forestgreen', marker='o', label='Birds', s=100, edgecolor='black', alpha=0.7)
plt.scatter(population_density, insect_biodiversity, color='darkorange', marker='^', label='Insects', s=100, edgecolor='black', alpha=0.7)
plt.scatter(population_density, mammal_biodiversity, color='royalblue', marker='s', label='Mammals', s=100, edgecolor='black', alpha=0.7)

# Title, labels, and legend
plt.title("Exploring Urban Wildlife Biodiversity:\nCorrelation with Population Density", fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Population Density (people per km²)', fontsize=12)
plt.ylabel('Biodiversity Index', fontsize=12)
plt.legend(title='Wildlife Category', fontsize=10, loc='upper right', frameon=True)

# Add grid and customize ticks
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(population_density)
plt.yticks(np.arange(2.0, 5.5, 0.5))

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()