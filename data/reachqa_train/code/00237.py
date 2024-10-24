import matplotlib.pyplot as plt
import numpy as np

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# Artificial data for renewable energy output (in GWh)
solar_energy = np.array([12, 14, 18, 22, 30, 35, 40, 42, 45, 48, 55])
wind_energy = np.array([20, 22, 23, 25, 30, 32, 35, 36, 40, 42, 45])
hydro_energy = np.array([15, 15, 16, 18, 19, 20, 22, 25, 27, 28, 30])

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each energy source
plt.plot(years, solar_energy, label='Solar Power', color='gold', marker='o', linestyle='-', linewidth=2)
plt.plot(years, wind_energy, label='Wind Power', color='skyblue', marker='^', linestyle='-', linewidth=2)
plt.plot(years, hydro_energy, label='Hydroelectric Power', color='forestgreen', marker='s', linestyle='-', linewidth=2)

# Adding labels and title
plt.title('Green Valley: Renewable Energy Generation\n(2015-2025)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Output (GWh)', fontsize=12)

# Add a grid for better readability
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a legend
plt.legend(title='Energy Source', fontsize=10, title_fontsize=12, loc='upper left')

# Adding annotations for significant years
plt.annotate('Significant Solar Expansion', xy=(2019, 30), xytext=(2020, 35),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='gold')

plt.annotate('Hydro Plant Upgrade', xy=(2023, 27), xytext=(2021, 32),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='forestgreen')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()