import matplotlib.pyplot as plt
import numpy as np

# Expanded time range and granularity: Individual years from 1960 to 2020
years = np.arange(1960, 2021)

# Define utopian cities
cities = ['Harmony', 'Innovation', 'Balance']

# Define renewable energy types with nonlinear growth patterns
solar_energy = np.array([
    0.5 * np.sqrt(years - 1959),  # Harmony
    0.45 * np.sqrt(years - 1959) * 1.1,  # Innovation
    0.4 * np.sqrt(years - 1959) * 1.2   # Balance
])

wind_energy = np.array([
    0.4 * np.log(years - 1959 + 1),  # Harmony
    0.35 * np.log(years - 1959 + 1) * 1.15,  # Innovation
    0.3 * np.log(years - 1959 + 1) * 1.25   # Balance
])

hydro_energy = np.array([
    2 * np.exp((years - 1980) / 50),  # Harmony
    2.2 * np.exp((years - 1980) / 50),  # Innovation
    1.8 * np.exp((years - 1980) / 50)   # Balance
])

# Additional energy type
geothermal_energy = np.array([
    0.1 * (years - 1960),  # Harmony
    0.12 * (years - 1960),  # Innovation
    0.11 * (years - 1960)   # Balance
])

# Plotting setup
fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)
city_colors = ['#FFD700', '#4682B4', '#32CD32', '#FFA07A']
energy_types = ['Solar', 'Wind', 'Hydro', 'Geothermal']

# Plotting data for each city
for i, ax in enumerate(axes):
    ax.stackplot(years, solar_energy[i], wind_energy[i], hydro_energy[i], geothermal_energy[i],
                 labels=energy_types, colors=city_colors, alpha=0.7)

    # Add growth trend lines for each energy type
    ax.plot(years, solar_energy[i], color='#FFD700', linewidth=1.5, linestyle='--')
    ax.plot(years, wind_energy[i], color='#4682B4', linewidth=1.5, linestyle='--')
    ax.plot(years, hydro_energy[i], color='#32CD32', linewidth=1.5, linestyle='--')
    ax.plot(years, geothermal_energy[i], color='#FFA07A', linewidth=1.5, linestyle='--')

    # Title, labels, and legends for each subplot
    ax.set_title(f"Renewable Energy Adoption in {cities[i]}\n(1960-2020)", fontsize=14, fontweight='bold')
    ax.set_xlabel('Years', fontsize=12)
    if i == 0:
        ax.set_ylabel('Energy Usage (Arbitrary Units)', fontsize=12)
    ax.legend(loc='upper left', title="Energy Types", fontsize=8)
    
    # Customize ticks and grid
    ax.set_xticks(years[::10])  # Show ticks every 10 years
    ax.grid(linestyle='--', linewidth=0.5, alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()