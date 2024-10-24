import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Energy consumption data in quadrillion BTUs for each sector
transportation = np.array([28.3, 29.0, 29.5, 30.0, 30.5, 30.8, 31.2, 31.5, 31.8, 32.0, 32.5])
residential = np.array([21.5, 21.3, 21.1, 21.0, 20.8, 20.6, 20.4, 20.3, 20.2, 20.1, 20.0])
industrial = np.array([22.7, 22.9, 23.1, 23.3, 23.5, 23.6, 23.8, 24.0, 24.1, 24.3, 24.5])
commercial = np.array([18.2, 18.5, 18.9, 19.2, 19.5, 19.7, 20.0, 20.2, 20.4, 20.6, 20.8])

# Total energy consumption (as a line plot overlay)
total_energy = transportation + residential + industrial + commercial

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Stacked area chart
ax1.stackplot(years, transportation, residential, industrial, commercial, 
              labels=['Transportation', 'Residential', 'Industrial', 'Commercial'], 
              colors=['#FF9999', '#66B2FF', '#99FF99', '#FFD700'], 
              alpha=0.8)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Consumption (Quadrillion BTUs)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Overlay line plot for total energy consumption
ax2 = ax1.twinx()
ax2.plot(years, total_energy, color='purple', linestyle='--', marker='o', label='Total Energy', linewidth=2)
ax2.set_ylabel('Total Energy Consumption (Quadrillion BTUs)', fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Add data annotations
for i, txt in enumerate(total_energy):
    ax2.annotate(f'{txt:.1f}', (years[i], total_energy[i]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=8)

# Legends
ax1.legend(loc='upper left', bbox_to_anchor=(0.0, 1), fontsize=10, title='Sectors')
ax2.legend(loc='upper left', bbox_to_anchor=(0.0, 1.12), fontsize=10)

# Title
plt.title('Energy Consumption Trends Across Different Sectors (2010-2020)\nIncluding Total Consumption as an Overlay', fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()