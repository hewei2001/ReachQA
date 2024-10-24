import matplotlib.pyplot as plt
import numpy as np

# Define years and energy sources
years = np.arange(2020, 2031)
energy_sources = ["Coal", "Natural Gas", "Solar Power", "Wind Power", "Nuclear", "Hydropower"]

# Define the percentage share for each energy source over the years
coal_share = [40, 35, 30, 28, 25, 20, 18, 15, 12, 10, 8]
natural_gas_share = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15]
solar_power_share = [5, 8, 10, 13, 16, 20, 24, 28, 32, 35, 38]
wind_power_share = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
nuclear_share = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
hydropower_share = [5, 6, 8, 8, 9, 10, 10, 10, 10, 10, 10]

# Stack the shares for stacked bar plot
shares = np.array([coal_share, natural_gas_share, solar_power_share, wind_power_share, nuclear_share, hydropower_share])

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar width
width = 0.6

# Create stacked bar chart
bottom = np.zeros(len(years))
colors = ['#8B4513', '#FFA07A', '#FFD700', '#00FA9A', '#4682B4', '#9ACD32']

for i, (share, color) in enumerate(zip(shares, colors)):
    ax.bar(years, share, width, bottom=bottom, color=color, edgecolor='k', label=energy_sources[i])
    bottom += share

# Add title and labels
ax.set_title("Future Energy Sources Adoption in CityX (2020-2030)", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage Share in Electricity Production", fontsize=12)

# Add legend
ax.legend(title="Energy Sources", loc='upper left', bbox_to_anchor=(1.02, 1))

# Customize ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_ylim(0, 100)

# Display grid
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate values on the chart
for year in range(len(years)):
    y_offset = 0
    for source, share in zip(energy_sources, shares[:, year]):
        if share > 3:  # Only annotate if the share is significant enough
            ax.text(years[year], y_offset + share/2, f'{share}%', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
        y_offset += share

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()