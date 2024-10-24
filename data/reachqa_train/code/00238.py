import matplotlib.pyplot as plt
import numpy as np

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# Artificial data for renewable energy output (in GWh)
solar_energy = np.array([12, 14, 18, 22, 30, 35, 40, 42, 45, 48, 55])
wind_energy = np.array([20, 22, 23, 25, 30, 32, 35, 36, 40, 42, 45])
hydro_energy = np.array([15, 15, 16, 18, 19, 20, 22, 25, 27, 28, 30])

# Additional data for energy storage capacity (in GWh)
storage_capacity = np.array([5, 7, 10, 13, 18, 22, 26, 30, 35, 40, 50])

# Create a subplot layout with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Line plot of renewable energy generation
axes[0].plot(years, solar_energy, label='Solar Power', color='gold', marker='o', linestyle='-', linewidth=2)
axes[0].plot(years, wind_energy, label='Wind Power', color='skyblue', marker='^', linestyle='-', linewidth=2)
axes[0].plot(years, hydro_energy, label='Hydroelectric Power', color='forestgreen', marker='s', linestyle='-', linewidth=2)

axes[0].set_title('Green Valley: Renewable Energy Generation\n(2015-2025)', fontsize=14, weight='bold', pad=15)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Energy Output (GWh)', fontsize=12)
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].legend(title='Energy Source', fontsize=10, title_fontsize=12, loc='upper left')

# Annotations for significant years
axes[0].annotate('Significant Solar Expansion', xy=(2019, 30), xytext=(2020, 35),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='gold')
axes[0].annotate('Hydro Plant Upgrade', xy=(2023, 27), xytext=(2021, 32),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='forestgreen')

# Second subplot: Bar chart of energy storage capacity
bar_width = 0.3
axes[1].bar(years - bar_width, solar_energy, width=bar_width, label='Solar Storage', color='gold', alpha=0.7)
axes[1].bar(years, wind_energy, width=bar_width, label='Wind Storage', color='skyblue', alpha=0.7)
axes[1].bar(years + bar_width, hydro_energy, width=bar_width, label='Hydro Storage', color='forestgreen', alpha=0.7)

axes[1].set_title('Energy Storage Capacity (GWh)', fontsize=14, weight='bold', pad=15)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Storage Capacity (GWh)', fontsize=12)
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].legend(title='Storage Type', fontsize=10, title_fontsize=12, loc='upper left')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()