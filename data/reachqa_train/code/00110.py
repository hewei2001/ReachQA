import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Energy production data (in terawatt-hours, TWh)
# Initial values for 2013 and a consistent growth pattern are used for simplicity
solar_energy = np.array([10, 15, 22, 33, 50, 65, 80, 100, 125, 150, 180])  # Growth in solar energy
wind_energy = np.array([20, 25, 35, 50, 70, 90, 120, 160, 200, 250, 310])  # Growth in wind energy
hydro_energy = np.array([50, 55, 60, 65, 70, 75, 78, 80, 82, 85, 88])     # Stable growth in hydropower

# Stack the data
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))

# Create the stacked area plot
plt.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower'], 
              colors=['#FFD700', '#87CEEB', '#32CD32'], alpha=0.8)

# Adding chart details
plt.title("The Rise of Green Energy:\nA Decade of Power Production Transformation in EcoLand", 
          fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Energy Production (TWh)", fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 601, 50))
plt.legend(loc='upper left', fontsize=12, frameon=True)
plt.grid(alpha=0.3, linestyle='--')

# Add annotations for significant points
plt.annotate("Significant Solar Expansion", xy=(2018, 80), xytext=(2015, 220),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='darkorange'), fontsize=12)

plt.annotate("Wind Energy Surpasses Hydropower", xy=(2021, 250), xytext=(2017, 400),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='blue'), fontsize=12)

# Ensure the layout is tidy and adjusted
plt.tight_layout()

# Display the plot
plt.show()