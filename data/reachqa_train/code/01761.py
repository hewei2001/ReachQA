import matplotlib.pyplot as plt
import numpy as np

# Define the years and the energy sources
years = np.arange(2000, 2051, 10)
energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Renewables']

# Hypothetical data for each energy source over the years (% of total energy consumption)
coal = [40, 35, 30, 25, 20, 15]
natural_gas = [25, 25, 20, 20, 18, 15]
nuclear = [10, 10, 12, 14, 15, 15]
hydroelectric = [10, 12, 13, 14, 15, 16]
renewables = [5, 8, 15, 20, 32, 39]

# Stack the data to ensure they add up to 100%
data = np.vstack([coal, natural_gas, nuclear, hydroelectric, renewables])

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Create the stacked area chart
colors = ['#8c564b', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax.stackplot(years, data, labels=energy_sources, colors=colors, alpha=0.8, edgecolor='grey')

# Title and axis labels
ax.set_title('The Evolution of Energy Sources\nOver the 21st Century', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Energy Consumption (%)', fontsize=12)

# Configure x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.5)

# Legend
ax.legend(title='Energy Sources', loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()