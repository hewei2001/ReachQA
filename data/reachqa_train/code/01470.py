import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Energy consumption in TWh for each renewable source
solar_energy = [0.2, 0.4, 0.8, 1.2, 1.8, 2.5, 3.5, 4.5, 6, 8, 10, 13, 16, 20, 25, 31, 38, 46, 55, 65, 76]
wind_energy = [0.5, 0.9, 1.2, 1.7, 2.4, 3.2, 4.1, 5.2, 6.8, 8.5, 10.6, 13.1, 15.9, 19.2, 23.0, 27.5, 32.8, 38.9, 45.9, 53.8, 62.7]
hydro_energy = [3.5, 3.8, 4.1, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.6, 8.2, 8.9, 9.7, 10.5, 11.4, 12.4, 13.5, 14.7, 16.0, 17.4, 18.9]

# Stackplot for area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, solar_energy, wind_energy, hydro_energy, 
              labels=['Solar', 'Wind', 'Hydroelectric'], 
              colors=['#ffcc00', '#66b3ff', '#339966'], alpha=0.85)

# Titles and labels
plt.title("Evolution of Renewable Energy Adoption\nin Tech Valley (2000-2020)", fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption (TWh)', fontsize=12)

# Legend
plt.legend(loc='upper left', title="Renewable Energy Source")

# Gridlines
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure x-axis labels are readable
plt.xticks(rotation=45)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()