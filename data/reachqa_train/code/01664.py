import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Solar capacity data (in GW) for different regions over the years
# These numbers are illustrative and crafted to show growth patterns
north_america = np.array([2, 2, 3, 4, 5, 7, 9, 12, 15, 20, 26, 33, 40, 50, 65, 80, 100, 125, 150, 175, 200])
europe = np.array([1, 2, 3, 5, 8, 12, 18, 25, 35, 50, 70, 95, 120, 150, 185, 220, 260, 300, 350, 410, 470])
asia = np.array([3, 4, 6, 8, 12, 18, 27, 38, 52, 70, 90, 115, 145, 180, 220, 270, 320, 380, 450, 530, 620])
africa = np.array([0, 0, 0, 0, 1, 2, 4, 6, 9, 13, 18, 24, 32, 42, 55, 70, 90, 110, 135, 160, 190])
latin_america = np.array([0, 1, 2, 3, 5, 8, 11, 15, 20, 26, 33, 41, 50, 60, 75, 90, 110, 130, 155, 180, 210])

# Plotting the area chart using fill_between
plt.figure(figsize=(14, 8))
plt.fill_between(years, north_america, label='North America', color='#ffd700', alpha=0.8)
plt.fill_between(years, north_america + europe, north_america, label='Europe', color='#4caf50', alpha=0.8)
plt.fill_between(years, north_america + europe + asia, north_america + europe, label='Asia', color='#2196f3', alpha=0.8)
plt.fill_between(years, north_america + europe + asia + africa, north_america + europe + asia, label='Africa', color='#ff5722', alpha=0.8)
plt.fill_between(years, north_america + europe + asia + africa + latin_america, north_america + europe + asia + africa, 
                 label='Latin America', color='#9c27b0', alpha=0.8)

# Title and labels
plt.title("Solar Odyssey: The Growth of Renewable Energy Across Continents\n(2000-2020)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Installed Solar Energy Capacity (GW)", fontsize=12)

# Customize legend
plt.legend(loc='upper left', title="Regions", fontsize=10, title_fontsize='12')

# Enhancing the grid and readability
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(years, rotation=45, ha='right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()