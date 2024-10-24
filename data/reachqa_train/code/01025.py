import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the performance categories
categories = ['Speed', 'Durability', 'Energy Efficiency', 'Payload Capacity', 'Navigation Systems', 'Crew Comfort']

# Performance metrics for each spacecraft model
stellar_voyager = [90, 85, 70, 80, 75, 95]
comet_cruiser = [80, 88, 85, 75, 70, 90]
nebula_navigator = [75, 80, 90, 85, 88, 80]

# Number of variables we're plotting
num_vars = len(categories)

# Compute angle for each category in the radar chart
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the loop

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to add spacecraft data to the radar chart
def add_to_radar(ax, values, color, label):
    values += values[:1]  # Repeat the first value to close the circle
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2, label=label)

# Add data for each spacecraft
add_to_radar(ax, stellar_voyager, 'blue', 'Stellar Voyager')
add_to_radar(ax, comet_cruiser, 'orange', 'Comet Cruiser')
add_to_radar(ax, nebula_navigator, 'green', 'Nebula Navigator')

# Add labels to the categories
plt.xticks(angles[:-1], categories, color='grey', size=10)

# Customize the radar chart's scales and labels
ax.set_rscale('linear')
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], color='grey', size=7)
ax.yaxis.grid(True)

# Set the title and legend
plt.title('Interstellar Fleet Performance Comparison\nSpacecraft Evaluation Report 2150', size=15, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()