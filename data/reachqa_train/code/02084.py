import matplotlib.pyplot as plt
import numpy as np

# Data: Countries and their renewable energy adoption percentages
countries = ['Norway', 'Germany', 'China', 'United States', 'India', 'Brazil', 'Spain', 'Australia', 'Japan', 'South Africa']
renewable_percentages = [98, 48, 35, 20, 28, 83, 45, 41, 25, 18]

# Additional data for overlay: CO2 emission reduction percentages
co2_reduction = [90, 52, 32, 10, 20, 78, 38, 37, 15, 12]

# Colors for each country using shades of green
colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(countries)))

# Create horizontal bar chart with overlay
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart
bars = ax1.barh(countries, renewable_percentages, color=colors, edgecolor='black', height=0.6)
ax1.set_xlabel('Percentage of Energy from Renewables (%)', fontsize=12)
ax1.set_xlim(0, 100)
ax1.set_yticks(np.arange(len(countries)))
ax1.set_yticklabels(countries, fontsize=12)
ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.bar_label(bars, fmt='%.0f%%', padding=3, fontsize=11)

# Create a secondary y-axis for the line plot
ax2 = ax1.twiny()
ax2.plot(co2_reduction, countries, 'o-', color='red', markerfacecolor='white', markersize=8, linewidth=2, label='CO2 Reduction (%)')
ax2.set_xlabel('CO2 Emission Reduction (%)', fontsize=12)
ax2.set_xlim(0, 100)
ax2.xaxis.label.set_color('red')
ax2.tick_params(axis='x', colors='red')

# Title and subtitle
ax1.set_title('Renewable Energy Adoption and\nCO2 Emission Reduction by Country in 2023', fontsize=16, fontweight='bold', pad=20)

# Legend
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9), fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()