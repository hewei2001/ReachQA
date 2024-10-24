import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2030, 2041)

# Energy consumption in PetaJoules for each energy source
# Adjusted for smoother transitions and clearer visual representation
solar_energy = np.array([40, 60, 80, 105, 135, 170, 210, 255, 305, 360, 420])
wind_energy = np.array([50, 70, 95, 125, 160, 200, 245, 295, 350, 410, 475])
nuclear_energy = np.array([90, 92, 95, 98, 101, 104, 108, 112, 115, 118, 120])
fossil_fuels = np.array([600, 570, 540, 510, 480, 450, 420, 390, 360, 330, 300])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
colors = ['gold', 'skyblue', 'forestgreen', 'lightcoral']
ax.stackplot(years, solar_energy, wind_energy, nuclear_energy, fossil_fuels,
             labels=['Solar Energy', 'Wind Energy', 'Nuclear Energy', 'Fossil Fuels'],
             colors=colors, alpha=0.8)

# Set the title and labels
ax.set_title('Projected Energy Consumption by Source (2030-2040)\nTransitioning Towards Renewable Energy', 
             fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (PetaJoules)', fontsize=14)

# Add a legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10, frameon=True)

# Add grid lines for readability
ax.grid(True, which='major', linestyle='--', alpha=0.6)

# Adjust x-axis ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Highlight the transition point in 2040 where renewables surpass fossil fuels
ax.annotate('Renewables Surpass Fossil Fuels',
            xy=(2040, solar_energy[-1] + wind_energy[-1] + nuclear_energy[-1]), 
            xytext=(2035, 750),
            textcoords="offset points", ha='center', fontsize=12, color='black',
            arrowprops=dict(arrowstyle='->', color='gray'))

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()