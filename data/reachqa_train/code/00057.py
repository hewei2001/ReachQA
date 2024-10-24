import numpy as np
import matplotlib.pyplot as plt

# Define the years and energy production data for each source
years = np.arange(2010, 2020)

# Data (in TWh - terawatt hours) for each renewable energy source
# Adjusted data to create a more dynamic transition over the years
solar_energy = np.array([15, 25, 35, 50, 70, 95, 125, 160, 200, 245])
wind_energy = np.array([40, 55, 80, 105, 140, 180, 230, 290, 360, 440])
hydropower = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145])
biomass_energy = np.array([10, 15, 25, 35, 50, 70, 95, 125, 160, 200])

# Stacking the data
energy_data = np.vstack([solar_energy, wind_energy, hydropower, biomass_energy])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower', 'Biomass'],
             colors=['#FDB813', '#0F7ABD', '#A4C639', '#8B4513'], alpha=0.8)

# Customize the plot
ax.set_title('Renewable Energy Production Trends Over a Decade\n(2010-2019)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Add legend and grid
ax.legend(loc='upper left', fontsize=10, title='Energy Source', frameon=False)
ax.grid(linestyle='--', alpha=0.6)

# Enhance readability of x-axis labels
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1001, 100))

# Annotate significant points or changes
ax.annotate('Wind surpasses other sources', xy=(2015, 300), xytext=(2012.5, 400),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='darkblue')

ax.annotate('Rapid Solar Growth', xy=(2018, 600), xytext=(2016, 700),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='orange'),
            fontsize=10, color='orange')

# Add a description box if needed
props = dict(boxstyle='round', facecolor='lightblue', alpha=0.3)
textstr = 'A decade marked by notable shifts\ntowards renewable energy sources.'
ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()