import matplotlib.pyplot as plt
import numpy as np

# Define the years in 5-year increments
years = np.arange(1980, 2025, 5)

# Number of discoveries made in each category over the years
# Increasing complexity and adding more categories
exoplanets = np.array([0, 1, 3, 5, 10, 20, 40, 300, 1000])
galaxies = np.array([2000, 2500, 3000, 3500, 5000, 7500, 10000, 15000, 25000])
nebulae = np.array([500, 550, 600, 650, 700, 750, 800, 850, 900])
black_holes = np.array([10, 15, 20, 25, 30, 45, 60, 90, 120])
supernovae = np.array([50, 60, 70, 80, 100, 150, 200, 300, 450])
asteroids = np.array([10000, 12000, 14000, 18000, 23000, 30000, 38000, 47000, 58000])
comets = np.array([100, 110, 115, 130, 150, 170, 200, 250, 300])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Plot each line with different styles
ax.plot(years, exoplanets, marker='o', linestyle='-', linewidth=2, label='Exoplanets', color='#FF5733')
ax.plot(years, galaxies, marker='s', linestyle='--', linewidth=2, label='Galaxies', color='#33FF57')
ax.plot(years, nebulae, marker='^', linestyle='-.', linewidth=2, label='Nebulae', color='#3357FF')
ax.plot(years, black_holes, marker='D', linestyle=':', linewidth=2, label='Black Holes', color='#FF33A1')
ax.plot(years, supernovae, marker='*', linestyle='-', linewidth=2, label='Supernovae', color='#33FFF2')
ax.plot(years, asteroids, marker='P', linestyle='--', linewidth=2, label='Asteroids', color='#FFA733')
ax.plot(years, comets, marker='X', linestyle='-.', linewidth=2, label='Comets', color='#A1FF33')

# Title and labels
ax.set_title("Astronomical Discoveries Over Time:\nComplex Growth Patterns in the Cosmos", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Discoveries", fontsize=14)

# Logarithmic scale for the y-axis
ax.set_yscale('log')

# Grid
ax.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(title='Type of Discovery', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to make room for elements
plt.tight_layout()

# Display the plot
plt.show()