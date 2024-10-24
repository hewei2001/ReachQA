import matplotlib.pyplot as plt
import numpy as np

# Urban areas in Greenvale
urban_areas = ['Downtown', 'Northside', 'South Hills', 'East End', 'West Valley']

# Number of wildlife sightings reported from 2018 to 2022 for different species
species = ['Squirrels', 'Raccoons', 'Birds', 'Foxes', 'Coyotes']
sightings_data = np.array([
    [120, 80, 150, 40, 10],   # Downtown
    [100, 110, 200, 30, 20],  # Northside
    [150, 130, 180, 60, 15],  # South Hills
    [90, 90, 160, 20, 5],     # East End
    [130, 70, 170, 50, 8]     # West Valley
])

# Plot details
fig, ax = plt.subplots(figsize=(12, 7))

# Bar width
bar_width = 0.15
# X positions for each urban area
positions = np.arange(len(urban_areas))

# Colors for each species
colors = ['#69b3a2', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plot bars for each species
for i, species_data in enumerate(sightings_data.T):  # Transpose to iterate over species
    ax.bar(positions + i * bar_width, species_data, bar_width, label=species[i], color=colors[i])

# Adding text labels above bars
for i, species_data in enumerate(sightings_data.T):
    for j, value in enumerate(species_data):
        ax.text(j + i * bar_width, value + 3, str(value), ha='center', va='bottom', fontsize=9)

# Adding title and labels
plt.title("Wildlife Sightings in Urban Greenvale\n(2018-2022)", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Urban Areas", fontsize=12)
plt.ylabel("Number of Sightings", fontsize=12)
plt.xticks(positions + 2 * bar_width, urban_areas)  # Centering the xticks

# Adding legend
plt.legend(title='Species', title_fontsize='13', fontsize=11)

# Adding gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust the layout for optimal viewing
plt.tight_layout()

# Show the plot
plt.show()