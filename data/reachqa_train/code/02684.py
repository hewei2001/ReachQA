import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2020, 2051)

# Create fictional data for renewable energy adoption (in TWh)
solar_energy = np.array([10, 15, 20, 28, 36, 45, 55, 68, 82, 97, 114, 132, 151, 171, 192, 215, 239, 264, 290, 317, 345, 374, 404, 435, 467, 500, 534, 569, 605, 642, 680])
wind_energy = np.array([30, 36, 43, 51, 60, 70, 82, 95, 109, 125, 142, 160, 180, 201, 223, 246, 270, 295, 321, 348, 376, 405, 435, 466, 498, 531, 565, 600, 636, 673, 711])
hydro_energy = np.array([40, 42, 45, 49, 54, 60, 67, 75, 84, 94, 105, 117, 130, 144, 159, 175, 192, 210, 229, 249, 270, 292, 315, 339, 364, 390, 417, 445, 474, 504, 535])
biomass_energy = np.array([5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95, 109, 124, 140, 157, 175, 194, 214, 235, 257, 280, 304, 329, 355, 382, 410, 439, 469, 500])
geothermal_energy = np.array([3, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 94, 108, 123, 139, 156, 174, 193, 213, 234, 256, 279, 303, 328, 354, 381, 409, 438, 468])

# Plotting setup
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked area chart
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy, 
             labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'], 
             colors=['#FFD700', '#87CEEB', '#32CD32', '#8B4513', '#FF4500'], alpha=0.8)

# Title and labels
ax.set_title("The Evolution of Renewable Energy Adoption\n(2020-2050)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

# Legend configuration
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, frameon=False)

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adjusting x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()