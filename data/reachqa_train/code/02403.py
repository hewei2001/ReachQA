import matplotlib.pyplot as plt
import numpy as np

# Define the regions and additional new regions for complexity
regions = ['Northern India', 'Southern India', 'Central Thailand', 
           'Southern Mexico', 'Ethiopian Highlands', 'Seoul, Korea', 'Busan, Korea']

# Expanded spice intensity data for each region (scale from 1 to 100)
spice_data = [
    [70, 85, 65, 80, 78, 90, 83, 88, 67, 85, 75, 88, 92, 79],  # Northern India
    [78, 82, 90, 92, 85, 88, 76, 85, 90, 80, 84, 86, 89, 91],  # Southern India
    [60, 75, 85, 70, 77, 82, 90, 88, 79, 80, 78, 85, 88, 92],  # Central Thailand
    [55, 60, 65, 70, 72, 78, 68, 75, 80, 82, 83, 81, 76, 74],  # Southern Mexico
    [45, 55, 60, 65, 58, 62, 64, 68, 70, 72, 66, 70, 74, 73],  # Ethiopian Highlands
    [50, 65, 75, 80, 70, 78, 85, 82, 74, 79, 80, 81, 83, 86],  # Seoul, Korea
    [55, 68, 73, 79, 82, 78, 88, 90, 85, 83, 84, 82, 80, 79]   # Busan, Korea
]

# Compute means for annotation
means = [np.mean(data) for data in spice_data]

# Create a figure with subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the horizontal boxplot
bplot = ax.boxplot(spice_data, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='#FFD700', color='#FF4500'),
                   whiskerprops=dict(color='#FF4500'),
                   capprops=dict(color='#FF4500'),
                   medianprops=dict(color='#FF6347', linewidth=2),
                   flierprops=dict(markerfacecolor='#FF4500', marker='o', markersize=8, alpha=0.6))

# Set y-tick labels and axis labels
ax.set_yticklabels(regions, fontsize=10)
ax.set_xlabel('Spice Intensity (1 to 100)', fontsize=12)
ax.set_title('Global Exploration of Spice Intensity Across Various Regions\nA Detailed Statistical Analysis', fontsize=16, fontweight='bold')

# Customize the appearance of each box with distinct colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#f6c7b6', '#f0e442']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Add the mean value as annotation for each region
for i, mean in enumerate(means):
    ax.annotate(f'Mean: {mean:.2f}', xy=(mean, i + 1), xytext=(mean + 1, i + 1 - 0.1),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()