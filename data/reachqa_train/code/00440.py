import matplotlib.pyplot as plt
import numpy as np

# Define research categories and the number of missions for each category
categories = [
    'Planetary Exploration', 'Human Health',
    'Astrophysics', 'Satellite Tech', 'Earth Sciences',
    'Exoplanet Studies', 'Space Physics'
]
missions_count = np.array([50, 30, 45, 25, 40, 15, 35])

# Calculate number of categories
num_categories = len(categories)

# Define angles for the rose chart (in polar coordinates)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

# Repeat the first angle and count to close the chart
angles += angles[:1]
missions_count = np.append(missions_count, missions_count[0])

# Plotting setup
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Colors for each category
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#9370DB', '#FF69B4', '#FF4500']

# Create the rose chart
bars = ax.bar(angles[:-1], missions_count[:-1], width=2*np.pi/num_categories, 
              color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)

# Add labels at each angle
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, fontweight='bold')

# Title with a backstory
ax.set_title("Diversity of Research Objectives in Space Missions\n(1990-2020)", 
             fontsize=14, fontweight='bold', loc='center', pad=20)

# Set radial limits and grid
ax.set_ylim(0, max(missions_count) + 10)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Legend configuration
ax.legend(bars, categories, title="Research Focus", loc="upper right", bbox_to_anchor=(1.1, 1.1), fontsize=9)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()