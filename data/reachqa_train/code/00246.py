import matplotlib.pyplot as plt
import numpy as np

# Define packaging materials and their waste reduction data (in tons)
packaging_materials = ['Biodegradable Plastics', 'Recyclable Paper',
                       'Plant-Based Polymers', 'Compostable Packaging']

# Manually crafted waste reduction data, ensuring a good range for box plots
biodegradable_plastics = [30, 35, 40, 40, 45, 50, 50, 55, 60, 65, 70]
recyclable_paper = [25, 27, 29, 29, 31, 33, 33, 35, 37, 39, 41, 45]
plant_based_polymers = [20, 23, 23, 25, 28, 30, 30, 32, 35, 37, 40]
compostable_packaging = [15, 18, 18, 20, 23, 25, 25, 28, 30, 33, 38]

# Organize data in a list of arrays
data = [np.array(biodegradable_plastics), np.array(recyclable_paper),
        np.array(plant_based_polymers), np.array(compostable_packaging)]

# Create a horizontal box plot
plt.figure(figsize=(12, 7))
box = plt.boxplot(data, vert=False, patch_artist=True, labels=packaging_materials,
                  notch=True, showfliers=False, whis=1.5)

# Customize colors and styles for each box
colors = ['#76c7c0', '#f6b76b', '#8fbc8f', '#d8bfd8']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    
# Set whisker and cap colors
for whisker in box['whiskers']:
    whisker.set(color='#8b8b8b', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='#8b8b8b', linewidth=1.5)
for median in box['medians']:
    median.set(color='#ff6f61', linewidth=2)

# Adding title and axis labels
plt.title('Eco-friendly Packaging Materials Impact on Plastic Waste Reduction\n(Annual Distribution)', fontsize=14, fontweight='bold')
plt.xlabel('Reduction in Plastic Waste (Tons)', fontsize=12)
plt.ylabel('Packaging Materials', fontsize=12)

# Add grid for easier interpretation
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()