import matplotlib.pyplot as plt
import numpy as np

# Define data for more buildings and more floors, and create additional metrics
buildings = [f'Building {chr(65+i)}' for i in range(6)]  # Buildings A to F
floors = [f'Floor {i+1}' for i in range(8)]  # Floors 1 to 8

# Average weekly air quality improvement percentages for each floor in each building
# Constructed with meaningful variations
air_quality_improvements = np.array([
    [12, 15, 18, 20, 25, 22, 24, 26],
    [10, 13, 16, 22, 24, 21, 23, 27],
    [14, 17, 19, 21, 23, 25, 26, 28],
    [11, 14, 17, 19, 21, 23, 22, 24],
    [13, 16, 20, 23, 22, 20, 21, 25],
    [15, 18, 21, 24, 26, 28, 29, 30]
])

# Additional metric: Energy savings percentage
energy_savings = np.array([
    [5, 7, 8, 10, 12, 11, 13, 15],
    [4, 6, 9, 11, 14, 12, 14, 16],
    [6, 8, 10, 12, 13, 14, 15, 17],
    [3, 5, 7, 9, 10, 11, 12, 14],
    [4, 6, 8, 11, 10, 12, 13, 15],
    [7, 9, 11, 13, 14, 16, 17, 18]
])

# Plot setup
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Heatmap for Air Quality Improvements
cax1 = axs[0].imshow(air_quality_improvements, cmap='YlGn', aspect='auto', interpolation='nearest')
axs[0].set_title('Air Quality Improvement (%)', fontsize=12, fontweight='bold', pad=10)
axs[0].set_xticks(np.arange(len(floors)))
axs[0].set_xticklabels(floors, fontsize=10, rotation=45, ha='right')
axs[0].set_yticks(np.arange(len(buildings)))
axs[0].set_yticklabels(buildings, fontsize=10)

# Annotate each cell with the air quality improvement value
for i in range(len(buildings)):
    for j in range(len(floors)):
        axs[0].text(j, i, f'{air_quality_improvements[i, j]}%', ha='center', va='center', color='black', fontsize=8)

# Add color bar for the first subplot
cbar1 = fig.colorbar(cax1, ax=axs[0], orientation='vertical', fraction=0.046, pad=0.04)
cbar1.set_label('Improvement (%)', rotation=270, labelpad=15)

# Second subplot: Heatmap for Energy Savings
cax2 = axs[1].imshow(energy_savings, cmap='BuPu', aspect='auto', interpolation='nearest')
axs[1].set_title('Energy Savings (%)', fontsize=12, fontweight='bold', pad=10)
axs[1].set_xticks(np.arange(len(floors)))
axs[1].set_xticklabels(floors, fontsize=10, rotation=45, ha='right')
axs[1].set_yticks(np.arange(len(buildings)))
axs[1].set_yticklabels(buildings, fontsize=10)

# Annotate each cell with the energy savings value
for i in range(len(buildings)):
    for j in range(len(floors)):
        axs[1].text(j, i, f'{energy_savings[i, j]}%', ha='center', va='center', color='black', fontsize=8)

# Add color bar for the second subplot
cbar2 = fig.colorbar(cax2, ax=axs[1], orientation='vertical', fraction=0.046, pad=0.04)
cbar2.set_label('Savings (%)', rotation=270, labelpad=15)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()