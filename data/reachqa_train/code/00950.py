import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2020
years = np.arange(1990, 2021)

# Hypothetical data for celestial body discoveries
exoplanets_discovered = np.array([
    0, 1, 0, 2, 5, 10, 8, 15, 20, 18, 25, 30, 40, 55, 60, 65, 70, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700
])
moons_discovered = np.array([
    2, 3, 5, 8, 9, 12, 15, 18, 21, 25, 30, 35, 38, 40, 42, 50, 55, 57, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 115, 120, 125
])
comets_discovered = np.array([
    10, 12, 15, 18, 20, 25, 28, 30, 35, 38, 40, 42, 45, 50, 55, 57, 60, 65, 68, 70, 75, 80, 82, 85, 90, 95, 100, 105, 110, 115, 120
])

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each category
ax.plot(years, exoplanets_discovered, label='Exoplanets', color='navy', marker='o', linewidth=2, linestyle='-')
ax.plot(years, moons_discovered, label='Moons', color='olive', marker='s', linewidth=2, linestyle='--')
ax.plot(years, comets_discovered, label='Comets', color='teal', marker='^', linewidth=2, linestyle='-.')

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Discoveries', fontsize=12)
ax.set_title('Cosmic Revelations:\nA Journey Through Space Discoveries (1990-2020)', fontsize=16, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(title='Celestial Bodies', loc='upper left', fontsize=10)

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()