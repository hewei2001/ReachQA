import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Artificial data for energy production in Terawatt-hours (TWh)
solar_energy = np.array([12, 15, 20, 30, 45, 70, 100, 150, 220, 300, 390])
wind_energy = np.array([50, 60, 75, 90, 110, 150, 200, 270, 320, 400, 480])
hydro_energy = np.array([300, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355])
biomass_energy = np.array([20, 25, 30, 35, 40, 50, 60, 75, 90, 100, 115])

# Create the plot
plt.figure(figsize=(14, 8))

# Plot each renewable energy source with a unique style
plt.plot(years, solar_energy, marker='o', linestyle='-', color='gold', linewidth=2, label='Solar Energy')
plt.plot(years, wind_energy, marker='^', linestyle='--', color='skyblue', linewidth=2, label='Wind Energy')
plt.plot(years, hydro_energy, marker='s', linestyle='-.', color='royalblue', linewidth=2, label='Hydro Energy')
plt.plot(years, biomass_energy, marker='d', linestyle=':', color='forestgreen', linewidth=2, label='Biomass Energy')

# Annotate significant points on line plots
for idx, year in enumerate(years):
    if year in [2010, 2020]:
        plt.annotate(f'{solar_energy[idx]}', xy=(year, solar_energy[idx]), xytext=(year, solar_energy[idx] + 20),
                     ha='center', fontsize=9, color='gold', bbox=dict(facecolor='white', alpha=0.7, edgecolor='gold'))
        plt.annotate(f'{wind_energy[idx]}', xy=(year, wind_energy[idx]), xytext=(year, wind_energy[idx] + 20),
                     ha='center', fontsize=9, color='skyblue', bbox=dict(facecolor='white', alpha=0.7, edgecolor='skyblue'))
        plt.annotate(f'{hydro_energy[idx]}', xy=(year, hydro_energy[idx]), xytext=(year, hydro_energy[idx] + 20),
                     ha='center', fontsize=9, color='royalblue', bbox=dict(facecolor='white', alpha=0.7, edgecolor='royalblue'))
        plt.annotate(f'{biomass_energy[idx]}', xy=(year, biomass_energy[idx]), xytext=(year, biomass_energy[idx] + 20),
                     ha='center', fontsize=9, color='forestgreen', bbox=dict(facecolor='white', alpha=0.7, edgecolor='forestgreen'))

# Add titles and labels
plt.title("Renewable Energy Transition:\nAnnual Energy Output (2010-2020)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Output (TWh)", fontsize=12)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Enhance grid for readability
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()