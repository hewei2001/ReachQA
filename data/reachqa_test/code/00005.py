import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy production data
years = np.arange(2010, 2021)
solar_energy = [5, 10, 15, 30, 50, 80, 120, 180, 250, 320, 400]
wind_energy = [20, 35, 50, 65, 80, 100, 120, 150, 180, 210, 250]
hydro_energy = [70, 75, 78, 80, 82, 84, 86, 88, 89, 90, 92]
geothermal_energy = [10, 12, 15, 18, 22, 26, 30, 36, 42, 48, 55]

# Calculate cumulative energy production
cumulative_solar = np.cumsum(solar_energy)
cumulative_wind = np.cumsum(wind_energy)
cumulative_hydro = np.cumsum(hydro_energy)
cumulative_geothermal = np.cumsum(geothermal_energy)

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot the line chart on the first subplot
axs[0].plot(years, solar_energy, label='Solar', color='gold', linestyle='-', marker='o', linewidth=2)
axs[0].plot(years, wind_energy, label='Wind', color='cornflowerblue', linestyle='--', marker='^', linewidth=2)
axs[0].plot(years, hydro_energy, label='Hydroelectric', color='seagreen', linestyle='-.', marker='s', linewidth=2)
axs[0].plot(years, geothermal_energy, label='Geothermal', color='indianred', linestyle=':', marker='d', linewidth=2)
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Energy Production (TWh)')
axs[0].set_title('Renewable Energy Production Growth\nfrom 2010 to 2020')
axs[0].legend(title='Energy Source', loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].set_xticks(years)
axs[0].tick_params(axis='x', rotation=45)

# Plot the stacked bar chart on the second subplot
axs[1].bar(years, cumulative_solar, label='Solar', color='gold')
axs[1].bar(years, cumulative_wind, bottom=cumulative_solar, label='Wind', color='cornflowerblue')
axs[1].bar(years, cumulative_hydro, bottom=cumulative_solar + cumulative_wind, label='Hydroelectric', color='seagreen')
axs[1].bar(years, cumulative_geothermal, bottom=cumulative_solar + cumulative_wind + cumulative_hydro, label='Geothermal', color='indianred')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Cumulative Energy Production (TWh)')
axs[1].set_title('Cumulative Renewable Energy Production\nfrom 2010 to 2020')
axs[1].legend(title='Energy Source', loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
axs[1].set_xticks(years)
axs[1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()