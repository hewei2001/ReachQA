import matplotlib.pyplot as plt
import numpy as np

# Cities and energy sources
cities = ['New York', 'Tokyo', 'Berlin', 'Sydney', 'Cape Town']
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass']

# Data: percentage adoption of each energy source by city
adoption_data = [
    [30, 10, 15, 5],   # New York
    [20, 25, 10, 5],   # Tokyo
    [15, 40, 20, 10],  # Berlin
    [25, 15, 30, 10],  # Sydney
    [35, 5, 10, 20]    # Cape Town
]

# Historical data: change in adoption over years for each energy source
years = ['2020', '2021', '2022', '2023']
historical_data = {
    'Solar': [10, 20, 30, 35],
    'Wind': [15, 25, 35, 40],
    'Hydroelectric': [25, 30, 25, 30],
    'Biomass': [5, 10, 15, 20]
}

# Colors for each energy source
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Initialize the plot with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Plot 1: Grouped bar chart
bar_width = 0.15
index = np.arange(len(cities))

for i, (energy_source, color) in enumerate(zip(energy_sources, colors)):
    bars = ax1.bar(index + i * bar_width, [data[i] for data in adoption_data],
                   bar_width, label=energy_source, color=color)

    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}%',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_xlabel('Cities', fontsize=12)
ax1.set_ylabel('Adoption Percentage (%)', fontsize=12)
ax1.set_title('Renewable Energy Adoption by City', fontsize=14, fontweight='bold', pad=10)
ax1.set_xticks(index + 1.5 * bar_width)
ax1.set_xticklabels(cities, fontsize=11)
ax1.set_ylim(0, 50)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.legend(title='Energy Sources', fontsize=10, title_fontsize='12', loc='upper right')

# Plot 2: Stacked bar chart showing historical data
bottom_values = np.zeros(len(years))
for i, (energy_source, color) in enumerate(zip(energy_sources, colors)):
    ax2.bar(years, historical_data[energy_source], bottom=bottom_values,
            label=energy_source, color=color)
    bottom_values += historical_data[energy_source]

ax2.set_xlabel('Year', fontsize=12)
ax2.set_title('Cumulative Renewable Adoption Trends (2020-2023)', fontsize=14, fontweight='bold', pad=10)
ax2.set_ylim(0, 100)
ax2.set_ylabel('Cumulative Adoption (%)', fontsize=12)
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax2.legend(title='Energy Sources', fontsize=10, title_fontsize='12', loc='upper left')

# Adjust layout for better fit and readability
plt.tight_layout()

# Show plot
plt.show()