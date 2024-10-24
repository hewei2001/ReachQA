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

# New data: Hypothetical growth in wildlife sightings (as percentage increase over years)
growth_percentage = np.array([5, 8, 3, 4, 2])

# Plot settings
fig, axes = plt.subplots(1, 2, figsize=(15, 7))
bar_width = 0.15
positions = np.arange(len(urban_areas))
colors = ['#69b3a2', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# First subplot: Grouped bar chart
for i, species_data in enumerate(sightings_data.T):
    axes[0].bar(positions + i * bar_width, species_data, bar_width, label=species[i], color=colors[i])
    for j, value in enumerate(species_data):
        axes[0].text(j + i * bar_width, value + 3, str(value), ha='center', va='bottom', fontsize=9)

axes[0].set_title("Wildlife Sightings in Urban Greenvale\n(2018-2022)", fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel("Urban Areas", fontsize=12)
axes[0].set_ylabel("Number of Sightings", fontsize=12)
axes[0].set_xticks(positions + 2 * bar_width)
axes[0].set_xticklabels(urban_areas)
axes[0].legend(title='Species', title_fontsize='12', fontsize=10)
axes[0].grid(axis='y', linestyle='--', alpha=0.6)

# Second subplot: Line chart showing percentage growth of wildlife sightings
axes[1].plot(urban_areas, growth_percentage, marker='o', color='b', linewidth=2)
for i, value in enumerate(growth_percentage):
    axes[1].text(i, value + 0.5, f"{value}%", ha='center', va='bottom', fontsize=9, color='darkblue')

axes[1].set_title("Hypothetical Growth in Wildlife Sightings\n(Percentage Increase)", fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel("Urban Areas", fontsize=12)
axes[1].set_ylabel("Growth Percentage (%)", fontsize=12)
axes[1].set_ylim(0, 10)
axes[1].grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()