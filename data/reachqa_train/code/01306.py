import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Define adoption rates for different energy sources as percentages
solar_adoption = np.array([2, 3, 5, 7, 10, 14, 18, 25, 30, 35, 40])
wind_adoption = np.array([10, 11, 13, 15, 17, 19, 21, 24, 26, 28, 30])
hydro_adoption = np.array([30, 31, 31, 32, 33, 33, 34, 35, 35, 36, 36])

# Define additional data for cumulative adoption
total_adoption = solar_adoption + wind_adoption + hydro_adoption

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 6), gridspec_kw={'width_ratios': [2, 1]})
fig.suptitle('Renewable Energy Adoption and Impact in EcoLand (2010-2020)', fontsize=16, fontweight='bold', y=1.02)

# First subplot: Line Chart
axs[0].plot(years, solar_adoption, label='Solar Energy', color='gold', linestyle='--', marker='o', linewidth=2)
axs[0].plot(years, wind_adoption, label='Wind Energy', color='skyblue', linestyle='-', marker='s', linewidth=2)
axs[0].plot(years, hydro_adoption, label='Hydropower', color='lightgreen', linestyle='-.', marker='^', linewidth=2)

axs[0].set_title('Evolution of Renewable Energy Adoption', fontsize=13, fontweight='bold', pad=10)
axs[0].set_xlabel('Year', fontsize=11)
axs[0].set_ylabel('Adoption Rate (% of Total Energy Consumption)', fontsize=11)
axs[0].legend(title="Energy Source", loc='upper left', fontsize=9)
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5)

axs[0].annotate('Solar Boost Innovations', xy=(2015, 14), xytext=(2013, 28),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')
axs[0].annotate('Steady Wind Policy Support', xy=(2017, 24), xytext=(2015, 10),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')

# Second subplot: Stacked Area Chart for cumulative adoption
axs[1].stackplot(years, solar_adoption, wind_adoption, hydro_adoption, labels=['Solar', 'Wind', 'Hydro'],
                 colors=['gold', 'skyblue', 'lightgreen'], alpha=0.8)

axs[1].set_title('Cumulative Renewable Energy Adoption', fontsize=13, fontweight='bold', pad=10)
axs[1].set_xlabel('Year', fontsize=11)
axs[1].set_ylabel('Cumulative Adoption Rate (%)', fontsize=11)
axs[1].legend(loc='upper left', fontsize=9)
axs[1].grid(True, linestyle='--', linewidth=0.5)

# Adjust layout for readability
fig.tight_layout()

# Show the plot
plt.show()