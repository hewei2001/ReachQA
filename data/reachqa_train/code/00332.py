import matplotlib.pyplot as plt
import numpy as np

# Define decades and marine biodiversity data (population in millions)
decades = np.arange(1920, 2030, 10)
fish_population = [80, 78, 72, 68, 65, 63, 66, 78, 90, 110, 130]
mollusks_population = [45, 43, 41, 37, 35, 33, 35, 40, 45, 50, 60]
crustaceans_population = [40, 39, 37, 34, 32, 31, 34, 38, 42, 48, 55]
marine_mammals_population = [12, 13, 14, 12, 11, 9, 10, 13, 17, 22, 28]

# Stack the data
biodiversity_data = np.vstack([fish_population, mollusks_population, crustaceans_population, marine_mammals_population])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart with transparency
ax.stackplot(decades, biodiversity_data, labels=['Fish', 'Mollusks', 'Crustaceans', 'Marine Mammals'],
             colors=['#1f78b4', '#33a02c', '#ff7f00', '#6a3d9a'], alpha=0.7)

# Add title and labels with appropriate font sizes and layout
ax.set_title('Exploration of the Ocean Depths:\nMarine Biodiversity Trends Over the Last Century', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (Millions)', fontsize=12)

# Customize x-axis labels
plt.xticks(decades, rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(loc='upper left', title='Species Groups', fontsize=10, title_fontsize='13')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()