import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Define years and energy production data
years = np.arange(2013, 2023)
solar_energy = [12, 20, 35, 50, 70, 100, 130, 160, 190, 220]
wind_energy = [40, 55, 75, 95, 120, 150, 180, 210, 245, 280]
hydro_energy = [100, 102, 105, 110, 115, 120, 125, 130, 135, 140]

# Stack the data to show cumulative energy production
production_data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Plot the area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, production_data, labels=['Solar Energy', 'Wind Energy', 'Hydroelectric Energy'],
             colors=['#E63946', '#457B9D', '#A8DADC'], alpha=0.9)

# Add titles and labels
plt.title('Renewable Energy Production Trends\nOver the Last Decade (2013-2022)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('Energy Production (TWh)', fontsize=12, labelpad=10)

# Customizing ticks and grid
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 701, 100))
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add trendlines
for i, color in enumerate(['#FFA07A', '#87CEFA', '#98FB98']):
    z = np.polyfit(years, production_data[i], 1)
    p = np.poly1d(z)
    ax.plot(years, p(years), linestyle='--', color=color, alpha=0.7)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Annotate notable trends with callouts
ax.annotate('Rapid Solar Growth', xy=(2018, 70), xytext=(2014, 250),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='darkorange', horizontalalignment='center')

ax.annotate('Steady Wind Expansion', xy=(2020, 215), xytext=(2016, 500),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='blue', horizontalalignment='center')

# Adjust layout
plt.tight_layout()

# Create inset plot for detailed view of solar energy growth
left, bottom, width, height = [0.15, 0.55, 0.25, 0.25]
ax_inset = fig.add_axes([left, bottom, width, height])
ax_inset.plot(years, solar_energy, marker='o', color='#E63946', linestyle='-')
ax_inset.set_title('Solar Energy Focus', fontsize=10)
ax_inset.set_xlabel('Year', fontsize=8)
ax_inset.set_ylabel('Solar Energy (TWh)', fontsize=8)
ax_inset.tick_params(axis='both', which='major', labelsize=8)
ax_inset.yaxis.set_major_locator(ticker.MultipleLocator(20))

# Show the plot
plt.show()