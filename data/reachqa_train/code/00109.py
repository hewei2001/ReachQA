import matplotlib.pyplot as plt
import squarify
import numpy as np

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

# Related growth data for overlay plot (hypothetical, directly constructed)
years = np.arange(2010, 2021)
growth_trends = {
    "Oil Painting": [15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 28],
    "Digital Painting": [10, 12, 14, 15, 17, 20, 22, 24, 26, 28, 30],
    "Virtual Reality Art": [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12]
}

# Prepare treemap data
labels = []
sizes = []
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#ff6666", "#c2f0c2", "#c2d6f0"]
for category, subcategories in mediums.items():
    for subcategory, size in subcategories.items():
        labels.append(f"{subcategory}\n({size})")
        sizes.append(size)

# Create figure and axis for treemap
fig, ax1 = plt.subplots(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=colors[:len(labels)], alpha=0.8, ax=ax1, edgecolor='black', linewidth=1)
ax1.set_title("Artistic Mediums of the 21st Century\nGrowth and Influence", fontsize=16, fontweight='bold', pad=20)
ax1.axis('off')

# Add overlay plot (Growth trends)
ax2 = ax1.twinx()  # Create a secondary y-axis
for medium, growth in growth_trends.items():
    ax2.plot(years, growth, marker='o', linestyle='-', label=medium)

# Overlay plot configurations
ax2.set_ylabel('Growth in Interest (%)', fontsize=12)
ax2.set_xlabel('Years', fontsize=12)
ax2.grid(False)
ax2.legend(title='Growth Trends', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()