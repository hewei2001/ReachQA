import matplotlib.pyplot as plt
import numpy as np

# Define the decades and utopian cities
decades = ['1970s', '1980s', '1990s', '2000s', '2010s']
cities = ['Harmony', 'Innovation', 'Balance']

# Define the renewable energy types and their respective adoption data (in arbitrary units)
solar_energy = np.array([
    [5, 10, 15, 20, 25],  # Harmony
    [3, 8, 14, 22, 30],   # Innovation
    [4, 7, 12, 18, 24]    # Balance
])

wind_energy = np.array([
    [10, 12, 15, 20, 30],  # Harmony
    [6, 10, 14, 18, 24],   # Innovation
    [5, 9, 13, 17, 22]     # Balance
])

hydro_energy = np.array([
    [8, 10, 13, 16, 20],   # Harmony
    [7, 10, 14, 19, 23],   # Innovation
    [9, 11, 14, 18, 21]    # Balance
])

# Plotting the area chart for Harmony
fig, ax = plt.subplots(figsize=(12, 8))

# Plot areas with transparency to distinguish them
ax.fill_between(decades, solar_energy[0], color='#FFD700', alpha=0.6, label='Solar Energy')
ax.fill_between(decades, wind_energy[0], color='#4682B4', alpha=0.6, label='Wind Energy')
ax.fill_between(decades, hydro_energy[0], color='#32CD32', alpha=0.6, label='Hydro Energy')

# Line plot to enhance trends
ax.plot(decades, solar_energy[0], color='#FFD700', linewidth=2)
ax.plot(decades, wind_energy[0], color='#4682B4', linewidth=2)
ax.plot(decades, hydro_energy[0], color='#32CD32', linewidth=2)

# Title, labels, and legend
ax.set_title("Renewable Energy Adoption in Harmony\n(1970s-2010s)", fontsize=16, fontweight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Energy Usage (Arbitrary Units)', fontsize=12)
ax.legend(loc='upper left', title="Energy Types", fontsize=10)

# Customize ticks and grid
ax.set_xticks(decades)
ax.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate the final points to highlight end values
for i, energy in enumerate([solar_energy, wind_energy, hydro_energy]):
    ax.annotate(
        str(energy[0][-1]),
        xy=(decades[-1], energy[0][-1]),
        xytext=(10, -10 * i),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', lw=1.5),
        fontsize=10,
        color='black'
    )

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()