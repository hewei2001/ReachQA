import matplotlib.pyplot as plt
import numpy as np

# Define species and their estimated populations
species = [
    'Asian Elephants',
    'Bengal Tigers',
    'Giant Pandas',
    'Snow Leopards',
    'Mountain Gorillas'
]
populations = np.array([250, 50, 40, 20, 15])

# Set up the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the data
bars = ax.barh(species, populations, color=['#7fc97f', '#fdc086', '#beaed4', '#ffff99', '#386cb0'])

# Adding labels to each bar
for bar in bars:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
            f'{int(bar.get_width())}', va='center', ha='left', fontsize=10, fontweight='bold')

# Customize the plot appearance
ax.set_title('Estimated Population of Endangered Species\nin Wildlife Preservation Reserve (2023)', 
             fontsize=16, fontweight='bold', loc='center', pad=20)
ax.set_xlabel('Estimated Population', fontsize=14)
ax.set_xlim(0, 300)

# Add gridlines for clarity
ax.xaxis.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout()

# Show the plot
plt.show()