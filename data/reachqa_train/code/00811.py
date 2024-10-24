import numpy as np
import matplotlib.pyplot as plt

# Define months and celestial body categories
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
bodies = ["Planets", "Stars", "Galaxies", "Comets"]

# Visibility data in hours each month
planets_visibility = [5, 6, 7, 8, 10, 12, 11, 9, 8, 7, 6, 5]
stars_visibility = [8, 9, 10, 11, 12, 14, 14, 13, 11, 10, 9, 8]
galaxies_visibility = [2, 3, 4, 6, 7, 7, 6, 5, 4, 3, 2, 2]
comets_visibility = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1, 1]

# Stack the visibility data
visibility_data = np.array([planets_visibility, stars_visibility, galaxies_visibility, comets_visibility])

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(months, visibility_data, labels=bodies, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Title and labels
ax.set_title('Visibility of Celestial Bodies Throughout the Year', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Hours of Visibility', fontsize=12)

# Customize x-ticks to avoid overlap
plt.xticks(rotation=45, ha='right')

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)

# Adding a legend
ax.legend(loc='upper right', fontsize=10, title='Celestial Bodies', title_fontsize='12')

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()