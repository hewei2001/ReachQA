import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2040
years = np.arange(2000, 2041)

# Renewable energy data (percentages of total energy)
solar = np.clip(np.linspace(2, 35, len(years)), 0, 100)
wind = np.clip(np.linspace(5, 30, len(years)), 0, 100)
hydro = np.clip(np.linspace(15, 18, len(years)), 0, 100)
biomass = np.clip(np.linspace(3, 12, len(years)), 0, 100)
geothermal = np.clip(np.linspace(1, 10, len(years)), 0, 100)

# Calculating the residual to ensure total is 100%
residual = np.clip(100 - (solar + wind + hydro + biomass + geothermal), 0, 100)

# Stack the data
data = np.vstack([solar, wind, hydro, biomass, geothermal, residual])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal', 'Other'],
             colors=['#FFD700', '#87CEEB', '#4682B4', '#32CD32', '#FF4500', '#C0C0C0'], alpha=0.8)

# Adding labels and title
ax.set_title('Transition of Energy Sources in EcoLand\nFrom 2000 to 2040', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Energy', fontsize=12)
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, frameon=False, bbox_to_anchor=(1, 1))

# Customizing ticks and grid
ax.set_xticks(years[::4])
ax.tick_params(axis='x', rotation=45)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotating key points in the transition
ax.annotate('Major Solar Investments\nInitiated', xy=(2015, 30), xytext=(2008, 50),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='darkblue')

# Improve layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()