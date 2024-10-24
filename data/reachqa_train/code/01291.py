import matplotlib.pyplot as plt
import numpy as np

# Define the decades
decades = np.array(['1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
decade_numeric = np.arange(len(decades))

# Number of significant events each decade in Astronomy
astronomy_discoveries = np.array([5, 3, 2, 4, 7, 9, 11, 15, 18, 21, 22])

# Number of significant events each decade in Space Exploration
space_exploration_milestones = np.array([0, 1, 3, 6, 11, 15, 14, 18, 25, 30, 35])

# Create a new figure with subplots
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the lines
ax.plot(decade_numeric, astronomy_discoveries, marker='o', linestyle='-', color='b', label='Astronomy Discoveries', linewidth=2)
ax.plot(decade_numeric, space_exploration_milestones, marker='s', linestyle='--', color='r', label='Space Exploration Milestones', linewidth=2)

# Fill between the lines for visual emphasis
ax.fill_between(decade_numeric, astronomy_discoveries, space_exploration_milestones, color='gray', alpha=0.2, label='Difference Area')

# Add labels, title, and legend
ax.set_title("A Century of Discovery:\nThe Evolution of Astronomy and Space Exploration", fontsize=18, fontweight='bold', pad=25)
ax.set_xlabel('Decades', fontsize=14)
ax.set_ylabel('Number of Significant Discoveries/Missions', fontsize=14)
ax.set_xticks(decade_numeric)
ax.set_xticklabels(decades, rotation=45, ha='right')
ax.set_ylim(0, 40)

# Highlight key points with annotations
ax.annotate('First Moon Landing', xy=(4, 11), xytext=(5.5, 18),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='r', bbox=dict(boxstyle="round", fc="w"))
ax.annotate('Hubble Space Telescope', xy=(7, 14), xytext=(6.5, 23),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='b', bbox=dict(boxstyle="round", fc="w"))

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', fontsize=10, title='Key Developments')

# Add an event marker for the Space Race period
ax.axvspan(4, 6, color='yellow', alpha=0.3, lw=0, label='Space Race Era')

# Adjust layout for better spacing and visibility
plt.tight_layout()

# Display the plot
plt.show()