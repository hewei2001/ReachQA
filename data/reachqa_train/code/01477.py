import matplotlib.pyplot as plt
import numpy as np

# Expanded list of agencies and their hypothetical success rates for each year from 2000 to 2020
agencies = ["NASA", "ESA", "SpaceX", "Roscosmos", "ISRO", "CNSA", "JAXA", "Blue Origin"]
success_rates = {
    "NASA": [87, 88, 90, 89, 92, 93, 94, 95, 96, 97, 98, 97, 95, 98, 99, 97, 96, 98, 99, 98, 99],
    "ESA": [84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 96, 97, 95, 98, 94, 92, 96, 97, 95, 94, 93],
    "SpaceX": [65, 67, 70, 73, 76, 80, 82, 85, 87, 90, 92, 94, 96, 98, 95, 99, 97, 96, 95, 97, 98],
    "Roscosmos": [81, 82, 83, 85, 87, 88, 89, 91, 92, 94, 95, 89, 91, 90, 89, 91, 90, 89, 88, 87, 86],
    "ISRO": [75, 77, 80, 81, 83, 86, 87, 89, 90, 91, 93, 95, 97, 96, 94, 92, 95, 94, 93, 91, 90],
    "CNSA": [80, 81, 83, 86, 87, 89, 91, 92, 93, 94, 95, 97, 98, 99, 98, 97, 96, 95, 96, 97, 99],
    "JAXA": [83, 84, 85, 87, 89, 90, 91, 93, 94, 95, 96, 98, 97, 95, 96, 94, 92, 93, 91, 90, 89],
    "Blue Origin": [60, 63, 65, 67, 70, 74, 77, 80, 82, 85, 87, 90, 92, 94, 95, 96, 97, 98, 99, 98, 97]
}

# Prepare data for the box plot
data = [success_rates[agency] for agency in agencies]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Plot the vertical box plot
box = ax.boxplot(data, labels=agencies, patch_artist=True, notch=True, vert=True)

# Customize the box plot with colors
colors = ['lightblue', 'lightgreen', 'salmon', 'lightcoral', 'lightskyblue', 'lightpink', 'lightyellow', 'lightgray']
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
ax.set_title('Launch Success Rates (2000-2020):\nComparative Analysis of Global Space Agencies', fontsize=16, fontweight='bold')
ax.set_ylabel('Success Rate (%)', fontsize=12)
ax.set_xlabel('Space Agencies', fontsize=12)

# Add grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Customize spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adding trend lines for medians
for i, agency in enumerate(agencies):
    ax.plot(np.full_like(data[i], i+1, dtype=float), data[i], 'o', color=colors[i], alpha=0.3, markersize=6)

# Adjust layout
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show plot
plt.show()