import matplotlib.pyplot as plt
import numpy as np

# Define bird species observed
bird_species = [
    'Scarlet Sunbird', 'Blue Jaydreamer', 'Golden Finch', 'Emerald Parrot',
    'Twilight Owl', 'Crescent Hawk', 'Ruby Robin', 'Silver Sparrow'
]

# Sightings data over 10 days
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

# Calculate the average sightings per day for the line plot
average_sightings_per_day = np.mean(sightings, axis=0)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Bird Sightings Analysis on Naturalis Island\nAcross 10-Day Survey Period', fontsize=16, fontweight='bold')

# Plot histogram in the first subplot
flattened_sightings = [sighting for species in sightings for sighting in species]
n, bins, patches = ax1.hist(flattened_sightings, bins=range(0, 35, 5), edgecolor='black', color='skyblue', alpha=0.7)

# Annotate the histogram with species names
for bin_count, patch, species in zip(n, patches, bird_species):
    ax1.text(patch.get_x() + patch.get_width()/2, bin_count + 0.2, species,
             fontsize=10, fontweight='bold', va='bottom', ha='center', rotation=90)

# Customize the first subplot
ax1.set_title('Distribution of Bird Sightings', fontsize=14, fontweight='bold')
ax1.set_xlabel('Number of Sightings in Range', fontsize=12)
ax1.set_ylabel('Frequency of Sightings', fontsize=12)
ax1.set_xticks(np.arange(0, 35, 5))
ax1.set_xticklabels([f'{i}-{i+4}' for i in range(0, 35, 5)])
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Plot line chart in the second subplot
days = np.arange(1, 11)
ax2.plot(days, average_sightings_per_day, marker='o', color='green', linestyle='-', linewidth=2, markersize=8, label='Average Sightings')

# Annotate the line chart with average values
for day, avg in zip(days, average_sightings_per_day):
    ax2.text(day, avg + 0.2, f'{avg:.1f}', fontsize=9, va='bottom', ha='center')

# Customize the second subplot
ax2.set_title('Average Bird Sightings Per Day', fontsize=14, fontweight='bold')
ax2.set_xlabel('Day', fontsize=12)
ax2.set_ylabel('Average Number of Sightings', fontsize=12)
ax2.set_xticks(days)
ax2.legend(loc='upper left')
ax2.grid(axis='both', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plots
plt.show()