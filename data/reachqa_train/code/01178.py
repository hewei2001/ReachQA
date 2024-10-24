import matplotlib.pyplot as plt
import numpy as np

# Data representing energy consumption (in GWh) over five years
years = [2019, 2020, 2021, 2022, 2023]
fossil_fuels = [500, 480, 450, 420, 390]
nuclear_energy = [300, 300, 290, 280, 280]
solar_energy = [50, 80, 120, 160, 210]
wind_energy = [30, 50, 70, 100, 130]
hydropower = [90, 85, 95, 88, 92]

# Stack data for the area chart
data = np.array([fossil_fuels, nuclear_energy, solar_energy, wind_energy, hydropower])
data_stack = np.cumsum(data, axis=0)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the areas
ax.fill_between(years, 0, data_stack[0], label='Fossil Fuels', color='lightcoral', alpha=0.8)
ax.fill_between(years, data_stack[0], data_stack[1], label='Nuclear Energy', color='gold', alpha=0.7)
ax.fill_between(years, data_stack[1], data_stack[2], label='Solar Energy', color='lightgreen', alpha=0.9)
ax.fill_between(years, data_stack[2], data_stack[3], label='Wind Energy', color='skyblue', alpha=0.6)
ax.fill_between(years, data_stack[3], data_stack[4], label='Hydropower', color='orchid', alpha=0.7)

# Add title and labels
ax.set_title("Energiville Energy Mix:\nA 5-Year Overview", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Consumption (GWh)", fontsize=12)

# Rotate x-axis labels to avoid overlapping
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add gridlines for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend with clear identification
ax.legend(loc='upper left', fontsize=10, title='Energy Sources', title_fontsize='12')

# Adjust layout to prevent overlap and improve visual appeal
plt.tight_layout()

# Display the chart
plt.show()