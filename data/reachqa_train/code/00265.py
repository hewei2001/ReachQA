import matplotlib.pyplot as plt
import numpy as np

# Define hours spent with each type of pet per week in urban apartments
cats_hours = [10, 12, 15, 16, 8, 14, 15, 18, 20, 11, 13, 16]
dogs_hours = [20, 22, 30, 25, 28, 35, 33, 32, 29, 31, 34, 30]
birds_hours = [5, 7, 8, 6, 9, 7, 10, 11, 5, 6, 8, 9]
reptiles_hours = [4, 5, 6, 3, 4, 5, 7, 6, 8, 5, 4, 3]
small_mammals_hours = [8, 10, 7, 9, 12, 11, 10, 9, 8, 11, 12, 10]

# Combine data into a list
pets_data = [cats_hours, dogs_hours, birds_hours, reptiles_hours, small_mammals_hours]

pet_types = ['Cats', 'Dogs', 'Birds', 'Reptiles', 'Small Mammals']

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot box plots
box = ax.boxplot(pets_data, vert=False, patch_artist=True, labels=pet_types, notch=True, whis=[5, 95])

# Define colors for each pet type
colors = ['coral', 'lightblue', 'lightgreen', 'plum', 'khaki']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize plot appearance
for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='grey', linewidth=1.5, linestyle='--')
    cap.set(color='grey', linewidth=1.5)
    median.set(color='darkred', linewidth=2)
    flier.set(marker='o', color='gold', alpha=0.5)

# Overlay violin plots
for i, data in enumerate(pets_data, start=1):
    parts = ax.violinplot(data, positions=[i], vert=False, showmeans=False, showextrema=False, widths=0.7)
    for pc in parts['bodies']:
        pc.set_facecolor(colors[i-1])
        pc.set_alpha(0.3)

# Add title and labels
ax.set_title('Pet Popularity:\nTime Spent with Different Pet Species in Urban Apartments', fontsize=16, fontweight='bold')
ax.set_xlabel('Hours Spent per Week', fontsize=14)
ax.set_ylabel('Pet Type', fontsize=14)

# Grid and layout adjustments
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
plt.tight_layout()

# Legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, pet_types, title='Pet Types', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Display the plot
plt.show()