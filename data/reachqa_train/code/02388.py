import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Skill attributes of a quintessential traveler
categories = ['Cultural Awareness', 'Language Proficiency', 'Survival Skills', 
              'Technological Savvy', 'Physical Fitness', 'Networking Ability', 
              'Financial Management']

# Data for a typical quintessential traveler (scale from 0 to 10)
traveler_scores = np.array([9, 8, 7, 8, 6, 8, 7])

# Data for an average traveler for comparison
average_scores = np.array([7, 7, 6, 6, 5, 7, 6])

# Number of variables
num_vars = len(categories)

# Compute angle of each axis (in radians) for radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart must be a closed loop, so duplicate the first value and angle
traveler_values = np.concatenate((traveler_scores, [traveler_scores[0]]))
average_values = np.concatenate((average_scores, [average_scores[0]]))
angles += angles[:1]

# Initialize the figure and its subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), subplot_kw=dict(polar=True))

# Radar chart subplot (ax1)
ax1.fill(angles, traveler_values, color='teal', alpha=0.25, label='Quintessential Traveler')
ax1.plot(angles, traveler_values, color='teal', linewidth=2)
ax1.fill(angles, average_values, color='orange', alpha=0.25, label='Average Traveler')
ax1.plot(angles, average_values, color='orange', linewidth=2)

# Add variable labels and title to the radar chart
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, color='darkslategray', size=9, wrap=True)
ax1.set_title('The Quintessential Traveler:\nSkills for Global Exploration', fontsize=13, fontweight='bold', pad=20)
ax1.yaxis.set_tick_params(labelsize=8, colors='darkslategray')
ax1.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.set_yticks([2, 4, 6, 8, 10])
ax1.set_yticklabels(['2', '4', '6', '8', '10'], color='gray', size=8)
ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Bar chart subplot (ax2)
x = np.arange(num_vars)  # the label locations
width = 0.35  # the width of the bars

ax2.bar(x - width/2, traveler_scores, width, color='teal', label='Quintessential Traveler')
ax2.bar(x + width/2, average_scores, width, color='orange', label='Average Traveler')

# Add labels, title, and customize the bar chart
ax2.set_ylabel('Score')
ax2.set_title('Comparison of Skills', fontsize=13, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(categories, rotation=45, ha="right", fontsize=10, wrap=True)
ax2.legend(loc='upper left')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Ensure layout is not overlapping
plt.tight_layout()

# Display the plot
plt.show()