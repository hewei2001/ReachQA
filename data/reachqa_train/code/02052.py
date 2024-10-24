import matplotlib.pyplot as plt
import numpy as np

# Define the years for monthly data from 2010 to 2023
years = np.arange(2010, 2024, 1/12)  # Represents monthly intervals

# Define the energy contributions (monthly data extrapolated)
solar_energy = np.array([2, 3, 5, 7, 10, 15, 20, 28, 36, 45, 55, 66, 78, 91])
solar_energy = np.interp(np.arange(0, 168), np.arange(0, 168, 12), solar_energy)

wind_energy = np.array([4, 6, 8, 10, 13, 16, 21, 25, 29, 35, 42, 50, 60, 72])
wind_energy = np.interp(np.arange(0, 168), np.arange(0, 168, 12), wind_energy)

hydro_energy = np.array([5, 5, 6, 7, 9, 11, 14, 18, 22, 25, 28, 30, 31, 32])
hydro_energy = np.interp(np.arange(0, 168), np.arange(0, 168, 12), hydro_energy)

bioenergy = np.array([1, 2, 3, 3, 4, 5, 6, 8, 10, 12, 14, 17, 20, 24])
bioenergy = np.interp(np.arange(0, 168), np.arange(0, 168, 12), bioenergy)

# New energy source: Geothermal energy
geothermal_energy = np.linspace(1, 10, num=168)

# Stack the energy sources including the new one
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bioenergy, geothermal_energy])

# Create the stacked area chart
plt.figure(figsize=(14, 10))
plt.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydroelectric', 'Bioenergy', 'Geothermal'],
              colors=['#FFD700', '#1E90FF', '#32CD32', '#A0522D', '#FF4500'], alpha=0.8)

# Add titles and labels
plt.title("The Evolution of Renewable Energy Sources in GreenCity\nfrom 2010 to 2023 (Monthly Data)", fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Contribution (GW)", fontsize=12)

# Adding a legend to identify the energy sources
plt.legend(loc='upper left', title="Energy Source", fontsize=10, bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Customize grid and layout
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(np.arange(2010, 2024, 1), rotation=45, fontsize=10)
plt.yticks(np.arange(0, 230, 20), fontsize=10)

# Highlight milestones with annotations
plt.annotate('First Wind Energy Peak', xy=(2017, 100), xytext=(2015, 150),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='blue')

plt.annotate('Geothermal Introduced', xy=(2010, 5), xytext=(2012, 50),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='red')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()