import matplotlib.pyplot as plt
import numpy as np

# Decades for x-axis
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Percentage of energy contribution by renewable sources over time (fictional data)
solar_energy = np.array([2, 5, 10, 15, 22])
wind_energy = np.array([3, 10, 18, 25, 30])
hydroelectric_energy = np.array([10, 12, 15, 18, 20])
biomass_energy = np.array([5, 8, 12, 15, 18])
geothermal_energy = np.array([1, 2, 2, 3, 5])

# Stack the energy data
energy_data = np.vstack([solar_energy, wind_energy, hydroelectric_energy, biomass_energy, geothermal_energy])

# Define colors for each energy source
colors = ['#ffd700', '#1e90ff', '#32cd32', '#8b4513', '#ff6347']

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(decades, energy_data, labels=[
    'Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal'], colors=colors, alpha=0.85)

# Customize the chart
ax.set_title('Evolution of Renewable Energy Sources\nin Europe (1980-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage of Total Energy Output', fontsize=12)
ax.set_xlim(decades[0], decades[-1])
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 10))

# Add a legend outside the main plot area
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Energy Sources', fontsize=10, title_fontsize='12', frameon=False)

# Annotate significant changes
ax.annotate('Rise of Wind Energy', xy=(2010, 40), xytext=(2005, 60),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='darkblue')

# Enhance layout for readability and avoid occlusion
plt.xticks(decades)
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to fit legend

# Show the plot
plt.show()