import matplotlib.pyplot as plt
import numpy as np

# Extend the years for the x-axis
years = ["2010", "2011", "2012", "2013", "2014", "2015", 
         "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]

# Define energy production data for each source in million MWh
wind_energy = np.array([50, 60, 70, 85, 100, 120, 130, 145, 160, 175, 190, 205, 215, 230, 245, 260])
solar_energy = np.array([10, 15, 25, 35, 50, 80, 95, 110, 130, 155, 180, 200, 215, 230, 255, 280])
hydro_energy = np.array([280, 285, 290, 295, 300, 300, 310, 320, 330, 340, 355, 360, 365, 370, 375, 380])
geothermal_energy = np.array([20, 22, 25, 28, 30, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 54])
biomass_energy = np.array([40, 42, 45, 48, 52, 55, 58, 60, 65, 70, 72, 75, 80, 85, 90, 95])

# Stacking the data
stacked_data = np.vstack([wind_energy, solar_energy, hydro_energy, geothermal_energy, biomass_energy])

# Colors for each energy source
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Plot each stacked bar segment
bottom = np.zeros(len(years))
for i, data in enumerate(stacked_data):
    ax.bar(years, data, bottom=bottom, color=colors[i], label=f'Energy Source {i+1}')
    bottom += data

# Title and labels
plt.title('Global Renewable Energy Production by Source\n(2010-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (million MWh)', fontsize=12)

# Cumulative energy production as a line plot
cumulative_energy = np.sum(stacked_data, axis=0)
ax.plot(years, cumulative_energy, color='black', marker='o', label='Total Energy Production', linewidth=2)

# Improve legend positioning
plt.legend(title='Energy Source', fontsize=10, loc='upper left', bbox_to_anchor=(1.05, 1))

# Automatically adjust layout for readability
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()