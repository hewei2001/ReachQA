import matplotlib.pyplot as plt
import numpy as np

# Define months
months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Energy output data for different sources (in Gigawatt-hours, GWh)
solar_energy = np.array([30, 35, 50, 70, 90, 110, 120, 115, 85, 60, 45, 35])
wind_energy = np.array([40, 45, 55, 60, 65, 70, 75, 70, 65, 60, 55, 50])
hydro_energy = np.array([50, 50, 55, 60, 65, 70, 70, 65, 60, 55, 50, 50])
geothermal_energy = np.array([20, 22, 25, 28, 30, 33, 35, 34, 31, 29, 25, 23])

# Cumulative annual energy output
cumulative_solar = np.cumsum(solar_energy)
cumulative_wind = np.cumsum(wind_energy)
cumulative_hydro = np.cumsum(hydro_energy)
cumulative_geothermal = np.cumsum(geothermal_energy)

# Set up the figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# First subplot: Stacked area chart
axs[0].stackplot(months, solar_energy, wind_energy, hydro_energy, geothermal_energy, 
                 labels=['Solar', 'Wind', 'Hydro', 'Geothermal'],
                 colors=['#FFD700', '#00BFFF', '#32CD32', '#8B4513'], alpha=0.8)
axs[0].set_title("Monthly Renewable Energy Output\n(Each Source)", fontsize=12, weight='bold', pad=10)
axs[0].set_xlabel("Months", fontsize=10)
axs[0].set_ylabel("Energy Output (GWh)", fontsize=10)
axs[0].legend(loc='upper left', fontsize=9)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)
axs[0].tick_params(axis='x', rotation=45)

# Second subplot: Bar chart of cumulative energy output
width = 0.2  # Width of the bars
x = np.arange(len(months))
axs[1].bar(x - 1.5*width, cumulative_solar, width, label='Solar', color='#FFD700', alpha=0.8)
axs[1].bar(x - 0.5*width, cumulative_wind, width, label='Wind', color='#00BFFF', alpha=0.8)
axs[1].bar(x + 0.5*width, cumulative_hydro, width, label='Hydro', color='#32CD32', alpha=0.8)
axs[1].bar(x + 1.5*width, cumulative_geothermal, width, label='Geothermal', color='#8B4513', alpha=0.8)
axs[1].set_title("Cumulative Renewable Energy Output\n(Throughout the Year)", fontsize=12, weight='bold', pad=10)
axs[1].set_xlabel("Months", fontsize=10)
axs[1].set_ylabel("Cumulative Output (GWh)", fontsize=10)
axs[1].set_xticks(x)
axs[1].set_xticklabels(months)
axs[1].legend(loc='upper left', fontsize=9)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)
axs[1].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plots
plt.show()