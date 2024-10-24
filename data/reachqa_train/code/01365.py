import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy production in GWh (including new regions and sources)
solar_energy = [450, 600, 350, 200, 300, 250, 150]      # North America, Europe, Asia, Oceania, South America, Africa, Middle East
wind_energy = [700, 850, 500, 300, 600, 450, 350]
hydro_energy = [1200, 950, 1500, 400, 800, 650, 500]
geothermal_energy = [300, 200, 100, 50, 70, 60, 40]
biomass_energy = [150, 220, 180, 70, 110, 90, 60]
nuclear_energy = [400, 600, 500, 200, 300, 250, 100]

# Aggregate data by energy source
data = np.array([solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy, nuclear_energy])

# Define labels for the x-axis and for the energy sources
regions = ['North America', 'Europe', 'Asia', 'Oceania', 'South America', 'Africa', 'Middle East']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Nuclear']

# Determine the number of regions and the number of energy sources
n_regions = len(regions)
n_sources = len(energy_sources)

# Define the positions of the bars
x = np.arange(n_regions)
bar_width = 0.7

# Create the main plot
fig, ax = plt.subplots(figsize=(16, 10))

# Plot stacked bars
bottom = np.zeros(n_regions)
colors = ['#FFA07A', '#20B2AA', '#87CEFA', '#FFD700', '#ADFF2F', '#FF6347']
for i, (energy, color) in enumerate(zip(data, colors)):
    bars = ax.bar(x, energy, width=bar_width, color=color, label=energy_sources[i], bottom=bottom)
    bottom += energy
    
    # Add text labels above the bars for nuclear energy (as an example)
    if i == 5:  # Only labeling nuclear energy for demonstration
        for bar in bars:
            yval = bar.get_height() + bar.get_y()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval:.0f}', ha='center', va='bottom', fontsize=9, color='white')

# Add labels and title
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)
ax.set_title('Diverse Renewable Energy Production\nAcross Regions', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(regions)

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=30, ha='right')

# Add a legend
ax.legend(title='Energy Sources', fontsize=10)

# Highlight total production for each region
total_production = data.sum(axis=0)
for idx, total in enumerate(total_production):
    ax.annotate(f'Total: {total:.0f} GWh', xy=(idx, total + 50), fontsize=10, ha='center', color='black')

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()