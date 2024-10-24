import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Sectors
sectors = ['Transportation', 'Industry', 'Residential', 'Commercial', 'Agriculture', 'Public Services']

# Percentage of energy from different renewable sources
# Data is given as [Solar, Wind, Hydropower, Biomass]
renewable_data = np.array([
    [20, 30, 10, 5],  # Transportation
    [10, 25, 5, 10],  # Industry
    [30, 20, 15, 10],  # Residential
    [25, 20, 20, 5],  # Commercial
    [15, 10, 5, 20],  # Agriculture
    [5, 25, 30, 10]   # Public Services
])

# Create a new figure with specific size
fig, ax = plt.subplots(figsize=(14, 10))

# Define colors and patterns for visual distinction
colors = ['#FFD700', '#87CEEB', '#98FB98', '#CD853F']
patterns = ['/', '\\', '|', '-']

# Stacking the bars horizontally with added textures
bars = []
left_positions = np.zeros(len(sectors))
for i in range(renewable_data.shape[1]):
    bar = ax.barh(sectors, renewable_data[:, i], left=left_positions, 
                  color=colors[i], hatch=patterns[i], edgecolor='black')
    left_positions += renewable_data[:, i]
    bars.append(bar)

# Adding percentage labels on the bars with improved formatting
for i, sector in enumerate(sectors):
    for j in range(renewable_data.shape[1]):
        width = renewable_data[i, j]
        if width > 0:
            ax.text(np.sum(renewable_data[i, :j]) + width / 2, i, f'{width}%', 
                    ha='center', va='center', color='black', fontsize=9, weight='bold')

# Title and labels with improved readability
ax.set_xlabel('Percentage of Total Energy from Renewable Sources', fontsize=12)
ax.set_title('Renewable Energy Adoption by Sector in 2030\nChallenges and Opportunities', 
             fontsize=18, weight='bold', pad=20)

# X-axis range fixed to 0-100%
ax.set_xlim(0, 100)

# Custom legend creation with patches to match patterns
legend_labels = ['Solar', 'Wind', 'Hydropower', 'Biomass']
handles = [mpatches.Patch(facecolor=colors[i], edgecolor='black', hatch=patterns[i], label=legend_labels[i])
           for i in range(len(legend_labels))]
ax.legend(handles=handles, loc='upper right', fontsize=10, title='Renewable Sources', title_fontsize='13')

# Background grid and layout adjustments
ax.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()