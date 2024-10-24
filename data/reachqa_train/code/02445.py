import matplotlib.pyplot as plt
import numpy as np

# Define data for three buildings, each with five floors
buildings = ['Building A', 'Building B', 'Building C']
floors = ['Floor 1', 'Floor 2', 'Floor 3', 'Floor 4', 'Floor 5']

# Average weekly air quality improvement percentages for each floor in each building
air_quality_improvements = np.array([
    [12, 15, 18, 20, 25],  # Building A
    [10, 13, 16, 22, 24],  # Building B
    [14, 17, 19, 21, 23]   # Building C
])

# Create the heat map
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(air_quality_improvements, cmap='YlGn', aspect='auto', interpolation='nearest')

# Add a color bar to provide reference for the values
cbar = plt.colorbar(cax)
cbar.set_label('Air Quality Improvement (%)', rotation=270, labelpad=15)

# Set axis labels and title
ax.set_xticks(np.arange(len(floors)))
ax.set_xticklabels(floors, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(buildings)))
ax.set_yticklabels(buildings, fontsize=10)

ax.set_title('Sustainability in Oceanview: Enhancing Air Quality\nwith Indoor Plants', fontsize=14, fontweight='bold', pad=20)

# Annotate each cell with the air quality improvement value
for i in range(len(buildings)):
    for j in range(len(floors)):
        ax.text(j, i, f'{air_quality_improvements[i, j]}%', ha='center', va='center', color='black', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()