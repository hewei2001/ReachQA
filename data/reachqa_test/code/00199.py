import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2020, 2031)

# Energy production data in TWh
wind_energy = [600, 620, 645, 680, 720, 770, 830, 890, 950, 1020, 1100]
solar_energy = [350, 380, 410, 450, 500, 560, 640, 730, 820, 930, 1050]
hydro_energy = [900, 920, 940, 960, 980, 1000, 1015, 1030, 1050, 1070, 1090]
bioenergy = [200, 210, 225, 240, 260, 290, 320, 360, 400, 450, 510]

# Stack the energy data for an area chart
energy_data = np.vstack([wind_energy, solar_energy, hydro_energy, bioenergy])

# Related but distinct data: Renewable energy capacity in GW
wind_capacity = [50, 52, 54, 58, 62, 67, 72, 78, 85, 92, 100]
solar_capacity = [30, 32, 35, 40, 45, 52, 60, 70, 80, 92, 105]

# Colors for each energy sector
colors = ['#a8dadc', '#f4a261', '#457b9d', '#2a9d8f']
capacity_colors = ['#1d3557', '#e76f51']

# Create the plots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Area chart for energy production
axs[0].stackplot(years, energy_data, labels=['Wind', 'Solar', 'Hydro', 'Bioenergy'], colors=colors, alpha=0.8)
axs[0].set_title('Renewable Energy Production by Sector\n(2020-2030)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Energy Production (TWh)', fontsize=12)
axs[0].legend(loc='upper left', fontsize=10, frameon=False)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)
axs[0].tick_params(axis='x', rotation=45)

# Second subplot: Line chart for capacity
axs[1].plot(years, wind_capacity, marker='o', color=capacity_colors[0], label='Wind Capacity')
axs[1].plot(years, solar_capacity, marker='x', color=capacity_colors[1], label='Solar Capacity')
axs[1].set_title('Renewable Energy Capacity Growth\n(2020-2030)', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Installed Capacity (GW)', fontsize=12)
axs[1].legend(loc='upper left', fontsize=10, frameon=False)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)
axs[1].tick_params(axis='x', rotation=45)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()