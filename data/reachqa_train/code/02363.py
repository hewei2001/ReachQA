import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = ["2015", "2016", "2017", "2018", "2019", "2020"]

# Define energy production data for each source in million MWh
wind_energy = np.array([120, 130, 145, 160, 175, 190])
solar_energy = np.array([80, 95, 110, 130, 155, 180])
hydro_energy = np.array([300, 310, 320, 330, 340, 355])
geothermal_energy = np.array([30, 32, 35, 38, 40, 42])

# Stacking the data
stacked_data = np.vstack([wind_energy, solar_energy, hydro_energy, geothermal_energy])

# Colors for each energy source
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the figure and axis
plt.figure(figsize=(12, 8))

# Plot each stacked bar segment
plt.bar(years, stacked_data[0], color=colors[0], label='Wind Energy')
plt.bar(years, stacked_data[1], bottom=stacked_data[0], color=colors[1], label='Solar Energy')
plt.bar(years, stacked_data[2], bottom=stacked_data[0] + stacked_data[1], color=colors[2], label='Hydro Energy')
plt.bar(years, stacked_data[3], bottom=stacked_data[0] + stacked_data[1] + stacked_data[2], color=colors[3], label='Geothermal Energy')

# Title and labels
plt.title('Global Renewable Energy Production by Source\n(2015-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (million MWh)', fontsize=12)

# Add legend and adjust its position
plt.legend(title='Energy Source', fontsize=10, loc='upper left', bbox_to_anchor=(1.05, 1))

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()