import matplotlib.pyplot as plt
import numpy as np

# Define decades for the x-axis
decades = np.arange(1970, 2021, 10)

# Population data in millions for each region
# The data represents populations for each decade: 1970, 1980, 1990, 2000, 2010, 2020
ardent_population = np.array([2, 3, 4, 5, 6, 7])
lumina_population = np.array([1, 2, 2.5, 3.5, 5, 6])
glacia_population = np.array([0.5, 1, 1.5, 2, 2.5, 3])

# Combine data to create stacked area chart
populations = np.vstack([ardent_population, lumina_population, glacia_population])

# Define the colors for each region
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Plotting the Area Chart
plt.figure(figsize=(12, 6))
plt.stackplot(decades, populations, labels=['Ardent', 'Lumina', 'Glacia'], colors=colors, alpha=0.8)

# Add titles and labels
plt.title('Population Growth in the\nFictional Land of Vesperia Over Decades', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (millions)', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title='Regions of Vesperia')

# Customize grid and layout
plt.grid(linestyle='--', alpha=0.6)
plt.xticks(decades, labels=[str(year) for year in decades])
plt.yticks(np.arange(0, 18, 2))  # Set y-ticks to prevent crowding

# Enhance the readability of x-axis labels
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()