import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data for the chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass']
energy_production = np.array([1200, 1400, 1600, 400, 600])  # in TWh

# Construct some example data for percentage growth
growth_rates = np.array([0.05, 0.03, 0.04, 0.02, 0.045])  # hypothetical growth rates

# Colors for the bars using gradients
base_colors = ['#FFD700', '#00BFFF', '#32CD32', '#FF6347', '#8B4513']
gradient_colors = ['#FFF5CC', '#CCF0FF', '#C9ECC9', '#FFC1B3', '#D2B48C']

# Create positions for the bars on the x-axis
positions = np.arange(len(energy_sources))

# Create the figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot bar chart with gradient effect
for idx, (base_color, grad_color) in enumerate(zip(base_colors, gradient_colors)):
    ax1.bar(positions[idx], energy_production[idx], color=base_color, edgecolor=grad_color, linewidth=3, hatch='//', width=0.6)

# Set x-ticks and labels
ax1.set_xticks(positions)
ax1.set_xticklabels(energy_sources, fontsize=12, rotation=45, ha='right')

# Set the primary y-axis label
ax1.set_ylabel('Energy Production (TWh)', fontsize=14, color='black')

# Set the chart title with multiple lines
ax1.set_title('Renewable Energy Revolution:\nGlobal Production Shares and Growth in 2023', 
              fontsize=16, fontweight='bold', pad=20)

# Annotate each bar with its value and percentage share
total_production = np.sum(energy_production)
for idx, bar in enumerate(ax1.patches):
    height = bar.get_height()
    percentage = (height / total_production) * 100
    ax1.annotate(f'{height} TWh\n({percentage:.1f}%)',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5),  # Offset to display above the bar
                 textcoords="offset points",
                 ha='center', va='bottom',
                 fontsize=10, color='black')

# Customize y-axis grid for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Secondary y-axis for growth rates
ax2 = ax1.twinx()
ax2.set_ylabel('Growth Rate', fontsize=14, color='blue')
ax2.plot(positions, growth_rates * 100, color='blue', linestyle='-', marker='o')
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.1f}%'))
ax2.spines['right'].set_color('blue')
ax2.tick_params(axis='y', colors='blue')

# Adding a legend
custom_lines = [plt.Line2D([0], [0], color=color, lw=4, label=label) for color, label in zip(base_colors, energy_sources)]
ax1.legend(handles=custom_lines, loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()