import matplotlib.pyplot as plt
import numpy as np

# Define the years and data for renewable energy contributions and total energy consumption
years = np.array([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020])
renewable_contribution = np.array([5, 8, 12, 18, 26, 35, 42, 50, 58, 66, 75])
total_energy_consumption = np.array([4200, 4180, 4150, 4100, 4050, 3950, 3800, 3700, 3600, 3550, 3500])

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot renewable energy contribution as a line chart
ax1.plot(years, renewable_contribution, marker='o', color='mediumseagreen', linestyle='-', linewidth=2, markersize=8, label='Renewable Energy Contribution (%)')

# Annotate points for renewables
for i, value in enumerate(renewable_contribution):
    ax1.text(years[i], value + 2, f"{value}%", ha='center', fontsize=9, color='mediumseagreen')

# Set labels and title for the primary axis
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Renewable Energy Contribution (%)', fontsize=12, fontweight='bold', color='mediumseagreen')
ax1.set_title('Transforming EcoCity:\nThe Rise of Renewable Energy and Changing Consumption Patterns (2000-2020)', 
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.grid(True, linestyle='--', alpha=0.5)

# Create secondary y-axis for total energy consumption
ax2 = ax1.twinx()
ax2.plot(years, total_energy_consumption, marker='s', color='steelblue', linestyle='--', linewidth=2, markersize=8, label='Total Energy Consumption (Million kWh)')

# Annotate points for energy consumption
for i, value in enumerate(total_energy_consumption):
    ax2.text(years[i], value - 100, f"{value}M", ha='center', fontsize=9, color='steelblue')

# Set label for the secondary axis
ax2.set_ylabel('Total Energy Consumption (Million kWh)', fontsize=12, fontweight='bold', color='steelblue')

# Add legend for both datasets
fig.legend(loc='upper right', bbox_to_anchor=(0.88, 0.85), fontsize=10, frameon=False)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()