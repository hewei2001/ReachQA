import matplotlib.pyplot as plt
import numpy as np

# Define regions and renewable energy types
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Africa']
energy_types = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']

# Installed capacity data for each region and energy type (in GW)
capacities = [
    [150, 120, 110, 60, 30],   # North America
    [180, 200, 95, 45, 25],    # Europe
    [250, 300, 150, 70, 40],   # Asia-Pacific
    [100, 80, 120, 35, 15],    # Latin America
    [60, 50, 90, 20, 10]       # Africa
]

# Growth rate data for each energy type over 5 years (in percentage)
growth_rates = [
    [4.2, 5.5, 2.1, 1.8, 3.5],  # Solar
    [3.5, 6.0, 4.0, 2.5, 3.0],  # Wind
    [2.0, 1.5, 3.0, 2.2, 1.0],  # Hydro
    [1.8, 2.5, 1.8, 1.0, 0.8],  # Biomass
    [3.0, 2.8, 2.5, 1.5, 2.0]   # Geothermal
]

# Convert the data into NumPy arrays
capacities = np.array(capacities)
growth_rates = np.array(growth_rates)

# Setup the subplot figure
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Bar plot for installed capacities
ax1 = axes[0]
x = np.arange(len(regions))
width = 0.15
colors = ['#FF5733', '#33A1FF', '#33FF57', '#FFD733', '#FF33A1']

for i, energy_type in enumerate(energy_types):
    bar = ax1.bar(x + i * width, capacities[:, i], width, label=energy_type, color=colors[i])
    for rect in bar:
        height = rect.get_height()
        ax1.annotate(f'{height}',
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=9)

ax1.set_xlabel('Regions', fontsize=12)
ax1.set_ylabel('Installed Capacity (GW)', fontsize=12)
ax1.set_title('The Rise of Renewable Energy:\nInstalled Capacity in Global Regions (2023)', fontsize=14, weight='bold')
ax1.set_xticks(x + width * (len(energy_types) / 2 - 0.5))
ax1.set_xticklabels(regions, fontsize=10)
ax1.legend(title='Energy Type', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Line plot for growth rates
ax2 = axes[1]
years = np.arange(2019, 2024)
markers = ['o', 's', 'D', '^', 'v']

for i, energy_type in enumerate(energy_types):
    ax2.plot(years, growth_rates[i], marker=markers[i], label=energy_type, color=colors[i])

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_title('Annual Growth Rates of Renewable Energy Types\n(2019-2023)', fontsize=14, weight='bold')
ax2.legend(title='Energy Type', fontsize=10)
ax2.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Ensure the layout fits well
plt.tight_layout()
plt.show()