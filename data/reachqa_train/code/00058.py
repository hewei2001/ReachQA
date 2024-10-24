import numpy as np
import matplotlib.pyplot as plt

# Define the years and energy production data for each source
years = np.arange(2010, 2020)

# Adjusted data for each renewable energy source (in TWh)
solar_energy = np.array([15, 25, 35, 50, 70, 95, 125, 160, 200, 245])
wind_energy = np.array([40, 55, 80, 105, 140, 180, 230, 290, 360, 440])
hydropower = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145])
biomass_energy = np.array([10, 15, 25, 35, 50, 70, 95, 125, 160, 200])

# Stacking the data
energy_data = np.vstack([solar_energy, wind_energy, hydropower, biomass_energy])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(14, 9))

colors = ['#FFDD44', '#33AADD', '#77CC44', '#CC8844']
patterns = ['/', '\\', 'x', '-']
stack = ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower', 'Biomass'],
                     colors=colors, alpha=0.9)

# Add patterns to the areas for better differentiation
for poly, pattern in zip(stack, patterns):
    poly.set_hatch(pattern)

# Customize the plot
ax.set_title('Trends in Renewable Energy Production\nOver a Decade (2010-2019)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)

# Add legend
ax.legend(loc='upper left', fontsize=12, title='Energy Source', frameon=False)

# Grid and minor grid lines
ax.grid(linestyle='--', alpha=0.6)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)

# Enhance readability of x-axis labels
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1001, 100))

# Trend lines
for i, data in enumerate(energy_data):
    ax.plot(years, data + np.sum(energy_data[:i], axis=0), color=colors[i], linestyle='--', linewidth=2)

# Annotate significant points or changes
ax.annotate('Wind exceeds other sources', xy=(2015, 300), xytext=(2012.5, 500),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='darkblue')

ax.annotate('Rapid Solar Growth', xy=(2018, 600), xytext=(2016, 750),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='orange'),
            fontsize=12, color='orange')

# Add a description box
props = dict(boxstyle='round', facecolor='lightblue', alpha=0.3)
textstr = ('A decade marked by notable shifts\n'
           'towards renewable energy sources.\n'
           'Innovations & policies accelerated growth.')
ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Highlight the first and last year values
for idx, energy in enumerate(['Solar', 'Wind', 'Hydropower', 'Biomass']):
    ax.annotate(f'{solar_energy[0]}', (2010, energy_data[idx, 0]), textcoords="offset points", xytext=(-15,5), ha='center')
    ax.annotate(f'{solar_energy[-1]}', (2019, energy_data[idx, -1] + np.sum(energy_data[:idx, -1])), textcoords="offset points", xytext=(-15,-10), ha='center')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()