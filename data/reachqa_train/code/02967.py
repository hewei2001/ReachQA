import matplotlib.pyplot as plt
import numpy as np

# Years and energy sources
years = ['2010', '2013', '2016', '2019', '2022']
sources = ['Coal', 'Natural Gas', 'Oil', 'Nuclear', 'Renewables']

# Data in terawatt-hours (TWh)
coal = [4200, 4000, 3800, 3600, 3300]
natural_gas = [3000, 3200, 3400, 3600, 3800]
oil = [3800, 3700, 3600, 3500, 3400]
nuclear = [800, 850, 900, 950, 1000]
renewables = [600, 800, 1100, 1500, 2000]

# Stacked data preparation
energy_data = np.array([coal, natural_gas, oil, nuclear, renewables])

# Plotting the stacked bar chart
plt.figure(figsize=(12, 7))
bottom_values = np.zeros(len(years))

# Define colors for each energy source
colors = ['#8b0000', '#ff6347', '#ff8c00', '#ffd700', '#32cd32']

# Iterate through each source to stack them
for i, source in enumerate(sources):
    plt.bar(years, energy_data[i], bottom=bottom_values, color=colors[i], label=source, alpha=0.85)
    bottom_values += energy_data[i]

# Add titles and labels
plt.title('Decade of Transition: Global Energy Consumption\nby Source', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Energy Consumption (TWh)', fontsize=12, fontweight='bold')

# Customize legend
plt.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.15, 1.0))

# Customize grid lines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotations to highlight trends
for i, year in enumerate(years):
    total_energy = np.sum(energy_data[:, i])
    plt.text(year, total_energy + 100, f'{total_energy} TWh', ha='center', fontweight='bold')

# Adjust the layout to prevent text overlap
plt.tight_layout()

# Show plot
plt.show()