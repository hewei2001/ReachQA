import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy production data for each renewable energy source
years = np.arange(2010, 2021)

solar_energy = [30, 40, 55, 70, 90, 120, 150, 180, 210, 250, 300]
wind_energy = [50, 60, 65, 75, 85, 100, 110, 130, 140, 160, 180]
hydro_energy = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
bio_energy = [20, 25, 30, 35, 40, 50, 55, 60, 65, 70, 75]

# Combine the data into a single array for plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bio_energy])

# Create a figure and a set of subplots
plt.figure(figsize=(12, 7))

# Plot the stacked area chart
plt.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Bioenergy'],
              colors=['#FFD700', '#87CEEB', '#8FBC8F', '#FF6347'])

# Adding title and labels
plt.title('Annual Renewable Energy Production by Source\nin Emerald City (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (GWh)', fontsize=12)

# Add legend to the plot
plt.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Add a grid for visual aid
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent clipping of tick-labels, legend and title
plt.tight_layout()

# Display the plot
plt.show()