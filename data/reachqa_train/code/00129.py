import matplotlib.pyplot as plt
import numpy as np

# Define the ancient civilizations
civilizations = ['Egyptians', 'Mesopotamians', 'Indus Valley']

# Adjusted data representing technology adoption rates (in years)
# Reflecting variability, each list contains years for: wheel, metallurgy, writing, irrigation
egyptians = [35, 60, 45, 20]
mesopotamians = [15, 40, 50, 30]
indus_valley = [20, 70, 55, 40]

# Create data structure for box plot
data = [egyptians, mesopotamians, indus_valley]

# Define labels for technologies
technologies = ['Wheel', 'Metallurgy', 'Writing', 'Irrigation']

# Plot the horizontal box chart
plt.figure(figsize=(14, 9))
box = plt.boxplot(data, vert=False, patch_artist=True, labels=civilizations, widths=0.6, notch=True, whis=[5, 95])

# Enhance colors with a gradient effect
colors = ['#fdae61', '#abd9e9', '#2c7bb6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customizing whiskers, caps, medians, and fliers
plt.setp(box['whiskers'], color='darkgrey', linewidth=1.5)
plt.setp(box['caps'], color='darkgrey', linewidth=1.5)
plt.setp(box['medians'], color='black', linewidth=1.5)
plt.setp(box['fliers'], marker='o', color='red', markersize=8)

# Add mean value annotations
means = [np.mean(group) for group in data]
for i, mean in enumerate(means):
    plt.text(mean + 1, i + 1, f'{mean:.1f}', verticalalignment='center', fontsize=10, color='black')

# Add jittered scatter plot for individual data points
for i, group in enumerate(data):
    y = np.random.normal(i + 1, 0.02, size=len(group))
    plt.plot(group, y, 'o', color='grey', alpha=0.6)

# Add title and labels with line breaks for better readability
plt.title("Variability in Technology Adoption\n Across Ancient Civilizations", fontsize=16, fontweight='bold')
plt.xlabel("Years After Introduction", fontsize=12)
plt.ylabel("Civilizations", fontsize=12)

# Add a legend to map colors to technologies with subtle symbolic icons
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(legend_patches, technologies, loc='upper right', title='Technologies', fontsize=10)

# Enhance layout and add grid
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the horizontal box chart
plt.show()