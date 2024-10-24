import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories for the radar chart
categories = ['Magic', 'Strength', 'Agility', 'Intelligence', 'Charisma']
N = len(categories)

# Create the data for each race
elves = [90, 40, 80, 85, 75]
dwarves = [20, 85, 40, 60, 50]
orcs = [10, 95, 50, 40, 30]
humans = [60, 70, 70, 70, 65]

# Data for all races
data = [elves, dwarves, orcs, humans]
race_names = ['Elves', 'Dwarves', 'Orcs', 'Humans']

# Calculate average performance for each category
average_performance = [np.mean([elves[i], dwarves[i], orcs[i], humans[i]]) for i in range(N)]

# Create the angles for each category on the radar chart
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]  # Ensure the plot is circular

# Set up the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw one line per race
for i, race_data in enumerate(data):
    race_data += race_data[:1]  # Loop back to the start
    ax.plot(angles, race_data, linewidth=2, linestyle='solid', label=race_names[i])
    ax.fill(angles, race_data, alpha=0.25)

# Add category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Set the range of the radial axes
ax.set_ylim(0, 100)

# Overlay the average performance as a radial bar chart
bars = ax.bar(angles[:-1], average_performance, color='grey', alpha=0.3, width=0.15, edgecolor='black', linewidth=1.5, label='Average Performance')

# Add a legend and title
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.title('RPG Fantasy Races Comparison\nAbilities & Strengths\nand Average Performance', size=14, pad=30)

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()