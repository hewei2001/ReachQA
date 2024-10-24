import matplotlib.pyplot as plt
import squarify  # For creating the tree map

# Define the economic sectors and their sub-categories with GDP contribution in billion dollars
sectors = {
    "Agriculture": {
        "Crop Production": 40,
        "Livestock": 30,
        "Forestry and Logging": 15
    },
    "Technology": {
        "Software Development": 70,
        "Hardware Manufacturing": 50
    },
    "Healthcare": {
        "Pharmaceuticals": 60,
        "Health Services": 55
    },
    "Education": {
        "Public Schools": 25,
        "Higher Education": 35
    },
    "Manufacturing": {
        "Automobile": 50,
        "Textiles": 20,
        "Machinery": 40
    },
    "Services": {
        "Banking": 70,
        "Real Estate": 65,
        "Tourism": 55
    }
}

# Prepare data for the tree map
labels = []
sizes = []
colors = []

# Assigning a color palette for visual appeal
color_palette = plt.cm.tab20c.colors

# Loop through each sector and its sub-categories to prepare labels, sizes, and colors
sector_index = 0
for sector, sub_sectors in sectors.items():
    for sub_sector, contribution in sub_sectors.items():
        labels.append(f"{sub_sector}\n({contribution}B)")
        sizes.append(contribution)
        colors.append(color_palette[sector_index % len(color_palette)])
    sector_index += 1

# Create the tree map
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, pad=3, text_kwargs={'fontsize': 10})

# Add title and adjust layout
plt.title('Economic Distribution of Econlandia\'s Sectors:\n2023 GDP Contribution', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')  # Turn off the axes for better visual appeal
plt.tight_layout()

# Show the tree map
plt.show()