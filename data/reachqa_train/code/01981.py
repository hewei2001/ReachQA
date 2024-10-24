import matplotlib.pyplot as plt
import numpy as np

# Define bird species observed
bird_species = [
    'Scarlet Sunbird', 'Blue Jaydreamer', 'Golden Finch', 'Emerald Parrot',
    'Twilight Owl', 'Crescent Hawk', 'Ruby Robin', 'Silver Sparrow'
]

# Create explicit data for bird sightings over 10 days
# Each entry in the list corresponds to sightings of a species across the 10-day survey
sightings = [
    [14, 15, 15, 16, 20, 22, 18, 19, 25, 28],  # Scarlet Sunbird
    [5, 7, 6, 8, 12, 14, 16, 13, 12, 15],     # Blue Jaydreamer
    [9, 8, 10, 11, 9, 10, 15, 12, 11, 13],    # Golden Finch
    [3, 4, 5, 4, 5, 6, 4, 5, 6, 8],           # Emerald Parrot
    [11, 13, 12, 14, 16, 18, 17, 19, 21, 20], # Twilight Owl
    [7, 8, 9, 10, 12, 11, 10, 9, 8, 11],      # Crescent Hawk
    [2, 3, 4, 5, 6, 7, 6, 8, 9, 10],          # Ruby Robin
    [6, 5, 7, 6, 8, 9, 11, 10, 12, 13]        # Silver Sparrow
]

# Flatten the list of sightings for the histogram
flattened_sightings = [sighting for species in sightings for sighting in species]

# Create a histogram
plt.figure(figsize=(14, 8))
n, bins, patches = plt.hist(flattened_sightings, bins=range(0, 35, 5), edgecolor='black', color='skyblue', alpha=0.7)

# Annotate the histogram with species names
for bin_count, patch, species in zip(n, patches, bird_species):
    plt.text(patch.get_x() + patch.get_width()/2, bin_count + 0.2, species,
             fontsize=10, fontweight='bold', va='bottom', ha='center', rotation=90)

# Customize the plot
plt.title('Bird Sightings Distribution on Naturalis Island\n(10-Day Survey Period)', fontsize=16, fontweight='bold')
plt.xlabel('Number of Sightings in Range', fontsize=14)
plt.ylabel('Frequency of Sightings', fontsize=14)
plt.xticks(np.arange(0, 35, 5), labels=[f'{i}-{i+4}' for i in range(0, 35, 5)])
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()