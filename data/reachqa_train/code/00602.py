import matplotlib.pyplot as plt
import numpy as np

# Names of the planetary colonies
colonies = ['Mars', 'Moon', 'Europa', 'Titan']

# Estimated efficiencies for each energy source
solar_efficiency = [48, 63, 35, 52]  # in percentage
wind_efficiency = [28, 22, 42, 38]   # in percentage
geothermal_efficiency = [53, 12, 63, 57]  # in percentage

# Estimated uncertainties (standard deviations)
solar_error = [6, 8, 4, 6]
wind_error = [5, 3, 6, 5]
geothermal_error = [9, 4, 7, 8]

# Create an array for the position of each colony
x_positions = np.arange(len(colonies))

# Width of a single bar
bar_width = 0.2

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the solar efficiency with error bars
ax.errorbar(x_positions - bar_width, solar_efficiency, yerr=solar_error, fmt='o', linestyle='-', 
            linewidth=2, capsize=5, label='Solar Energy', color='gold', markerfacecolor='yellow', alpha=0.7)

# Plot the wind efficiency with error bars
ax.errorbar(x_positions, wind_efficiency, yerr=wind_error, fmt='s', linestyle='-', 
            linewidth=2, capsize=5, label='Wind Energy', color='blue', markerfacecolor='cyan', alpha=0.7)

# Plot the geothermal efficiency with error bars
ax.errorbar(x_positions + bar_width, geothermal_efficiency, yerr=geothermal_error, fmt='^', linestyle='-', 
            linewidth=2, capsize=5, label='Geothermal Energy', color='green', markerfacecolor='lightgreen', alpha=0.7)

# Set the title and labels
ax.set_title('Renewable Energy Production Efficiency\nin Planetary Colonies, Year 2150', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Planetary Colonies', fontsize=12)
ax.set_ylabel('Efficiency (%)', fontsize=12)

# Customize the x-axis
ax.set_xticks(x_positions)
ax.set_xticklabels(colonies, fontsize=11)

# Enable grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add a legend
ax.legend(title='Energy Source', title_fontsize='13', fontsize=11, loc='upper left')

# Adjust layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()