import matplotlib.pyplot as plt

# Define energy sources and their percentage contributions for 2050
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Nuclear', 'Geothermal', 'Biomass', 'Natural Gas', 'Others']
percentages_2050 = [25, 20, 15, 10, 5, 5, 15, 5]

# Current percentages for 2020
percentages_2020 = [15, 10, 20, 15, 3, 7, 25, 5]

# Colors for each energy source
colors = ['gold', 'skyblue', 'lightgreen', 'orange', 'purple', 'brown', 'lightcoral', 'grey']

# Create a subplot figure with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot horizontal bar chart for 2050
bars = axes[0].barh(energy_sources, percentages_2050, color=colors)
axes[0].set_title('Projected Energy Consumption\nby Source in 2050', fontsize=12, pad=20)
axes[0].set_xlabel('Percentage of Total Energy Consumption', fontsize=10)
axes[0].set_xlim(0, 100)
for bar, percentage in zip(bars, percentages_2050):
    axes[0].text(percentage + 1, bar.get_y() + bar.get_height() / 2, f'{percentage}%', va='center', ha='left', fontsize=9)
axes[0].spines['right'].set_visible(False)
axes[0].spines['top'].set_visible(False)
axes[0].legend(bars, energy_sources, loc='lower right', title='Energy Sources', fontsize=8)

# Plot pie chart for 2020
axes[1].pie(percentages_2020, labels=energy_sources, autopct='%1.1f%%', startangle=140, colors=colors)
axes[1].set_title('Energy Consumption\nby Source in 2020', fontsize=12, pad=20)

# Adjust layout to fit the plot area
plt.tight_layout()

# Show plot
plt.show()