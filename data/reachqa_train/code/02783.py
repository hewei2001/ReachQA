import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define species and their estimated populations
species = [
    'Asian Elephants',
    'Bengal Tigers',
    'Giant Pandas',
    'Snow Leopards',
    'Mountain Gorillas'
]
populations = np.array([250, 50, 40, 20, 15])
colors = ['#7fc97f', '#fdc086', '#beaed4', '#ffff99', '#386cb0']

# Calculate percentage of total population for annotation
total_population = populations.sum()
percentages = (populations / total_population) * 100

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data
bars = ax.barh(species, populations, color=colors, edgecolor='black', hatch='//')

# Add text annotations for population and percentages
for bar, perc in zip(bars, percentages):
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height() / 2,
            f'{int(width)} ({perc:.1f}%)', va='center', ha='left', fontsize=10, fontweight='bold')

# Customize the plot
ax.set_title('Estimated Population of Endangered Species\nin Wildlife Preservation Reserve (2023)',
             fontsize=16, fontweight='bold', loc='center', pad=20)
ax.set_xlabel('Estimated Population', fontsize=14)
ax.set_xlim(0, 300)

# Add gridlines for clarity
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)

# Create a legend with species icons
legend_elements = [Patch(facecolor=colors[i], edgecolor='black', hatch='//', label=species[i]) for i in range(len(species))]
ax.legend(handles=legend_elements, title="Species", loc='upper right', bbox_to_anchor=(1.15, 1))

# Historical data subplot
# Define historical data for additional context
years = np.array([2000, 2005, 2010, 2015, 2020, 2023])
populations_history = np.array([
    [300, 280, 260, 255, 250, 250],  # Asian Elephants
    [100, 90, 80, 60, 55, 50],       # Bengal Tigers
    [50, 45, 45, 40, 40, 40],        # Giant Pandas
    [30, 25, 22, 21, 20, 20],        # Snow Leopards
    [20, 18, 16, 15, 15, 15]         # Mountain Gorillas
])

ax2 = fig.add_axes([0.15, -0.4, 0.7, 0.3])  # Add a subplot at the bottom
for i, color in enumerate(colors):
    ax2.plot(years, populations_history[i], label=species[i], color=color, marker='o')

ax2.set_title('Historical Population Trends', fontsize=14, fontweight='bold', loc='center', pad=10)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Population', fontsize=12)
ax2.legend(loc='upper right')
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout()
plt.subplots_adjust(bottom=0.25)  # Adjust space for historical trends subplot

# Show the plot
plt.show()