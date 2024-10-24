import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = [1990, 2000, 2010, 2020]

# Energy production data (in terawatt-hours, TWh)
coal = np.array([1200, 1100, 950, 800])
natural_gas = np.array([300, 500, 600, 750])
nuclear = np.array([450, 500, 550, 600])
hydroelectric = np.array([150, 200, 250, 300])
renewables = np.array([20, 60, 200, 550])

# Cumulative data for each energy source
cumulative_energy = coal + natural_gas + nuclear + hydroelectric + renewables

# Calculate percentage share of each energy source
total_energy = coal + natural_gas + nuclear + hydroelectric + renewables
coal_share = (coal / total_energy) * 100
natural_gas_share = (natural_gas / total_energy) * 100
nuclear_share = (nuclear / total_energy) * 100
hydroelectric_share = (hydroelectric / total_energy) * 100
renewables_share = (renewables / total_energy) * 100

# Creating the plot with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# Stacked area chart for energy production
axes[0].stackplot(years, coal, natural_gas, nuclear, hydroelectric, renewables,
                  labels=['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Renewables'],
                  colors=['#8B0000', '#FFA500', '#4682B4', '#32CD32', '#FFD700'], alpha=0.8)
axes[0].set_title('Energy Transition Over Time\nElectricity Production Sources (1990-2020)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Electricity Production (TWh)', fontsize=12)
axes[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
axes[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Line plot for percentage share of each energy source
axes[1].plot(years, coal_share, label='Coal', color='#8B0000', marker='o')
axes[1].plot(years, natural_gas_share, label='Natural Gas', color='#FFA500', marker='o')
axes[1].plot(years, nuclear_share, label='Nuclear', color='#4682B4', marker='o')
axes[1].plot(years, hydroelectric_share, label='Hydroelectric', color='#32CD32', marker='o')
axes[1].plot(years, renewables_share, label='Renewables', color='#FFD700', marker='o')
axes[1].set_title('Percentage Share of Electricity Production (1990-2020)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Percentage Share (%)', fontsize=12)
axes[1].legend(loc='upper left', bbox_to_anchor=(1, 1))
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.xticks(years, rotation=45)

# Display the plots
plt.show()