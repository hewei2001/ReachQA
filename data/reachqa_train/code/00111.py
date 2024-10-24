import matplotlib.pyplot as plt
import numpy as np

# Extended Years from 2010 to 2030
years = np.arange(2010, 2031)

# Energy production data (in terawatt-hours, TWh)
# Adding more complexity with different energy sources and growth patterns
solar_energy = np.array([5, 7, 10, 15, 22, 33, 50, 65, 80, 100, 125, 150, 180, 210, 250, 300, 370, 450, 520, 600, 700])
wind_energy = np.array([10, 12, 20, 25, 35, 50, 70, 90, 120, 160, 200, 250, 310, 380, 460, 540, 620, 680, 740, 800, 900])
hydro_energy = np.array([40, 45, 50, 55, 60, 65, 70, 75, 78, 80, 82, 85, 88, 90, 92, 94, 96, 98, 100, 102, 105])
geothermal_energy = np.array([2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 30, 36, 43, 50, 60, 70, 85, 100, 120, 140])
biomass_energy = np.array([3, 4, 6, 8, 11, 15, 18, 22, 27, 33, 40, 48, 58, 70, 83, 97, 110, 125, 140, 160, 180])

# Stack the data
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy])

# Plotting the stacked area chart
plt.figure(figsize=(14, 10))

# Create the stacked area plot
plt.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass'], 
              colors=['#FFD700', '#87CEEB', '#32CD32', '#D2691E', '#8B4513'], alpha=0.85)

# Adding chart details
plt.title("The Rise of Green Energy:\nTwo Decades of Power Production Transformation in EcoLand", 
          fontsize=18, weight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Energy Production (TWh)", fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 2101, 200))
plt.legend(loc='upper left', fontsize=11, frameon=True)
plt.grid(alpha=0.3, linestyle='--')

# Add annotations for significant points
plt.annotate("Solar Surpasses Wind", xy=(2025, 600), xytext=(2020, 1500),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='darkorange'), fontsize=12)

plt.annotate("Rapid Growth in Geothermal", xy=(2030, 140), xytext=(2023, 700),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='brown'), fontsize=12)

# Adding a line plot for the total energy production
total_energy = energy_data.sum(axis=0)
plt.plot(years, total_energy, label='Total Energy Production', color='black', linestyle='--', linewidth=2)

# Ensure the layout is tidy and adjusted
plt.tight_layout()

# Display the plot
plt.show()