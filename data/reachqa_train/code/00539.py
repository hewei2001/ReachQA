import matplotlib.pyplot as plt
import numpy as np

# Sectors and types of energy
sectors = ['Transportation', 'Industry', 'Residential', 'Commercial', 'Agriculture', 'Utilities', 'Public Services']
energy_sources = ['Solar', 'Wind', 'Biomass', 'Hydro', 'Geothermal', 'Nuclear']

# Hypothetical energy consumption data in terawatt-hours (TWh)
energy_data = np.array([
    [50, 30, 20, 10, 5, 3],   # Transportation
    [70, 50, 30, 20, 10, 15], # Industry
    [40, 40, 40, 10, 5, 0],   # Residential
    [60, 40, 20, 15, 10, 5],  # Commercial
    [30, 10, 10, 5, 10, 5],   # Agriculture
    [90, 60, 40, 30, 20, 10], # Utilities
    [20, 15, 10, 5, 5, 0]     # Public Services
])

# Stacked bar plot
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each energy source
colors = ['#ffcc00', '#1f78b4', '#33a02c', '#a6cee3', '#b2df8a', '#fb9a99']

# Plotting each energy type
bottom = np.zeros(len(sectors))
for i in range(energy_data.shape[1]):
    ax.bar(sectors, energy_data[:, i], bottom=bottom, color=colors[i], edgecolor='black', label=energy_sources[i], alpha=0.8)
    bottom += energy_data[:, i]

# Title and labels
ax.set_title('Diverse Renewable Energy Consumption\nby Sector in 2030', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Sectors', fontsize=12)
ax.set_ylabel('Energy Consumption (TWh)', fontsize=12)

# Add value labels
for i, sector in enumerate(sectors):
    cumulative_height = 0
    for j in range(energy_data.shape[1]):
        value = energy_data[i, j]
        cumulative_height += value
        ax.text(i, cumulative_height - value/2, str(value), ha='center', va='center', fontsize=9, color='white', fontweight='bold')

# Legend
ax.legend(title="Energy Sources", fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to prevent overlap
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Subplot for cumulative sum by sector
fig, ax2 = plt.subplots(figsize=(12, 4))

# Cumulative data
cumulative_data = np.sum(energy_data, axis=1)
ax2.plot(sectors, cumulative_data, marker='o', linestyle='-', color='purple', linewidth=2)

# Title and labels for subplot
ax2.set_title('Cumulative Energy Consumption by Sector', fontsize=14, fontweight='bold')
ax2.set_xlabel('Sectors', fontsize=12)
ax2.set_ylabel('Total Energy (TWh)', fontsize=12)

# Annotations
for i, (sector, total) in enumerate(zip(sectors, cumulative_data)):
    ax2.annotate(f'{total}', (i, total), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black', fontweight='bold')

# Show plots
plt.tight_layout()
plt.show()