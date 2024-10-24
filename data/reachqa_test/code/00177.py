import matplotlib.pyplot as plt
import numpy as np

# Enhanced data for archaeological discoveries categorized by artifact type
# Numbers are in hundreds of artifacts discovered
discoveries_data = {
    'Ancient Egypt': {'Tools': 20, 'Pottery': 25, 'Jewelry': 27},
    'Mesopotamia': {'Tools': 15, 'Pottery': 20, 'Jewelry': 20},
    'The Indus Valley': {'Tools': 14, 'Pottery': 13, 'Jewelry': 15},
    'Ancient China': {'Tools': 22, 'Pottery': 23, 'Jewelry': 20},
    'Mesoamerica': {'Tools': 10, 'Pottery': 15, 'Jewelry': 13},
    'The Inca Empire': {'Tools': 8, 'Pottery': 10, 'Jewelry': 10}
}

# Prepare data for stacked histogram
civilizations = list(discoveries_data.keys())
artifact_types = list(next(iter(discoveries_data.values())).keys())

# Create stacked data arrays for each type of artifact
stacked_data = {artifact: np.array([civ_data[artifact] for civ_data in discoveries_data.values()]) for artifact in artifact_types}

# Define bin edges for the histogram
bins = np.arange(0, 81, 10)

# Create the stacked histogram
plt.figure(figsize=(14, 8))
bottoms = np.zeros(len(civilizations))
colors = {'Tools': 'skyblue', 'Pottery': 'orange', 'Jewelry': 'green'}

# Plot each category on top of the previous ones
for artifact in artifact_types:
    plt.bar(civilizations, stacked_data[artifact], bottom=bottoms, label=artifact, color=colors[artifact])
    bottoms += stacked_data[artifact]

# Calculate and plot mean discovery line
mean_discovery = np.mean([sum(discoveries.values()) for discoveries in discoveries_data.values()])
plt.axhline(y=mean_discovery, color='red', linestyle='--', label='Mean Discoveries')

# Add labels, title, and legend
plt.title("Distribution of Archaeological Discoveries by Artifact Type in Ancient Civilizations\n(Last Decade)", fontsize=16, fontweight='bold')
plt.xlabel('Ancient Civilizations', fontsize=12)
plt.ylabel('Number of Discoveries (Hundreds of Artifacts)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Artifact Types')

# Annotate bars with discovery counts
for idx, civ in enumerate(civilizations):
    total = 0
    for artifact, values in stacked_data.items():
        total += values[idx]
        plt.text(idx, total - values[idx]/2, f'{values[idx]}', ha='center', va='center', color='white', fontsize=10)

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()