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

# Stacking the areas
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, africa, asia, europe, north_america, south_america, 
             labels=['Africa', 'Asia', 'Europe', 'North America', 'South America'], 
             colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.8)

# Adding titles and labels
ax.set_title("Decade of Renewable Energy Growth:\nGlobal Adoption by Continent (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Cumulative Renewable Energy Production (GW)", fontsize=12)

# Rotate x-axis labels to avoid overlapping
plt.xticks(years, rotation=45)

# Adding legend and grid
ax.legend(loc='upper left', title='Continents', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Ensure everything fits well within the plot
plt.tight_layout()

# Display the plot
plt.show()