import matplotlib.pyplot as plt
import numpy as np

# Define the decades
decades = ['2000s', '2010s', '2020s', '2030s', '2040s']

# Number of significant astronomical discoveries in each decade
discoveries = [15, 30, 45, 60, 80]

# Key breakthroughs in each decade
breakthroughs = [
    "First Exoplanet Atmosphere Detected",
    "Gravitational Waves Observed",
    "First Image of a Black Hole",
    "First Successful Asteroid Mining Mission",
    "Discovery of Interstellar Object"
]

# Years corresponding to breakthroughs
breakthrough_years = ['2004', '2015', '2019', '2035', '2047']

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 7))

# Plot line with markers
ax.plot(decades, discoveries, marker='o', linestyle='-', color='b', linewidth=2)

# Add annotations for key breakthroughs
for i, txt in enumerate(breakthroughs):
    ax.annotate(
        f'{txt} ({breakthrough_years[i]})',
        xy=(decades[i], discoveries[i]),
        xytext=(0, 15),  # Offset text to avoid overlapping
        textcoords='offset points',
        arrowprops=dict(facecolor='black', arrowstyle='->'),
        fontsize=9,
        ha='center'
    )

# Add labels and title
ax.set_xlabel('Decade', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Discoveries', fontsize=12, labelpad=10)
ax.set_title('Journey to the Stars:\nAstronomical Discoveries Over the Decades', fontsize=16, pad=20)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(['Astronomical Discoveries'], loc='upper left')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()