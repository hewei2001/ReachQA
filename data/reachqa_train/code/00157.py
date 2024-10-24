import matplotlib.pyplot as plt
import numpy as np

# Define the time range for a century
years = np.arange(1900, 2000)

# Growth data for eco-industries over a century
# Modified for clarity and realistic growth patterns
organic_farming = 5 + np.linspace(1, 10, len(years))
solar_energy = np.array([0 if year < 1950 else (year - 1950)**1.5 for year in years])
wind_power = np.linspace(0, 25, len(years))
recycling = np.array([1 if year < 1960 else (year - 1960)**0.8 for year in years])
electric_vehicles = np.array([0 if year < 1980 else (year - 1980)**1.2 for year in years])

# Create stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, organic_farming, solar_energy, wind_power, recycling, electric_vehicles,
             labels=['Organic Farming', 'Solar Energy', 'Wind Power', 'Recycling', 'Electric Vehicles'],
             colors=['forestgreen', 'gold', 'skyblue', 'darkorange', 'purple'], alpha=0.8)

# Add labels, title, and legend
ax.set_title("The Rise of Eco-Industries: \nA Century of Sustainability and Innovation", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Contribution to Sustainable Economy (Units)', fontsize=14)
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1.05, 1))
ax.grid(True, linestyle='--', alpha=0.5)

# Set ticks to every 10 years
ax.set_xticks(np.arange(1900, 2001, 10))

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()