import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2031)

# Artificial data for renewable energy generation (in GWh) per year for each country
# Each array represents energy from 2020 to 2030
solaria_energy = [20, 25, 35, 45, 55, 70, 85, 100, 120, 135, 150]
windlandia_energy = [15, 30, 50, 65, 80, 95, 110, 130, 150, 170, 200]
hydrovia_energy = [50, 52, 54, 55, 60, 63, 65, 68, 70, 75, 78]
geothermalia_energy = [5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70]
biomassia_energy = [10, 15, 22, 30, 40, 50, 65, 80, 100, 125, 150]

# Combine the datasets into a single 2D array for the stackplot function
energy_sources = np.array([solaria_energy, windlandia_energy, hydrovia_energy, geothermalia_energy, biomassia_energy])

# Create a new figure and axis with a specific size
fig, ax = plt.subplots(figsize=(10, 6))

# Use the stackplot function to create the stacked area chart
ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'], 
             colors=['gold', 'skyblue', 'lightgreen', 'orange', 'brown'], alpha=0.8)

# Set chart title with line break for clarity
ax.set_title("Renewable Energy Generation in Simulated Countries\n(2020-2030)", fontsize=14, fontweight='bold')

# Label the x and y axes
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Generation (GWh)", fontsize=12)

# Add a legend and place it outside the plot to avoid overlapping data
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Source')

# Add grid lines for better readability of the plot
ax.grid(alpha=0.3)

# Adjust layout to avoid clipping of text
plt.tight_layout()

# Display the final plot
plt.show()