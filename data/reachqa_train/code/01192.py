import matplotlib.pyplot as plt
import numpy as np

# Decades for x-axis
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Renewable energy contributions (fictional data)
solar_energy = np.array([2, 5, 10, 15, 22])
wind_energy = np.array([3, 10, 18, 25, 30])
hydroelectric_energy = np.array([10, 12, 15, 18, 20])
biomass_energy = np.array([5, 8, 12, 15, 18])
geothermal_energy = np.array([1, 2, 2, 3, 5])

# Cumulative renewable energy and its growth rate over the decades
total_renewable_energy = solar_energy + wind_energy + hydroelectric_energy + biomass_energy + geothermal_energy
growth_rate = np.array([0, 25, 60, 40, 45])  # Hypothetical growth rate data

# Create a 1x2 subplot layout
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Colors for the stacked area plot
colors = ['#ffd700', '#1e90ff', '#32cd32', '#8b4513', '#ff6347']

# First subplot: Stacked area plot
axes[0].stackplot(decades, solar_energy, wind_energy, hydroelectric_energy, biomass_energy, geothermal_energy,
                  labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal'], colors=colors, alpha=0.85)
axes[0].set_title('Evolution of Renewable Energy Sources\nin Europe (1980-2020)', fontsize=14, fontweight='bold', pad=15)
axes[0].set_xlabel('Decade', fontsize=12)
axes[0].set_ylabel('Percentage of Total Energy Output', fontsize=12)
axes[0].set_xlim(decades[0], decades[-1])
axes[0].set_ylim(0, 100)
axes[0].set_yticks(range(0, 101, 10))
axes[0].legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Energy Sources', fontsize=10, title_fontsize='12', frameon=False)
axes[0].annotate('Rise of Wind Energy', xy=(2010, 40), xytext=(2005, 60),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='darkblue')

# Second subplot: Line plot for cumulative and growth rate
axes[1].plot(decades, total_renewable_energy, label='Total Renewable Energy', color='darkgreen', marker='o', linewidth=2)
axes[1].plot(decades, growth_rate, label='Growth Rate (%)', color='darkorange', linestyle='--', marker='s', linewidth=2)
axes[1].set_title('Renewable Energy Growth Rate Analysis', fontsize=14, fontweight='bold', pad=15)
axes[1].set_xlabel('Decade', fontsize=12)
axes[1].set_ylabel('Energy Contribution & Growth Rate', fontsize=12)
axes[1].set_xlim(decades[0], decades[-1])
axes[1].set_ylim(0, 150)
axes[1].legend(loc='upper left', fontsize=10, title_fontsize='12', frameon=False)
axes[1].grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout(pad=4)

# Show the plot
plt.show()