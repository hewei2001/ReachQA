import matplotlib.pyplot as plt
import numpy as np

# Energy sources and their projected percentage contributions in 2050
energy_sources = ['Solar', 'Wind', 'Nuclear', 'Coal', 'Natural Gas', 'Hydroelectric']
percentages_2050 = [25, 20, 15, 10, 20, 10]  # Example data for 2050

# Hypothetical data representing past percentages (2020) for the overlay plot
percentages_2020 = [10, 15, 13, 25, 30, 7]  # Example historical data

# Calculate growth or reduction percentages for overlay
growth_percentages = [(p2050 - p2020) / p2020 * 100 for p2050, p2020 in zip(percentages_2050, percentages_2020)]

# Plotting setup
fig, ax1 = plt.subplots(figsize=(12, 8))

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#C0C0C0', '#696969', '#FF8C00', '#00CED1']

# Create horizontal bar chart
bars = ax1.barh(energy_sources, percentages_2050, color=colors, label='Projected 2050')

# Add text annotations for each bar to show the percentage
for bar, percentage in zip(bars, percentages_2050):
    ax1.text(bar.get_width() - 1.5, bar.get_y() + bar.get_height() / 2, f'{percentage}%', 
             va='center', ha='right', color='white', fontsize=10, fontweight='bold')

# Customize the bar chart
ax1.set_title('Global Energy Landscape 2050:\nA Shift Towards Sustainability', fontsize=14, fontweight='bold')
ax1.set_xlabel('Percentage of Global Energy Consumption', fontsize=12)
ax1.set_xlim(0, 30)
ax1.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_axisbelow(True)

# Create a secondary y-axis for the growth percentages
ax2 = ax1.twiny()
ax2.plot(growth_percentages, energy_sources, 'o-', color='darkgreen', label='Growth from 2020 (%)')
ax2.set_xlabel('Growth (%)', fontsize=12)
ax2.xaxis.set_ticks_position('top')
ax2.xaxis.set_label_position('top')

# Add annotations to the line plot
for i, growth in enumerate(growth_percentages):
    ax2.annotate(f'{growth:.1f}%', xy=(growth, i), xytext=(5, -10), textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='green'), color='green')

# Adjust layout and add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.65, 0.85), fontsize=10, frameon=False)

# Prevent layout overlap
plt.tight_layout()

# Display the plot
plt.show()