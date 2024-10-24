import matplotlib.pyplot as plt
import numpy as np

# Define the labels for each axis representing different attributes
attributes = ['Speed', 'Intelligence', 'Strength', 'Camouflage', 'Lifespan']

# Define the data for each creature
dolphin = [8, 9, 5, 4, 7]
octopus = [5, 8, 3, 9, 6]
shark = [9, 6, 8, 3, 8]
seahorse = [3, 4, 2, 7, 5]
jellyfish = [2, 3, 1, 8, 4]

# Combine the data in a list
creatures = [dolphin, octopus, shark, seahorse, jellyfish]
creature_names = ['Dolphin', 'Octopus', 'Shark', 'Seahorse', 'Jellyfish']

# Number of variables
num_vars = len(attributes)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Make the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Loop over data to plot each creature
for idx, creature in enumerate(creatures):
    # Complete the data circle
    data = np.array(creature)
    data = np.concatenate((data, [data[0]]))
    current_angles = angles + angles[:1]
    
    # Draw the radar chart
    ax.fill(current_angles, data, alpha=0.25, label=creature_names[idx])
    ax.plot(current_angles, data, linewidth=2)

# Set the attributes as labels on the axes
ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels(attributes, fontsize=10, weight='bold')

# Set title and legend
ax.set_title("Marine Life Adaptation Radar Chart\nComparative Analysis", size=16, color='darkblue', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()