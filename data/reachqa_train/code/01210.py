import matplotlib.pyplot as plt
import numpy as np

# Define the years for our study
years = np.arange(2010, 2021)

# Define energy production in TWh for each energy source across the years
solar_energy = np.array([5, 6, 8, 11, 15, 20, 26, 35, 47, 60, 75])
wind_energy = np.array([10, 12, 15, 20, 25, 33, 40, 52, 65, 80, 100])
hydropower_energy = np.array([30, 32, 35, 36, 37, 38, 39, 40, 41, 42, 44])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, solar_energy, label='Solar Energy', color='gold', edgecolor='black')
ax.bar(years, wind_energy, bottom=solar_energy, label='Wind Energy', color='lightblue', edgecolor='black')
ax.bar(years, hydropower_energy, bottom=solar_energy + wind_energy, label='Hydropower', color='seagreen', edgecolor='black')

# Add labels and title with line breaks to fit the layout
ax.set_title('Adoption of Renewable Energy Sources\nin Futuristan (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 250, 25))

# Add a legend to differentiate between the energy sources
ax.legend(loc='upper left', fontsize=12)

# Annotate the plot with an insight
ax.text(2010.5, 200, 'Note: Significant growth post-2015', fontsize=12, style='italic', 
        bbox={'facecolor': 'lightgray', 'alpha': 0.5, 'pad': 5})

# Adding a grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap of elements
plt.tight_layout()

# Show the plot
plt.show()