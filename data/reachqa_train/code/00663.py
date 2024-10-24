import matplotlib.pyplot as plt
import numpy as np

# Define months
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Monthly energy generation data (in GWh) for each renewable source
solar_energy = np.array([50, 60, 75, 85, 100, 120, 135, 130, 115, 95, 75, 55])
wind_energy = np.array([80, 85, 90, 95, 105, 110, 120, 125, 130, 125, 100, 90])
hydro_energy = np.array([110, 100, 115, 135, 145, 140, 150, 155, 145, 130, 115, 110])
biomass_energy = np.array([35, 37, 40, 42, 45, 47, 50, 48, 45, 42, 38, 35])

# Stack the data for area plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

# Plotting the area chart
plt.figure(figsize=(14, 8))

plt.stackplot(months, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], 
              colors=['#f1c40f', '#3498db', '#1abc9c', '#e67e22'], alpha=0.8)

# Add titles and labels
plt.title('Emerging Trends in Renewable Energy Generation:\nTracking Monthly Output in 2023', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Energy Generation (GWh)', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(loc='upper left', fontsize=12)

# Add grid lines for better readability
plt.grid(alpha=0.3, linestyle='--', linewidth=0.7)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()