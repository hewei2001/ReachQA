import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Energy production data in GWh
solar_energy = [5, 8, 10, 15, 22, 30, 42, 58, 80, 110, 150, 200, 270, 360, 470, 600, 750, 930, 1150, 1400, 1700]
wind_energy = [30, 45, 65, 90, 120, 160, 210, 270, 340, 420, 510, 600, 690, 770, 840, 910, 980, 1040, 1100, 1160, 1230]
hydropower = [1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400]
biomass = [20, 22, 25, 28, 32, 37, 43, 50, 58, 67, 77, 88, 100, 113, 127, 142, 158, 175, 193, 212, 232]

# Stack the data
energy_data = np.vstack([solar_energy, wind_energy, hydropower, biomass])

# Plot the stacked area chart
plt.figure(figsize=(14, 7))
plt.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower', 'Biomass'], colors=['#ffcc00', '#0099cc', '#3366cc', '#99cc33'])

# Enhance plot with labels and legend
plt.title('Evolution of Renewable Energy Mix\n(2000-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Energy Production (Gigawatt-hours)', fontsize=12, fontweight='bold')
plt.xticks(years, rotation=45)
plt.legend(loc='upper left', fontsize=10, title='Energy Types')
plt.grid(True, linestyle='--', alpha=0.5)

# Annotate significant points or changes
plt.annotate('Rapid Solar Growth', xy=(2010, 150), xytext=(2012, 500),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7),
             fontsize=10, color='darkred')
plt.annotate('Steady Wind Increase', xy=(2008, 270), xytext=(2010, 600),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7),
             fontsize=10, color='darkblue')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()