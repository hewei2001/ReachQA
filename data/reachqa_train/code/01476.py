import matplotlib.pyplot as plt
import numpy as np

# Agencies and their hypothetical success rates for each year from 2010 to 2020
agencies = ["NASA", "ESA", "SpaceX", "Roscosmos", "ISRO"]
success_rates = {
    "NASA": [96, 97, 98, 97, 95, 98, 99, 97, 96, 98, 99],
    "ESA": [94, 95, 93, 96, 97, 95, 98, 94, 92, 96, 97],
    "SpaceX": [75, 80, 85, 90, 92, 94, 96, 98, 95, 99, 97],
    "Roscosmos": [89, 91, 90, 88, 92, 93, 94, 95, 89, 91, 90],
    "ISRO": [88, 89, 90, 91, 93, 95, 97, 96, 94, 92, 95]
}

# Prepare data for the box plot
data = [success_rates[agency] for agency in agencies]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the vertical box plot
box = ax.boxplot(data, labels=agencies, patch_artist=True, notch=True, vert=True)

# Customize the box plot with colors
colors = ['lightblue', 'lightgreen', 'salmon', 'lightcoral', 'lightskyblue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Style box plot elements
for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle='--')
for cap in box['caps']:
    cap.set(color='gray', linewidth=1.5)
for median in box['medians']:
    median.set(color='orange', linewidth=2)
for flier in box['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)

# Add title and labels
ax.set_title('Launch Success Rates (2010-2020):\nComparison of Major Space Agencies', fontsize=16, fontweight='bold')
ax.set_ylabel('Success Rate (%)', fontsize=12)
ax.set_xlabel('Space Agencies', fontsize=12)

# Add grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Customize spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Automatically adjust layout for better readability
plt.tight_layout()

# Show plot
plt.show()