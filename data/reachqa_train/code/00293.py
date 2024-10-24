import matplotlib.pyplot as plt
import numpy as np

# Data representing the percentage of total energy consumption from solar and wind in urban areas (2000-2023)
years = np.arange(2000, 2024)

solar_energy_percentage = [
    0.5, 0.7, 1.0, 1.5, 2.3, 3.2, 4.5, 6.0, 8.0, 10.0, 
    12.5, 15.3, 18.0, 21.0, 25.0, 29.0, 34.0, 40.0, 46.0, 52.0, 
    59.0, 67.0, 74.0, 80.0
]

wind_energy_percentage = [
    1.0, 1.2, 1.6, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 
    10.0, 12.0, 14.5, 17.0, 20.0, 24.0, 29.0, 35.0, 41.0, 48.0, 
    56.0, 64.0, 72.0, 78.0
]

# Plot configuration
plt.figure(figsize=(12, 6))

# Plotting the data
plt.plot(years, solar_energy_percentage, label='Solar Energy', color='orange', marker='o', linestyle='-', linewidth=2)
plt.plot(years, wind_energy_percentage, label='Wind Energy', color='green', marker='s', linestyle='--', linewidth=2)

# Titles and labels
plt.title('The Rise of Renewable Energy Adoption\nin Urban Areas (2000-2023)', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Total Energy Consumption (%)', fontsize=12)

# Enhancing grid for readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adding a legend
plt.legend(loc='upper left', fontsize=10)

# Highlighting significant trends with annotations
plt.axvline(2010, color='grey', linestyle='--', alpha=0.5)
plt.text(2011, 20, 'Increased adoption post-2010', fontsize=9, color='black', rotation=90)

plt.axvline(2020, color='grey', linestyle='--', alpha=0.5)
plt.text(2021, 60, 'Rapid growth in 2020s', fontsize=9, color='black', rotation=90)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()