import matplotlib.pyplot as plt

# Observation programs and their monthly recorded observations
programs = ['Star Gazing', 'Planet Exploration', 'Galactic Survey', 'Asteroid Watch', 'Comet Tracker']
observations = {
    'Star Gazing': [120, 130, 135, 140, 145, 150],
    'Planet Exploration': [150, 160, 155, 165, 170, 175],
    'Galactic Survey': [180, 185, 190, 195, 200, 205],
    'Asteroid Watch': [100, 105, 110, 115, 120, 125],
    'Comet Tracker': [130, 135, 140, 145, 150, 155]
}

# Collect the observations data
data = [observations[program] for program in programs]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the box plot
box = ax.boxplot(data, patch_artist=True, notch=True, vert=True, 
                 boxprops=dict(facecolor='#d1e7dd', color='black'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='blue'),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=5))

# Customize and annotate the plot
ax.set_title('Distribution of Celestial Observations by Program\n(January to June 2023)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Observation Programs', fontsize=12)
ax.set_ylabel('Number of Observations', fontsize=12)
ax.set_xticks(range(1, len(programs) + 1))
ax.set_xticklabels(programs, fontsize=11)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding a legend
handles = [plt.Line2D([0], [0], color='blue', lw=2, label='Median'),
           plt.Line2D([0], [0], marker='o', color='w', label='Outliers', 
                      markerfacecolor='red', markersize=5)]
ax.legend(handles=handles, loc='upper left', fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()