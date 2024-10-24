import matplotlib.pyplot as plt

# Define the regions
regions = ['India', 'Thailand', 'Mexico', 'Ethiopia', 'Korea']

# Define spice intensity data for each region (scale from 1 to 100)
spice_data = [
    [70, 85, 65, 80, 78, 90, 83, 88, 67, 85],  # India
    [60, 75, 85, 70, 77, 82, 90, 88, 79, 80],  # Thailand
    [55, 60, 65, 70, 72, 78, 68, 75, 80, 82],  # Mexico
    [45, 55, 60, 65, 58, 62, 64, 68, 70, 72],  # Ethiopia
    [50, 65, 75, 80, 70, 78, 85, 82, 74, 79]   # Korea
]

# Create a figure and a horizontal boxplot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the boxplot horizontally
bplot = ax.boxplot(spice_data, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='#FFD700', color='#FF4500'),
                   whiskerprops=dict(color='#FF4500'),
                   capprops=dict(color='#FF4500'),
                   medianprops=dict(color='#FF6347', linewidth=2),
                   flierprops=dict(markerfacecolor='#FF4500', marker='o', markersize=8, alpha=0.6))

# Set y-tick labels
ax.set_yticklabels(regions)
ax.set_xlabel('Spice Intensity (1 to 100)', fontsize=12)
ax.set_title('Culinary Adventures: Exploration of\nGlobal Spice Intensity', fontsize=14, fontweight='bold')

# Customize the appearance of each box with distinct colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()