import matplotlib.pyplot as plt
import numpy as np

# Define the years range from 2013 to 2023
years = np.arange(2013, 2024)

# Construct contribution data for each renewable energy source in terawatt-hours (TWh)
solar_energy = np.array([5, 8, 14, 23, 35, 48, 65, 85, 105, 125, 150])
wind_energy = np.array([30, 35, 45, 55, 65, 75, 90, 105, 125, 145, 160])
hydroelectric = np.array([50, 52, 55, 57, 60, 63, 65, 68, 70, 72, 75])
geothermal = np.array([15, 16, 17, 19, 22, 24, 27, 30, 34, 38, 42])

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stackplot to illustrate cumulative contribution of each energy source
ax.stackplot(years, solar_energy, wind_energy, hydroelectric, geothermal,
             labels=['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Geothermal'],
             colors=['#FFD700', '#4682B4', '#32CD32', '#8B4513'], alpha=0.8)

# Title and labels with clear and descriptive text
ax.set_title("Decade of Renewable Energy Growth: 2013-2023\nContribution of Renewable Sources to National Grid", 
             fontsize=16, weight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Contribution (TWh)', fontsize=12)

# Add a legend to the plot, positioned outside to avoid overlap
ax.legend(loc='upper left', fontsize=10, title='Energy Sources', bbox_to_anchor=(1.05, 1))

# Annotate key trends or significant points in the plot
ax.annotate('Solar Boom', xy=(2018, 90), xytext=(2016, 110),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='red')
ax.annotate('Wind Expansion', xy=(2020, 175), xytext=(2018, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='blue')

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the final plot
plt.show()