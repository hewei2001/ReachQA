import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Skill attributes of a quintessential traveler
categories = ['Cultural Awareness', 'Language Proficiency', 'Survival Skills', 
              'Technological Savvy', 'Physical Fitness', 'Networking Ability', 
              'Financial Management']

# Data for a typical quintessential traveler (scale from 0 to 10)
values = np.array([9, 8, 7, 8, 6, 8, 7])

# Number of variables
num_vars = len(categories)

# Compute angle of each axis (in radians)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart must be a closed loop, so duplicate the first value and angle
values = np.concatenate((values, [values[0]]))
angles += angles[:1]

# Initialize the radar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot the radar chart
ax.fill(angles, values, color='teal', alpha=0.25)
ax.plot(angles, values, color='teal', linewidth=2)

# Add variable labels
plt.xticks(angles[:-1], categories, color='darkslategray', size=10)

# Add title with line breaks for readability
ax.set_title('The Quintessential Traveler:\nSkills for Global Exploration', 
             fontsize=14, fontweight='bold', pad=20)

# Customize radial labels and grid
ax.yaxis.set_tick_params(labelsize=8, colors='darkslategray')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Add radial range labels
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='gray', size=8)

# Ensure layout is not overlapping
plt.tight_layout()

# Display the plot
plt.show()