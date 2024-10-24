import matplotlib.pyplot as plt
import numpy as np

# Define cities and energy contribution data
cities = ['New York', 'London', 'Tokyo', 'Sydney', 'São Paulo']
solar = np.array([30, 25, 20, 35, 15])
wind = np.array([20, 30, 25, 25, 20])
hydroelectric = np.array([10, 5, 15, 10, 30])
biomass = np.array([15, 20, 25, 5, 20])
nuclear = np.array([25, 20, 15, 25, 15])

# Colors for each energy source
colors = ['#f4a261', '#2a9d8f', '#e9c46a', '#264653', '#e76f51']

# Set figure size
plt.figure(figsize=(12, 8))

# Plot each energy source as a stacked bar
plt.bar(cities, solar, color=colors[0], label='Solar')
plt.bar(cities, wind, bottom=solar, color=colors[1], label='Wind')
plt.bar(cities, hydroelectric, bottom=solar+wind, color=colors[2], label='Hydroelectric')
plt.bar(cities, biomass, bottom=solar+wind+hydroelectric, color=colors[3], label='Biomass')
plt.bar(cities, nuclear, bottom=solar+wind+hydroelectric+biomass, color=colors[4], label='Nuclear')

# Customizing the plot with title and labels
plt.title("Energy Source Contributions\nin Urban Sustainability Initiatives (2023)", fontsize=14, fontweight='bold')
plt.xlabel("Cities", fontsize=12)
plt.ylabel("Percentage Contribution (%)", fontsize=12)
plt.ylim(0, 100)
plt.xticks(fontsize=10)

# Adding a legend with energy sources
plt.legend(loc='upper left', title='Energy Source')

# Annotate each segment of the bars with its percentage contribution
for i, city in enumerate(cities):
    y_offset = 0
    for j, percentage in enumerate([solar[i], wind[i], hydroelectric[i], biomass[i], nuclear[i]]):
        plt.text(i, y_offset + percentage / 2, f'{percentage}%', ha='center', va='center', color='white', fontweight='bold')
        y_offset += percentage

# Grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()