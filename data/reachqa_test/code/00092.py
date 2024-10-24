import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define planets and their difficulty levels (arbitrary units)
planet_names = ['Terra Nova', 'Red Dusk', 'Blue Mirage', 'Green Glade', 'Silver Peak']
difficulty_levels = [1, 2, 3, 4, 5]  # Arbitrary difficulty levels

# Exploration efficiency (%) of drones on these planets
exploration_efficiency = [92, 78, 65, 47, 30]

# Additional data for the bar chart subplot
# Example: Average resources gathered (arbitrary units) on each planet
resources_gathered = [150, 120, 90, 50, 20]

# Create a subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Scatter plot with smoothing curve
ax1.scatter(difficulty_levels, exploration_efficiency, color='teal', s=100, edgecolors='black', label='Efficiency Data')

difficulty_levels_smooth = np.linspace(min(difficulty_levels), max(difficulty_levels), 300)
spl = make_interp_spline(difficulty_levels, exploration_efficiency, k=3)
efficiency_smooth = spl(difficulty_levels_smooth)

ax1.plot(difficulty_levels_smooth, efficiency_smooth, color='orangered', linewidth=2, linestyle='-', label='Efficiency Trend')

for i, planet in enumerate(planet_names):
    ax1.annotate(planet, (difficulty_levels[i], exploration_efficiency[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, weight='bold', color='darkblue')

ax1.set_xlabel('Planetary Difficulty Level', fontsize=12)
ax1.set_ylabel('Exploration Efficiency (%)', fontsize=12)
ax1.set_title('Exploration Efficiency of Drones\nAcross Alien Planets', fontsize=14, weight='bold')
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Bar chart for average resources gathered
ax2.bar(planet_names, resources_gathered, color=['skyblue', 'lightcoral', 'lightgreen', 'gold', 'lightgray'], edgecolor='black')
ax2.set_ylabel('Average Resources Gathered', fontsize=12)
ax2.set_title('Resources Gathered by Drones\nAcross Planets', fontsize=14, weight='bold')
ax2.set_ylim(0, max(resources_gathered) + 30)
for i, val in enumerate(resources_gathered):
    ax2.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=10, weight='bold', color='darkblue')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()