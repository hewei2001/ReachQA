import matplotlib.pyplot as plt
import numpy as np

# Data representing sightings of mythical creatures
creatures = ['Phoenix', 'Dragon', 'Minotaur', 'Griffin', 'Hydra', 'Chimera', 'Unicorn']
# Count of sightings for each creature type from different civilizations
sightings_mesopotamian = [50, 20, 10, 30, 15, 5, 2]
sightings_egyptian = [40, 30, 5, 25, 10, 10, 3]
sightings_greek = [35, 45, 25, 40, 30, 20, 15]
sightings_indian = [25, 40, 5, 10, 5, 3, 20]

# Combining sightings data into one dataset for histogram plotting
sightings = (
    sightings_mesopotamian +
    sightings_egyptian +
    sightings_greek +
    sightings_indian
)

# Repeating creature names based on their sighting count
data = []
for creature, count in zip(creatures * 4, sightings):
    data.extend([creature] * count)

# Configure and plot the histogram
fig, ax = plt.subplots(figsize=(12, 8))
n, bins, patches = ax.hist(data, bins=len(creatures), edgecolor='black', color='skyblue', alpha=0.7)

# Customizing the chart
ax.set_title('Chronicles of the Mystical:\nSightings of Mythical Creatures in Ancient Civilizations', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Mythical Creatures', fontsize=14)
ax.set_ylabel('Number of Recorded Sightings', fontsize=14)
ax.set_xticks(np.arange(len(creatures)))
ax.set_xticklabels(creatures)

# Adding annotations for each bar
for count, rect in zip(n, patches):
    height = rect.get_height()
    ax.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

# Adding a legend for cultural context
legend_labels = [
    'Sightings in Mesopotamia', 
    'Sightings in Egypt', 
    'Sightings in Greece', 
    'Sightings in India'
]
ax.legend(legend_labels, title='Civilization Context', loc='upper right', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)

# Layout adjustment
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()