import matplotlib.pyplot as plt
import numpy as np

# Time periods
decades = ['1980', '1990', '2000', '2010', '2020']

# Energy consumption data (arbitrary units) for different sources over the decades
coal = np.array([70, 65, 55, 40, 25])
oil = np.array([60, 58, 55, 50, 45])
natural_gas = np.array([20, 25, 30, 35, 38])
solar = np.array([1, 2, 4, 10, 20])
wind = np.array([0, 1, 3, 8, 18])
hydro = np.array([10, 12, 15, 18, 20])

# Stack the energy sources for the area chart
energy_sources = np.array([coal, oil, natural_gas, solar, wind, hydro])

# Calculate the growth rate for renewable energy sources (Solar, Wind, Hydro)
renewables = np.array([solar, wind, hydro])
growth_rates = np.diff(renewables, axis=1) / renewables[:, :-1] * 100  # percentage growth rate
growth_rates = np.concatenate((np.zeros((3, 1)), growth_rates), axis=1)  # adding zero growth for the first decade

# Plotting the figures
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Stacked area chart
ax[0].stackplot(decades, energy_sources, labels=['Coal', 'Oil', 'Natural Gas', 'Solar', 'Wind', 'Hydro'],
                colors=['#708090', '#8B4513', '#DAA520', '#FFA500', '#00BFFF', '#2E8B57'], alpha=0.8)
ax[0].set_title("Energy Sources Shift Over Time\nFrom Fossil Fuels to Renewables", fontsize=14, fontweight='bold')
ax[0].set_xlabel('Decades', fontsize=12)
ax[0].set_ylabel('Energy Consumption (Arbitrary Units)', fontsize=12)
ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources', fontsize=10)
ax[0].grid(linestyle='--', linewidth=0.5, alpha=0.7)
ax[0].tick_params(axis='x', labelrotation=45)

# Line chart for growth rates of renewable energy
ax[1].plot(decades, growth_rates[0], marker='o', label='Solar', color='#FFA500')
ax[1].plot(decades, growth_rates[1], marker='o', label='Wind', color='#00BFFF')
ax[1].plot(decades, growth_rates[2], marker='o', label='Hydro', color='#2E8B57')
ax[1].set_title("Growth Rates of Renewable Energy Sources", fontsize=14, fontweight='bold')
ax[1].set_xlabel('Decades', fontsize=12)
ax[1].set_ylabel('Growth Rate (%)', fontsize=12)
ax[1].legend(loc='upper left', title='Energy Sources', fontsize=10)
ax[1].grid(linestyle='--', linewidth=0.5, alpha=0.7)
ax[1].tick_params(axis='x', labelrotation=45)

# Adjust layout for both plots
plt.tight_layout()

# Display the plots
plt.show()