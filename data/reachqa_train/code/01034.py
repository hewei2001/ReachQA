import matplotlib.pyplot as plt
import numpy as np

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# Energy data in megawatts (MW)
solar_energy = np.array([20, 25, 35, 50, 70, 90, 120, 160, 210, 270, 340])
wind_energy = np.array([15, 20, 30, 45, 60, 80, 105, 140, 180, 230, 290])
hydro_energy = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Calculate percentage growth year-over-year
solar_growth = np.append([0], np.diff(solar_energy) / solar_energy[:-1] * 100)
wind_growth = np.append([0], np.diff(wind_energy) / wind_energy[:-1] * 100)
hydro_growth = np.append([0], np.diff(hydro_energy) / hydro_energy[:-1] * 100)

# Plotting the area chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked area plot
ax1.stackplot(years, solar_energy, wind_energy, hydro_energy,
              labels=['Solar Energy', 'Wind Energy', 'Hydro Energy'],
              colors=['#FFD700', '#1E90FF', '#32CD32'],
              alpha=0.7)
ax1.set_title("Renewable Energy Adoption in GreenCity\nTransition from 2015 to 2025", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Energy Contribution (MW)", fontsize=14)
ax1.legend(loc='upper left', title='Energy Sources', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Secondary y-axis for growth rate
ax2 = ax1.twinx()
ax2.plot(years, solar_growth, label='Solar Growth %', color='#FFD700', linestyle='--', marker='o')
ax2.plot(years, wind_growth, label='Wind Growth %', color='#1E90FF', linestyle='--', marker='s')
ax2.plot(years, hydro_growth, label='Hydro Growth %', color='#32CD32', linestyle='--', marker='^')
ax2.set_ylabel("Growth Rate (%)", fontsize=14)
ax2.legend(loc='upper right', title='Growth Rates', fontsize=12)

# Annotate trends
ax1.annotate('Solar energy peak', xy=(2024, 700), xytext=(2021, 780),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Wind energy surge', xy=(2023, 580), xytext=(2019, 650),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Customize x-axis labels
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Adjust layout to prevent text cutoff
fig.tight_layout()

# Show the plot
plt.show()