import matplotlib.pyplot as plt
import numpy as np

# Ecosystems and their respective number of unique species
ecosystems = ['Amazon Rainforest', 'Coral Reefs', 'Deep Sea', 'Alpine Meadows', 'Wetlands']
unique_species_counts = [390, 230, 150, 80, 110]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Bar colors, distinct for each ecosystem
colors = ['#4CAF50', '#FFA07A', '#87CEEB', '#FFD700', '#8FBC8F']

# Positions for bars
positions = np.arange(len(ecosystems))

# Plot the bar chart
bars = ax.barh(positions, unique_species_counts, color=colors, edgecolor='black', height=0.6)

# Set the y-ticks to the ecosystem names
ax.set_yticks(positions)
ax.set_yticklabels(ecosystems, fontsize=12)

# Add title and labels
ax.set_title('Biodiversity Richness\nAcross Different Ecosystems', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Number of Unique Species', fontsize=14, labelpad=15)
ax.set_ylabel('Ecosystems', fontsize=14, labelpad=15)

# Add a grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate each bar with the number of unique species
for bar in bars:
    width = bar.get_width()
    ax.text(width + 10, bar.get_y() + bar.get_height()/2, f'{width}', va='center', ha='left', fontsize=12, fontweight='bold', color='black')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()