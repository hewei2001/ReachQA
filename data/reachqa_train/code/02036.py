import matplotlib.pyplot as plt
import numpy as np

# Technology sectors and their respective innovation indices over the last decade
sectors = ["AI", "Robotics", "Quantum", "Biotech", "Renewables"]
innovation_data = [
    [65, 72, 78, 85, 90, 92, 95, 97, 100, 105],  # Artificial Intelligence
    [50, 55, 62, 65, 70, 78, 80, 82, 85, 88],    # Robotics
    [30, 35, 42, 50, 60, 70, 75, 80, 85, 90],    # Quantum Computing
    [70, 72, 74, 75, 77, 80, 85, 88, 90, 92],    # Biotech
    [40, 50, 58, 65, 72, 80, 85, 89, 93, 95],    # Renewable Energy
]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a vertical box plot for the innovation indices
bp = ax.boxplot(innovation_data, vert=True, patch_artist=True, 
                notch=True, showmeans=True, meanline=True,
                meanprops=dict(linestyle='--', linewidth=2.5, color='orange'))

# Customize the appearance of the boxes
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
hatches = ['/', '\\', '|', '-', '+']
for patch, color, hatch in zip(bp['boxes'], colors, hatches):
    patch.set(facecolor=color, hatch=hatch, alpha=0.7)

# Enhance the medians, whiskers, and caps
for median in bp['medians']:
    median.set(color='blue', linewidth=3)
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=2, linestyle='--')
for cap in bp['caps']:
    cap.set(color='black', linewidth=2)

# Set title and labels
ax.set_title('Annual Innovation Indices in Technology Sectors\nA Decade of Progress', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Technology Sector', fontsize=13)
ax.set_ylabel('Innovation Index', fontsize=13)
ax.set_xticks(np.arange(1, len(sectors) + 1))
ax.set_xticklabels(sectors, fontsize=12, rotation=15)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend to explain the box plot components
boxplot_elements = [bp['means'][0], bp['medians'][0], bp['whiskers'][0]]
ax.legend(boxplot_elements, ['Mean', 'Median', 'Whisker'], loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()