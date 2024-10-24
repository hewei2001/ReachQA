import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Cumulative renewable energy production (in gigawatts) by continent
africa = np.array([10, 15, 22, 30, 40, 55, 70, 85, 100, 120, 145])
asia = np.array([20, 35, 50, 70, 95, 125, 160, 195, 230, 270, 315])
europe = np.array([15, 25, 40, 60, 80, 105, 130, 160, 190, 225, 260])
north_america = np.array([25, 40, 60, 85, 115, 145, 180, 215, 255, 300, 350])
south_america = np.array([5, 10, 15, 25, 35, 50, 70, 95, 120, 150, 185])

# Calculate the year-on-year increase
africa_growth = np.diff(africa, prepend=africa[0])
asia_growth = np.diff(asia, prepend=asia[0])
europe_growth = np.diff(europe, prepend=europe[0])
north_america_growth = np.diff(north_america, prepend=north_america[0])
south_america_growth = np.diff(south_america, prepend=south_america[0])

# Plot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Subplot 1: Stack plot for cumulative production
ax1.stackplot(years, africa, asia, europe, north_america, south_america, 
              labels=['Africa', 'Asia', 'Europe', 'North America', 'South America'], 
              colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.8)
ax1.set_title("Decade of Renewable Energy Growth:\nGlobal Adoption by Continent (2010-2020)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Cumulative Renewable Energy Production (GW)", fontsize=12)
ax1.legend(loc='upper left', title='Continents', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)

# Subplot 2: Line plot for year-on-year growth
ax2.plot(years, africa_growth, marker='o', label='Africa', color='#ff9999')
ax2.plot(years, asia_growth, marker='o', label='Asia', color='#66b3ff')
ax2.plot(years, europe_growth, marker='o', label='Europe', color='#99ff99')
ax2.plot(years, north_america_growth, marker='o', label='North America', color='#ffcc99')
ax2.plot(years, south_america_growth, marker='o', label='South America', color='#c2c2f0')

ax2.set_title("Year-on-Year Renewable Energy Production Increase", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Annual Increase in Production (GW)", fontsize=12)
ax2.legend(loc='upper left', title='Continents', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_xticks(years)
ax2.tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()