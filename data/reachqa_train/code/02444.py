import matplotlib.pyplot as plt
import numpy as np

# Define the regions and the renewable energy sources
regions = ['Region A', 'Region B', 'Region C', 'Region D']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass']

# Create fictional data for renewable energy capacities in GW
solar = np.array([5, 6, 7, 9, 11, 13, 15, 17, 20, 23, 26])
wind = np.array([8, 9, 10, 12, 14, 16, 18, 21, 24, 27, 30])
hydro = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
biomass = np.array([3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])

# Stack the data for each region
capacity_data = [solar, wind, hydro, biomass]

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Colors for each energy source
colors = ['#FFD700', '#00BFFF', '#7FFF00', '#FF69B4']

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Offset for each region to create visual separation in stacked bar
bar_width = 0.2
x_indexes = np.arange(len(years))

# Plotting each energy source as a stacked component
for i, source in enumerate(capacity_data):
    bottom = np.zeros(len(years)) if i == 0 else sum(capacity_data[:i])
    ax.bar(x_indexes + bar_width * i, source, width=bar_width, label=energy_sources[i], color=colors[i], alpha=0.8, bottom=bottom)

# Add the region label on top of each stack
for i, year in enumerate(years):
    total_height = sum(data[i] for data in capacity_data)
    ax.text(years[i] - 2009.5, total_height + 1, f"{regions[i%4]}", ha='center', va='bottom', fontweight='bold')

# Title and labels
ax.set_title('Cumulative Capacity of Renewable Energy Sources\nby Region: 2010-2020', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Capacity in GW', fontsize=12)

# Customize ticks
plt.xticks(ticks=x_indexes + bar_width * 1.5, labels=years, rotation=45)
plt.yticks(np.arange(0, 120, 10))

# Legend
ax.legend(title='Energy Source', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Add grid for improved readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()