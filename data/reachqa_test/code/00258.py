import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import matplotlib.ticker as ticker

# Data for the explorers and their distances traveled (in nautical miles)
explorers = [
    'Christopher Columbus',
    'Vasco da Gama',
    'Ferdinand Magellan',
    'John Cabot',
    'Amerigo Vespucci'
]
distances = [
    12_000,  # Columbus' 4 main voyages to the New World
    24_000,  # Da Gama's voyages to India and beyond
    42_000,  # Magellan's circumnavigation of the globe
    3_000,   # Cabot's voyage to Newfoundland
    7_500    # Vespucci's voyages to South America
]

# Additional data for complexity: number of voyages
voyages = [
    4,  # Columbus
    3,  # Da Gama
    1,  # Magellan (the circumnavigation)
    1,  # Cabot
    2   # Vespucci
]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Define bar positions and colors
bar_positions = np.arange(len(explorers))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the bar chart for distances
bars = ax1.bar(bar_positions, distances, color=colors, width=0.6, 
               edgecolor='grey', hatch='//')

# Secondary axis for the number of voyages
ax2 = ax1.twinx()
ax2.plot(bar_positions, voyages, color='black', marker='o', linestyle='--')
ax2.set_ylabel('Number of Voyages', fontsize=12, color='black')

# Add data labels on the bars
for bar, distance in zip(bars, distances):
    height = bar.get_height()
    ax1.annotate(f'{distance:,} nm',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords='offset points',
                 ha='center', va='bottom', fontsize=10)

# Title and labels
ax1.set_title('Distances Traveled by Explorers\nDuring the Age of Discovery',
              fontsize=16, pad=15)
ax1.set_xlabel('Explorers', fontsize=12)
ax1.set_ylabel('Distance Traveled (nautical miles)', fontsize=12)

# Set the positions and labels of the x-ticks
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(explorers, rotation=30, ha='right', fontsize=10)

# Add grid lines on y-axis
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Legend for the plot
legend_elements = [Patch(facecolor=colors[i], edgecolor='grey', hatch='//',
                         label=f"{explorers[i]}'s distance") for i in range(len(explorers))]
ax1.legend(handles=legend_elements, title='Explorers', bbox_to_anchor=(1.15, 1), loc='upper left')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()