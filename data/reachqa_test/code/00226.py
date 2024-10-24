import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2020
years = list(range(2000, 2021))

# Fictional data for energy output (in TWh) for each renewable source
solar = [5, 8, 11, 14, 17, 21, 26, 31, 37, 44, 51, 59, 68, 78, 89, 101, 114, 128, 143, 159, 176]
wind = [15, 18, 22, 27, 32, 38, 45, 53, 62, 72, 83, 95, 108, 122, 137, 153, 170, 188, 207, 227, 248]
hydroelectric = [40, 42, 44, 47, 51, 55, 60, 66, 73, 81, 90, 100, 111, 123, 136, 150, 165, 181, 198, 216, 235]
geothermal = [3, 4, 5, 6, 7, 9, 10, 12, 14, 17, 20, 23, 27, 31, 36, 41, 47, 53, 60, 67, 75]
biomass = [10, 12, 14, 16, 18, 21, 24, 27, 31, 35, 40, 45, 51, 58, 65, 73, 82, 92, 103, 115, 128]
tidal = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 20, 23, 26, 29]

# Calculate cumulative and percentage data
total_energy = np.array(solar) + np.array(wind) + np.array(hydroelectric) + np.array(geothermal) + np.array(biomass) + np.array(tidal)
solar_pct = np.array(solar) / total_energy * 100
wind_pct = np.array(wind) / total_energy * 100
hydroelectric_pct = np.array(hydroelectric) / total_energy * 100
geothermal_pct = np.array(geothermal) / total_energy * 100
biomass_pct = np.array(biomass) / total_energy * 100
tidal_pct = np.array(tidal) / total_energy * 100

# Plot configuration
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# Stacked bar plot for energy outputs
ax1.bar(years, solar, label='Solar', color='#FFD700', edgecolor='white')
ax1.bar(years, wind, bottom=solar, label='Wind', color='#87CEEB', edgecolor='white')
ax1.bar(years, hydroelectric, bottom=np.array(solar) + np.array(wind), label='Hydroelectric', color='#4682B4', edgecolor='white')
ax1.bar(years, geothermal, bottom=np.array(solar) + np.array(wind) + np.array(hydroelectric), label='Geothermal', color='#FF8C00', edgecolor='white')
ax1.bar(years, biomass, bottom=np.array(solar) + np.array(wind) + np.array(hydroelectric) + np.array(geothermal), label='Biomass', color='#8FBC8F', edgecolor='white')
ax1.bar(years, tidal, bottom=np.array(solar) + np.array(wind) + np.array(hydroelectric) + np.array(geothermal) + np.array(biomass), label='Tidal', color='#708090', edgecolor='white')
ax1.set_title("Renewable Energy Revolution in Solaris (2000-2020)", fontsize=16, pad=20)
ax1.set_ylabel("Energy Output (TWh)", fontsize=12)
ax1.legend(loc='upper left', title="Energy Sources", fontsize=10, bbox_to_anchor=(1, 1))
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Line plot for percentage contribution
ax2.plot(years, solar_pct, label='Solar', marker='o', color='#FFD700')
ax2.plot(years, wind_pct, label='Wind', marker='s', color='#87CEEB')
ax2.plot(years, hydroelectric_pct, label='Hydroelectric', marker='^', color='#4682B4')
ax2.plot(years, geothermal_pct, label='Geothermal', marker='d', color='#FF8C00')
ax2.plot(years, biomass_pct, label='Biomass', marker='x', color='#8FBC8F')
ax2.plot(years, tidal_pct, label='Tidal', marker='*', color='#708090')
ax2.set_title("Percentage Contribution of Each Renewable Source", fontsize=14, pad=10)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Percentage of Total Energy (%)", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Rotate x-axis labels and adjust layout
plt.xticks(years, rotation=45, ha='right')
plt.tight_layout()

# Display the chart
plt.show()