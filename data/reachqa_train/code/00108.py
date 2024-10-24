import matplotlib.pyplot as plt
import squarify

# Define data for artistic mediums
mediums = {
    "Traditional Mediums": {
        "Oil Painting": 15,
        "Watercolor": 10,
        "Sculpture": 12
    },
    "Digital Mediums": {
        "Digital Painting": 20,
        "3D Modeling": 18,
        "Animation": 17
    },
    "Emerging Mediums": {
        "Virtual Reality Art": 8,
        "Augmented Reality": 5
    }
}

# Flatten data for plotting
labels = []
sizes = []
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#ff6666", "#c2f0c2", "#c2d6f0"]
color_index = 0

# Traverse the data to extract labels and sizes
for category, subcategories in mediums.items():
    for subcategory, size in subcategories.items():
        labels.append(f"{subcategory}\n({size})")
        sizes.append(size)

# Create the tree map
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors[:len(labels)], alpha=0.8, ax=ax, edgecolor='black', linewidth=1)

# Configure the plot
plt.title("Artistic Mediums of the 21st Century:\nA Composition of Influence", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')

# Adjust layout to accommodate labels
plt.tight_layout()

# Display the plot
plt.show()