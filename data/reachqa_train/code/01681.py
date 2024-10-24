import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Population density (people per square kilometer)
population_density = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000])

# Biodiversity index values for each wildlife category
bird_biodiversity = np.array([4.2, 3.9, 3.7, 3.5, 3.3, 3.0, 2.8, 2.5])
insect_biodiversity = np.array([2.5, 3.0, 3.5, 4.0, 4.5, 4.8, 5.0, 5.2])
mammal_biodiversity = np.array([3.8, 3.5, 3.2, 2.9, 2.7, 2.5, 2.2, 2.0])

# Figure setup
plt.figure(figsize=(14, 10))

# Scatter plot with color gradients
scatter_birds = plt.scatter(population_density, bird_biodiversity, 
                            c=bird_biodiversity, cmap='Greens', marker='o', label='Birds', s=100, edgecolor='black', alpha=0.7)

scatter_insects = plt.scatter(population_density, insect_biodiversity, 
                              c=insect_biodiversity, cmap='Oranges', marker='^', label='Insects', s=100, edgecolor='black', alpha=0.7)

scatter_mammals = plt.scatter(population_density, mammal_biodiversity, 
                              c=mammal_biodiversity, cmap='Blues', marker='s', label='Mammals', s=100, edgecolor='black', alpha=0.7)

# Add trend lines
for y_values, label, color in zip([bird_biodiversity, insect_biodiversity, mammal_biodiversity], 
                                  ['Birds', 'Insects', 'Mammals'], 
                                  ['green', 'orange', 'blue']):
    slope, intercept, _, _, _ = linregress(population_density, y_values)
    plt.plot(population_density, intercept + slope * population_density, color=color, linestyle='--', linewidth=1, label=f'{label} Trend')

# Annotations for specific points
plt.annotate('High Insect Biodiversity', xy=(8000, 5.2), xytext=(6500, 5.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold')

# Title, labels, and legend
plt.title("Exploring Urban Wildlife Biodiversity:\nCorrelation with Population Density", fontsize=18, fontweight='bold', ha='center')
plt.xlabel('Population Density (people per km²)', fontsize=14)
plt.ylabel('Biodiversity Index', fontsize=14)
plt.legend(title='Wildlife Category', fontsize=12, loc='upper right', frameon=True)

# Add grid and customize ticks
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(population_density, fontsize=12)
plt.yticks(np.arange(2.0, 5.5, 0.5), fontsize=12)

# Background shading for different biodiversity index ranges
plt.axhspan(4.5, 5.5, color='lightgreen', alpha=0.1)
plt.axhspan(3.5, 4.5, color='lightblue', alpha=0.1)
plt.axhspan(2.5, 3.5, color='lightcoral', alpha=0.1)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()