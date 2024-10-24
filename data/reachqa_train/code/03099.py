import matplotlib.pyplot as plt
import numpy as np

# Define a more detailed dataset for each year
years = np.arange(2000, 2021)

# Renewable energy contribution as percentage
renewable_contribution = np.array([5, 6, 7, 8, 9, 11, 14, 18, 22, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

# Total energy consumption in million kWh
total_energy_consumption = np.array([4200, 4190, 4180, 4170, 4160, 4140, 4120, 4100, 4080, 4060, 4040, 4020, 4000, 3980, 3960, 3940, 3920, 3900, 3880, 3860, 3840])

# Carbon emissions in million tons (hypothetical data)
carbon_emissions = np.array([200, 198, 197, 195, 193, 190, 185, 180, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125, 120, 115])

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot renewable energy contribution as a line chart
ax1.plot(years, renewable_contribution, marker='o', color='mediumseagreen', linestyle='-', linewidth=2, markersize=6, label='Renewable Energy Contribution (%)')

# Annotate points for renewables
for i, value in enumerate(renewable_contribution):
    ax1.text(years[i], value + 2, f"{value}%", ha='center', fontsize=8, color='mediumseagreen')

# Set labels and title for the primary axis
ax1.set_xlabel('Year', fontsize=11, fontweight='bold')
ax1.set_ylabel('Renewable Energy Contribution (%)', fontsize=11, fontweight='bold', color='mediumseagreen')
ax1.set_title('Transforming EcoCity:\nThe Rise of Renewable Energy, Consumption Patterns, and Emissions (2000-2020)', 
              fontsize=13, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.grid(True, linestyle='--', alpha=0.5)

# Create secondary y-axis for total energy consumption
ax2 = ax1.twinx()
ax2.plot(years, total_energy_consumption, marker='s', color='steelblue', linestyle='--', linewidth=2, markersize=6, label='Total Energy Consumption (Million kWh)')

# Annotate points for energy consumption
for i, value in enumerate(total_energy_consumption):
    ax2.text(years[i], value - 70, f"{value}M", ha='center', fontsize=8, color='steelblue')

# Set label for the secondary axis
ax2.set_ylabel('Total Energy Consumption (Million kWh)', fontsize=11, fontweight='bold', color='steelblue')

# Create third y-axis for carbon emissions
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, carbon_emissions, marker='^', color='indianred', linestyle='-.', linewidth=2, markersize=6, label='Carbon Emissions (Million Tons)')

# Annotate points for carbon emissions
for i, value in enumerate(carbon_emissions):
    ax3.text(years[i], value + 2, f"{value}M", ha='center', fontsize=8, color='indianred')

# Set label for the third axis
ax3.set_ylabel('Carbon Emissions (Million Tons)', fontsize=11, fontweight='bold', color='indianred')

# Calculate and annotate growth rate for renewables
for i in range(1, len(years)):
    growth_rate = ((renewable_contribution[i] - renewable_contribution[i-1]) / renewable_contribution[i-1]) * 100
    ax1.text(years[i], renewable_contribution[i] - 10, f"{growth_rate:.1f}%", ha='center', fontsize=7, color='darkgreen')

# Add legend for all datasets
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=9, frameon=False)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()