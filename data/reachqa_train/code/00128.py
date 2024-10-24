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
plt.figure(figsize=(12, 8))
box = plt.boxplot(data, vert=False, patch_artist=True, labels=civilizations, widths=0.6, notch=True, whis=[5, 95])

# Customize colors for the box plots
colors = ['lightcoral', 'lightblue', 'lightgreen']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customizing whiskers, caps, medians, and fliers
plt.setp(box['whiskers'], color='darkgrey', linewidth=1.5)
plt.setp(box['caps'], color='darkgrey', linewidth=1.5)
plt.setp(box['medians'], color='black', linewidth=1.5)
plt.setp(box['fliers'], marker='o', color='red', markersize=8)

# Add title and labels with line breaks for better readability
plt.title("Variability in Technology Adoption\n Across Ancient Civilizations", fontsize=16, fontweight='bold')
plt.xlabel("Years After Introduction", fontsize=12)
plt.ylabel("Civilizations", fontsize=12)

# Add a legend to map colors to technologies
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(legend_patches, technologies, loc='upper right', title='Technologies', fontsize=10)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the horizontal box chart
plt.show()