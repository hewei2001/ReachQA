import matplotlib.pyplot as plt
import numpy as np

# Define the labels for each adaptive trait
labels = np.array(['Water Conservation', 'Thermoregulation', 'Camouflage', 'Dietary Flexibility', 'Nocturnal Activity'])

# Define the number of traits
num_traits = len(labels)

# Data for each species
fennec_fox = np.array([7, 8, 9, 5, 10])
camel = np.array([10, 9, 5, 8, 4])
desert_tortoise = np.array([9, 7, 6, 4, 6])

# Repeat the first value to close the radar chart loop
fennec_fox = np.append(fennec_fox, fennec_fox[0])
camel = np.append(camel, camel[0])
desert_tortoise = np.append(desert_tortoise, desert_tortoise[0])

# Calculate angles for each trait (including closure)
angles = np.linspace(0, 2 * np.pi, num_traits, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each species and fill the areas
ax.fill(angles, fennec_fox, color='cyan', alpha=0.25, label='Fennec Fox')
ax.plot(angles, fennec_fox, color='cyan', linewidth=2)

ax.fill(angles, camel, color='orange', alpha=0.25, label='Camel')
ax.plot(angles, camel, color='orange', linewidth=2)

ax.fill(angles, desert_tortoise, color='green', alpha=0.25, label='Desert Tortoise')
ax.plot(angles, desert_tortoise, color='green', linewidth=2)

# Add labels for each angle
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=11)

# Title and legend with clear positioning
plt.title('Adaptive Traits of Desert Species', size=15, weight='bold', va='top')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Customize radial axis and hide y-ticks
ax.set_yticklabels([])
ax.set_rlabel_position(0)
ax.spines['polar'].set_visible(False)

# Improve layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()