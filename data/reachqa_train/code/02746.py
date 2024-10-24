import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the plant species and their attributes
plant_species = ['Oak', 'Cactus', 'Fern', 'Bamboo', 'Tulip']
attributes = ['Resilience', 'Moisture', 'Sunlight', 'Nutrients', 'Growth']

# Define the data for each plant species
data = np.array([
    [8, 4, 6, 7, 5],  # Oak
    [9, 8, 10, 3, 2], # Cactus
    [6, 9, 5, 8, 4],  # Fern
    [7, 5, 7, 9, 6],  # Bamboo
    [5, 6, 8, 5, 7]   # Tulip
])

# Number of variables
num_attributes = len(attributes)

# Add the first column to the end of each row to close the radar chart
data = np.concatenate((data, data[:, [0]]), axis=1)

# Compute angle for each attribute in radar chart
angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]  # complete the loop

# Create a radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each plant's data and fill the area
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, species in enumerate(plant_species):
    ax.plot(angles, data[i], linewidth=1.5, linestyle='solid', label=species, color=colors[i])
    ax.fill(angles, data[i], color=colors[i], alpha=0.25)

# Add labels for each attribute
plt.xticks(angles[:-1], attributes, fontsize=11)

# Set radial ticks and labels
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], color='grey', size=10)
plt.ylim(0, 10)

# Add title and legend
plt.title('Versatile Flora:\nPlant Attributes Across Diverse Habitats', fontsize=16, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title='Plant Species', fontsize=10)

# Automatically adjust the layout to prevent overlapping text
plt.tight_layout()

# Display the plot
plt.show()