import matplotlib.pyplot as plt
import numpy as np

# Define the climate zones and plant species
climate_zones = ['Tropical', 'Arid', 'Temperate', 'Continental', 'Polar']
plant_species = ['Rice', 'Cactus', 'Wheat', 'Maple', 'Pine']

# Suitability scores for each plant species in different climate zones
suitability_scores = np.array([
    [9, 3, 7, 2, 1],  # Rice
    [1, 10, 3, 2, 1], # Cactus
    [4, 2, 9, 5, 3],  # Wheat
    [2, 1, 8, 10, 4], # Maple
    [1, 1, 5, 7, 10], # Pine
])

# Calculate the average suitability score for each plant species
average_scores = np.mean(suitability_scores, axis=1)

# Create the figure and axes for the plots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plot the heatmap on the first subplot
cax = ax1.imshow(suitability_scores, cmap='YlGnBu', aspect='auto', interpolation='nearest')
cbar = fig.colorbar(cax, ax=ax1, orientation='vertical', pad=0.05)
cbar.set_label('Suitability Score', fontsize=10, weight='bold')

# Set ticks and labels for heatmap
ax1.set_xticks(np.arange(len(climate_zones)))
ax1.set_yticks(np.arange(len(plant_species)))
ax1.set_xticklabels(climate_zones, rotation=45, ha='right', fontsize=9)
ax1.set_yticklabels(plant_species, fontsize=9)

# Add text annotations to heatmap
for i in range(len(plant_species)):
    for j in range(len(climate_zones)):
        ax1.text(j, i, suitability_scores[i, j], ha="center", va="center", color="black", fontsize=8)

# Add title and axes labels for heatmap
ax1.set_title("Suitability of Plant Species Across Climate Zones", fontsize=12, weight='bold', pad=15)
ax1.set_xlabel('Climate Zones', fontsize=11, weight='bold')
ax1.set_ylabel('Plant Species', fontsize=11, weight='bold')

# Plot the bar chart on the second subplot
bars = ax2.barh(plant_species, average_scores, color='teal', edgecolor='black')
ax2.set_title('Average Suitability Scores by Plant Species', fontsize=12, weight='bold', pad=15)
ax2.set_xlabel('Average Suitability Score', fontsize=11, weight='bold')
ax2.set_ylabel('Plant Species', fontsize=11, weight='bold')
ax2.set_xlim(0, 10)  # Adjusted to fit score range

# Annotate bar chart with score values
for bar in bars:
    ax2.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
             f'{bar.get_width():.1f}', va='center', ha='left', fontsize=9)

# Ensure there is adequate space between subplots and surrounding text
plt.tight_layout()

# Display the complete figure with subplots
plt.show()