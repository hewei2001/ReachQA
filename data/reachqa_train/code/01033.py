import matplotlib.pyplot as plt
import numpy as np

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# Energy data in megawatts (MW)
solar_energy = np.array([20, 25, 35, 50, 70, 90, 120, 160, 210, 270, 340])
wind_energy = np.array([15, 20, 30, 45, 60, 80, 105, 140, 180, 230, 290])
hydro_energy = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Calculate cumulative energy for stacking
total_energy = solar_energy + wind_energy + hydro_energy

# Plotting the area chart
plt.figure(figsize=(14, 8))

# Stacked area plot
plt.stackplot(years, solar_energy, wind_energy, hydro_energy,
              labels=['Solar Energy', 'Wind Energy', 'Hydro Energy'],
              colors=['#FFD700', '#1E90FF', '#32CD32'],
              alpha=0.7)

# Title and labels
plt.title("Renewable Energy Adoption in GreenCity\nTransition from 2015 to 2025", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Energy Contribution (MW)", fontsize=14)

# Legend
plt.legend(loc='upper left', title='Energy Sources', fontsize=12)

# Annotate key trends
plt.annotate('Solar energy peak', xy=(2024, 700), xytext=(2021, 780),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.annotate('Wind energy surge', xy=(2023, 580), xytext=(2019, 650),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Customize x-axis labels
plt.xticks(years, rotation=45)

# Grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent text cutoff
plt.tight_layout()

# Show the plot
plt.show()