import matplotlib.pyplot as plt
import numpy as np

# Define the years (2010-2021)
years = np.arange(2010, 2022)  # Adjust to match the length of energy lists

# Define the energy produced (in terawatt-hours)
solar_power = [30, 50, 70, 110, 170, 250, 350, 470, 600, 750, 900, 1050]  # Length 12
wind_power = [80, 100, 150, 200, 300, 400, 500, 620, 780, 910, 1100, 1300]  # Length 12
hydro_power = [90, 85, 80, 70, 65, 60, 58, 57, 55, 54, 50, 48]  # Length 12
biomass_power = [20, 25, 30, 35, 40, 45, 55, 60, 70, 80, 90, 100]  # Length 12
geothermal_power = [10, 12, 14, 15, 18, 20, 22, 24, 26, 28, 30, 32]  # Length 12

# Ensure data is appropriate
hydro_power = np.clip(hydro_power, 50, None)

# Set bar width
bar_width = 0.35

# Create bar positions
index = np.arange(len(years))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Create stacked bar chart
bars1 = ax.bar(index, solar_power, bar_width, label='Solar Power', color='#ffcc00')
bars2 = ax.bar(index, wind_power, bar_width, bottom=solar_power, label='Wind Power', color='#3399ff')
bars3 = ax.bar(index, hydro_power, bar_width, bottom=np.array(solar_power) + np.array(wind_power), label='Hydroelectric Power', color='#33cc33')
bars4 = ax.bar(index, biomass_power, bar_width, bottom=np.array(solar_power) + np.array(wind_power) + np.array(hydro_power), label='Biomass Power', color='#9966cc')
bars5 = ax.bar(index, geothermal_power, bar_width, bottom=np.array(solar_power) + np.array(wind_power) + np.array(hydro_power) + np.array(biomass_power), label='Geothermal Power', color='#ff6699')

# Adding data annotations for total energy production
for i in range(len(years)):
    total_energy = solar_power[i] + wind_power[i] + hydro_power[i] + biomass_power[i] + geothermal_power[i]
    ax.annotate(f'Total: {total_energy}', 
                xy=(i, total_energy + 20), 
                ha='center', 
                fontsize=9, 
                fontweight='bold')

# Customize the plot
ax.set_title('The Rise of Renewable Energy Sources:\nA Decade of Progress (2010-2021)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Produced (TWh)', fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(years, fontsize=10, rotation=45)
ax.legend(title='Energy Sources', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to ensure nothing is clipped
plt.tight_layout()

# Display the plot
plt.show()