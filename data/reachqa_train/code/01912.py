import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Define the decades and data
decades = ['2000s', '2010s', '2020s', '2030s', '2040s']
discoveries = [15, 30, 45, 60, 80]

# Key breakthroughs and their years
breakthroughs = [
    "Exoplanet Atmosphere",
    "Gravitational Waves",
    "Black Hole Image",
    "Asteroid Mining",
    "Interstellar Object"
]
breakthrough_years = ['2004', '2015', '2019', '2035', '2047']

# Additional data: total number of missions
missions = [10, 20, 35, 55, 75]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot line with markers for discoveries
ax.plot(decades, discoveries, marker='o', linestyle='-', color='b', linewidth=2, label='Discoveries', markersize=8)

# Add a secondary line for missions
ax.plot(decades, missions, marker='s', linestyle='--', color='g', linewidth=2, label='Missions', markersize=8)

# Enhance grid
ax.grid(True, linestyle='--', color='gray', alpha=0.5)

# Annotations for key breakthroughs
for i, txt in enumerate(breakthroughs):
    ax.annotate(
        f'{txt} ({breakthrough_years[i]})',
        xy=(decades[i], discoveries[i]),
        xytext=(0, 10 if i % 2 == 0 else -30),  # Alternating text position to prevent overlap
        textcoords='offset points',
        arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
        fontsize=9,
        ha='center',
        bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.8)
    )

# Set labels and title
ax.set_xlabel('Decade', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Discoveries / Missions', fontsize=12, labelpad=10)
ax.set_title('Journey to the Stars:\nAstronomical Discoveries and Missions Over the Decades', fontsize=16, pad=20)

# Add a legend with customized styling
ax.legend(loc='upper left', fontsize=10, frameon=True, shadow=True, fancybox=True)

# Set background color for visual appeal
ax.set_facecolor('whitesmoke')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()