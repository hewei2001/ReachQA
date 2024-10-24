import matplotlib.pyplot as plt
import numpy as np

# Define architectural styles
styles = ['Gothic', 'Baroque', 'Neoclassical', 'Modern', 'Postmodern']

# Create data for each style across five criteria
# Values are on a scale from 0 to 100
data = {
    'Design Complexity': [90, 85, 60, 45, 75],
    'Ornamentation': [95, 90, 55, 30, 85],
    'Spatial Organization': [70, 75, 65, 85, 80],
    'Structural Innovation': [60, 70, 75, 90, 85],
    'Cultural Influence': [80, 85, 80, 75, 90],
}

# Convert data into a 2D array for plotting
data_values = np.array(list(data.values()))

# Define positions for each box
positions = np.arange(len(styles))

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))

# Plot each criterion as a horizontal box plot
for i, (criterion, values) in enumerate(data.items()):
    box = ax.boxplot(values, positions=[positions[i]], widths=0.6, vert=False,
                     patch_artist=True, notch=True,
                     boxprops=dict(facecolor=colors[i], color=colors[i], alpha=0.7),
                     whiskerprops=dict(color=colors[i]), capprops=dict(color=colors[i]),
                     medianprops=dict(color='black'))

# Set title and labels
ax.set_title('The Evolution of Architectural Styles:\nA Comparative Analysis of Design Complexity', fontsize=16, fontweight='bold')
ax.set_yticks(positions)
ax.set_yticklabels(data.keys(), fontsize=12)
ax.set_xlabel('Assessment Score (0-100)', fontsize=12)

# Add a grid to improve readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Create a legend
handles = [plt.Line2D([0], [0], color=colors[i], lw=2, label=styles[i]) for i in range(len(styles))]
ax.legend(handles=handles, title='Architectural Styles', loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to fit all elements
plt.tight_layout()

# Show the plot
plt.show()