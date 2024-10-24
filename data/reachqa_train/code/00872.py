import matplotlib.pyplot as plt
import numpy as np

# Data representing sightings of mythical creatures
creatures = ['Phoenix', 'Dragon', 'Minotaur', 'Griffin', 'Hydra', 'Chimera', 'Unicorn']
sightings_mesopotamian = [50, 20, 10, 30, 15, 5, 2]
sightings_egyptian = [40, 30, 5, 25, 10, 10, 3]
sightings_greek = [35, 45, 25, 40, 30, 20, 15]
sightings_indian = [25, 40, 5, 10, 5, 3, 20]

# Prepare proportions for stacked bar chart
total_sightings_per_civilization = [
    sum(sightings_mesopotamian),
    sum(sightings_egyptian),
    sum(sightings_greek),
    sum(sightings_indian)
]

proportions = {
    'Mesopotamian': np.array(sightings_mesopotamian) / total_sightings_per_civilization[0],
    'Egyptian': np.array(sightings_egyptian) / total_sightings_per_civilization[1],
    'Greek': np.array(sightings_greek) / total_sightings_per_civilization[2],
    'Indian': np.array(sightings_indian) / total_sightings_per_civilization[3]
}

# Setup the figure and axes for subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# Original Histogram Plot
ax1 = axs[0]
data = []
for creature, count in zip(creatures * 4, sightings_mesopotamian + sightings_egyptian + sightings_greek + sightings_indian):
    data.extend([creature] * count)

n, bins, patches = ax1.hist(data, bins=len(creatures), edgecolor='black', color='skyblue', alpha=0.7)
ax1.set_title('Chronicles of the Mystical:\nSightings of Mythical Creatures in Ancient Civilizations', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Mythical Creatures', fontsize=14)
ax1.set_ylabel('Number of Recorded Sightings', fontsize=14)
ax1.set_xticks(np.arange(len(creatures)))
ax1.set_xticklabels(creatures)

for count, rect in zip(n, patches):
    height = rect.get_height()
    ax1.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

# New Stacked Bar Chart
ax2 = axs[1]
bottom = np.zeros(len(creatures))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
for i, (civilization, prop) in enumerate(proportions.items()):
    ax2.bar(creatures, prop, bottom=bottom, color=colors[i], label=civilization, edgecolor='black', alpha=0.7)
    bottom += prop

ax2.set_title('Proportion of Mythical Creatures Sightings by Civilization', fontsize=14, fontweight='bold', pad=20)
ax2.set_ylabel('Proportion of Sightings', fontsize=14)
ax2.set_xlabel('Mythical Creatures', fontsize=14)
ax2.legend(title='Civilization', loc='upper left', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)

# Layout adjustment
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()