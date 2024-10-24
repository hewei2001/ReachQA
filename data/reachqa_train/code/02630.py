import matplotlib.pyplot as plt
import numpy as np

# Time periods
decades = ['1980', '1990', '2000', '2010', '2020']

# Energy consumption data (arbitrary units) for different sources over the decades
coal = [70, 65, 55, 40, 25]
oil = [60, 58, 55, 50, 45]
natural_gas = [20, 25, 30, 35, 38]
solar = [1, 2, 4, 10, 20]
wind = [0, 1, 3, 8, 18]
hydro = [10, 12, 15, 18, 20]

# Stack the energy sources for the area chart
energy_sources = np.array([coal, oil, natural_gas, solar, wind, hydro])

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(decades, energy_sources, labels=['Coal', 'Oil', 'Natural Gas', 'Solar', 'Wind', 'Hydro'],
              colors=['#708090', '#8B4513', '#DAA520', '#FFA500', '#00BFFF', '#2E8B57'], alpha=0.8)

# Add title and labels
plt.title("The Shift of Energy Sources Over Time\nA Journey from Fossil Fuels to Renewables", fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Energy Consumption (Arbitrary Units)', fontsize=12)

# Add legend with reduced font size and positioning
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources', fontsize=10)

# Add gridlines for better readability
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45)

# Automatically adjust layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the plot
plt.show()