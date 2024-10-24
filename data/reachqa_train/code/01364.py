import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy production in GWh
solar_energy = [450, 600, 350, 200]     # North America, Europe, Asia, Oceania
wind_energy = [700, 850, 500, 300]
hydro_energy = [1200, 950, 1500, 400]
geothermal_energy = [300, 200, 100, 50]

# Aggregate data by energy source
data = [solar_energy, wind_energy, hydro_energy, geothermal_energy]

# Define labels for the x-axis and for the energy sources
regions = ['North America', 'Europe', 'Asia', 'Oceania']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']

# Determine the number of regions and the number of energy sources
n_regions = len(regions)
n_sources = len(energy_sources)

# Define the positions of the bars
x = np.arange(n_regions)
bar_width = 0.2

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each energy source as a separate set of bars
colors = ['#FFA07A', '#20B2AA', '#87CEFA', '#FFD700']
for i, energy_source in enumerate(energy_sources):
    bars = ax.bar(x + i * bar_width, data[i], width=bar_width, color=colors[i], label=energy_source)
    
    # Add text labels above the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval}', ha='center', va='bottom', fontsize=9)

# Add labels and title
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)
ax.set_title('Renewable Energy Production\nAcross Different Regions and Sources', fontsize=16, fontweight='bold', pad=15)
ax.set_xticks(x + bar_width * (n_sources - 1) / 2)
ax.set_xticklabels(regions)

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=20, ha='right')

# Add a legend
ax.legend(title='Energy Sources', fontsize=10)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()