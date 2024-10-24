import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Original energy production data in GWh
solar_energy = [5, 8, 10, 15, 22, 30, 42, 58, 80, 110, 150, 200, 270, 360, 470, 600, 750, 930, 1150, 1400, 1700]
wind_energy = [30, 45, 65, 90, 120, 160, 210, 270, 340, 420, 510, 600, 690, 770, 840, 910, 980, 1040, 1100, 1160, 1230]
hydropower = [1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400]
biomass = [20, 22, 25, 28, 32, 37, 43, 50, 58, 67, 77, 88, 100, 113, 127, 142, 158, 175, 193, 212, 232]

# Calculating growth rates for each energy type
solar_growth = np.gradient(solar_energy)
wind_growth = np.gradient(wind_energy)
hydro_growth = np.gradient(hydropower)
biomass_growth = np.gradient(biomass)

# Stack the original energy data
energy_data = np.vstack([solar_energy, wind_energy, hydropower, biomass])

# Create the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 7), constrained_layout=True)

# First subplot: Stacked Area Chart
axes[0].stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower', 'Biomass'], colors=['#ffcc00', '#0099cc', '#3366cc', '#99cc33'])
axes[0].set_title('Evolution of Renewable Energy Mix (2000-2020)\nStacked Area Chart', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Energy Production (GWh)', fontsize=12, fontweight='bold')
axes[0].legend(loc='upper left', title='Energy Types', fontsize=10)
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].annotate('Rapid Solar Growth', xy=(2010, 150), xytext=(2012, 600),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7),
                 fontsize=10, color='darkred')
axes[0].annotate('Steady Wind Increase', xy=(2008, 270), xytext=(2010, 800),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7),
                 fontsize=10, color='darkblue')

# Second subplot: Line Plot of Growth Rates
axes[1].plot(years, solar_growth, label='Solar', color='#ffcc00', linewidth=2)
axes[1].plot(years, wind_growth, label='Wind', color='#0099cc', linewidth=2)
axes[1].plot(years, hydro_growth, label='Hydropower', color='#3366cc', linewidth=2)
axes[1].plot(years, biomass_growth, label='Biomass', color='#99cc33', linewidth=2)
axes[1].set_title('Growth Rate of Renewable Energy Sources\n(2000-2020)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Growth Rate (GWh/year)', fontsize=12, fontweight='bold')
axes[1].legend(loc='upper right', title='Growth Rates', fontsize=10)
axes[1].grid(True, linestyle='--', alpha=0.5)

# Display the plots
plt.show()