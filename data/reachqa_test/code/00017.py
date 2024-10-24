import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy adoption across regions
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
solar = [200, 180, 220, 110, 130]
wind = [150, 200, 140, 80, 100]
hydro = [100, 120, 90, 50, 120]

# Additional data: Total energy consumption including non-renewables (in TWh)
total_energy = [600, 700, 650, 300, 400]  # Hypothetical data

# Set figure size and create a new plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Bar width
bar_width = 0.5
# Position of bars on x-axis
indices = np.arange(len(regions))

# Plotting stacked bars
ax1.bar(indices, solar, bar_width, label='Solar', color='gold', alpha=0.7)
ax1.bar(indices, wind, bar_width, bottom=solar, label='Wind', color='skyblue', alpha=0.7)
ax1.bar(indices, hydro, bar_width, bottom=np.array(solar) + np.array(wind), label='Hydro', color='seagreen', alpha=0.7)

# Setting titles and labels
ax1.set_title('Renewable Energy Adoption Across Regions\n2023 Analysis & Total Energy Consumption', fontsize=16, fontweight='bold')
ax1.set_xlabel('Region', fontsize=14)
ax1.set_ylabel('Renewable Energy Consumption (TWh)', fontsize=14)

# Customizing x-ticks
ax1.set_xticks(indices)
ax1.set_xticklabels(regions, rotation=15, ha='right', fontsize=12)

# Adding legend
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Type')

# Gridlines for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Overlay plot: line plot for total energy consumption
ax2 = ax1.twinx()  # Create a second y-axis
ax2.plot(indices, total_energy, color='red', marker='o', linestyle='-', linewidth=2, label='Total Energy Consumption')
ax2.set_ylabel('Total Energy Consumption (TWh)', fontsize=14, color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.9), title='Total Consumption')

# Annotate significant data points on the line plot
for i, value in enumerate(total_energy):
    ax2.annotate(f'{value} TWh', xy=(i, value), xytext=(0, 10), textcoords='offset points', ha='center', color='red', fontsize=10)

# Automatically adjust subplot parameters for a neat layout
fig.tight_layout()

# Display the plot
plt.show()