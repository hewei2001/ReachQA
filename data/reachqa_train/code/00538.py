import matplotlib.pyplot as plt
import numpy as np

# Sectors and types of energy
sectors = ['Transportation', 'Industry', 'Residential', 'Commercial']
energy_sources = ['Solar', 'Wind', 'Biomass']

# Hypothetical energy consumption data in terawatt-hours (TWh)
energy_data = np.array([
    [50, 30, 20],  # Transportation
    [70, 50, 30],  # Industry
    [40, 40, 40],  # Residential
    [60, 40, 20]   # Commercial
])

# Stacked bar plot
fig, ax = plt.subplots(figsize=(10, 7))

# Colors for each energy source
colors = ['#ffcc00', '#1f78b4', '#33a02c']

# Plotting each energy type
bottom = np.zeros(len(sectors))
for i in range(energy_data.shape[1]):
    ax.bar(sectors, energy_data[:, i], bottom=bottom, color=colors[i], edgecolor='black', label=energy_sources[i], alpha=0.8)
    bottom += energy_data[:, i]

# Title and labels
ax.set_title('Renewable Energy Consumption\nby Sector in 2030', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Sectors', fontsize=12)
ax.set_ylabel('Energy Consumption (TWh)', fontsize=12)

# Add value labels
for i, sector in enumerate(sectors):
    cumulative_height = 0
    for j in range(energy_data.shape[1]):
        value = energy_data[i, j]
        cumulative_height += value
        ax.text(i, cumulative_height - value/2, str(value), ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Legend
ax.legend(title="Energy Sources", fontsize=11, loc='upper right', bbox_to_anchor=(1.12, 1))

# Adjust layout to prevent overlap
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()