import matplotlib.pyplot as plt
import numpy as np

# Define fictional planet names and mission stages
planets = ['Xylophon', 'Zantron', 'Gallium', 'Quria', 'Vortexia']

# Constructing data for each stage and planet (in billion Galactic Credits)
# Each sub-list contains costs for stages: Initial Research, Launch Prep, Travel, Landing Ops, Surface Exploration
costs = {
    'Xylophon': [15, 18, 25, 35, 40],
    'Zantron': [12, 22, 32, 42, 37],
    'Gallium': [10, 19, 27, 33, 29],
    'Quria': [14, 21, 31, 38, 36],
    'Vortexia': [17, 23, 34, 45, 41]
}

# Prepare data for box plot: transpose to create datasets for each stage across different planets
stages_data = np.array(list(costs.values())).T

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the vertical box plots with notch and color
boxplots = ax.boxplot(stages_data, notch=True, vert=True, patch_artist=True, labels=['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4', 'Stage 5'])

# Define a color palette
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Set colors for each box plot and adjust median line properties
for patch, color, median in zip(boxplots['boxes'], colors, boxplots['medians']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
    patch.set_edgecolor('black')
    median.set_color('black')
    median.set_linewidth(1.5)

# Customizing the plot
ax.set_title('Galactic Exploration Costs\nAcross Mission Stages (2300 Andromeda Missions)', fontsize=16, fontweight='bold')
ax.set_ylabel('Cost (Billion Galactic Credits)', fontsize=12)
ax.set_xlabel('Mission Stage', fontsize=12)

# Add a grid for the y-axis to improve readability
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.6)

# Adding legends to explain stages
stage_labels = ['Initial Research', 'Launch Preparation', 'Interstellar Travel', 'Landing Operations', 'Surface Exploration']
for line, label in zip(boxplots['medians'], stage_labels):
    line.set_label(label)

# Add legend
ax.legend(title='Mission Stages', fontsize=10, loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()