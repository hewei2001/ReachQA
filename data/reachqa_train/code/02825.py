import matplotlib.pyplot as plt
import numpy as np

# Original data for stacked area plot
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
solar = [2, 3, 5, 10, 20, 30, 40]
wind = [1, 2, 10, 15, 25, 30, 25]
geothermal = [3, 4, 6, 7, 10, 8, 5]
hydropower = [25, 30, 35, 28, 22, 18, 15]
biomass = [9, 8, 6, 5, 3, 2, 2]

# Hypothetical data for line plot (Total energy output in TWh)
total_renewable_energy_output = [5, 10, 20, 40, 60, 80, 87]

# Create a figure and two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Stacked area plot on the first subplot
data = np.vstack([solar, wind, geothermal, hydropower, biomass])
ax1.stackplot(decades, data, labels=['Solar', 'Wind', 'Geothermal', 'Hydropower', 'Biomass'],
              colors=['#FFD700', '#1E90FF', '#32CD32', '#4682B4', '#8B4513'], alpha=0.85)
ax1.set_title('Renewable Energy Sources in Urban Development\n(1960s to 2020s)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Energy Share (%)', fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10)
ax1.set_ylim(0, 100)
ax1.grid(True, linestyle='--', alpha=0.7)

# Line plot on the second subplot
ax2.plot(decades, total_renewable_energy_output, marker='o', color='b', label='Total Renewable Output (TWh)', linestyle='-', linewidth=2)
ax2.set_title('Total Renewable Energy Output\n(1960s to 2020s)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Decade', fontsize=12)
ax2.set_ylabel('Energy Output (TWh)', fontsize=12)
ax2.set_ylim(0, 100)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(loc='upper left', fontsize=10)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()