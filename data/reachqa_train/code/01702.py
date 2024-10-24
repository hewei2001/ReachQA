import matplotlib.pyplot as plt
import numpy as np

# Define the regions and seasons
regions = ["Downtown", "Suburbs", "Industrial", "Residential", "Commercial"]
seasons = ["Winter", "Spring", "Summer", "Fall"]

# Construct IAQI data for each region and season (values range from 0 to 100)
iaq_data = np.array([
    [65, 75, 55, 60],  # Downtown
    [80, 85, 70, 78],  # Suburbs
    [50, 45, 55, 52],  # Industrial
    [70, 78, 82, 75],  # Residential
    [60, 65, 58, 62]   # Commercial
])

# Rotate the data to align the regions along y-axis and seasons along x-axis
iaq_data = np.rot90(iaq_data)

# Create a figure and axis for the heatmap
fig, ax = plt.subplots(figsize=(10, 6))

# Create the heatmap using imshow with appropriate colormap and aspect
cax = ax.imshow(iaq_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Add colorbar with label
cbar = fig.colorbar(cax)
cbar.set_label('Indoor Air Quality Index', rotation=270, labelpad=15, fontsize=12)

# Set labels and titles
ax.set_yticks(np.arange(len(seasons)))
ax.set_xticks(np.arange(len(regions)))
ax.set_yticklabels(seasons, fontsize=10)
ax.set_xticklabels(regions, fontsize=10)
ax.set_title('Indoor Air Quality Index\nAcross Urban Regions by Season', fontsize=14, fontweight='bold', pad=15)

# Rotate the x-tick labels to prevent overlap
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(seasons)):
    for j in range(len(regions)):
        ax.text(j, i, iaq_data[i, j], ha='center', va='center', color='black', fontsize=9)

# Enhance layout
plt.tight_layout()

# Show the plot
plt.show()