import matplotlib.pyplot as plt
import numpy as np

# Define countries and energy sources
countries = ["Sunlandia", "Hydrovia", "Nuketopia", "Fossilia"]
energy_sources = ["Coal", "Natural Gas", "Nuclear", "Hydropower", "Solar"]

# Energy source distribution (percentage)
data = np.array([
    [5, 10, 5, 30, 50],  # Sunlandia
    [10, 10, 5, 60, 15], # Hydrovia
    [20, 10, 50, 5, 15], # Nuketopia
    [40, 40, 10, 5, 5]   # Fossilia
])

# Renewable sources indices (Hydropower and Solar)
renewable_indices = [3, 4]
renewable_percentages = data[:, renewable_indices].sum(axis=1)

# Colors for each energy source
colors = ['#8B4513', '#4682B4', '#FFD700', '#32CD32', '#FFA500']

# Plot setup
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot each energy source as a stack on the bar chart
bottom = np.zeros(len(countries))
for idx, (source, color) in enumerate(zip(energy_sources, colors)):
    ax1.bar(countries, data[:, idx], bottom=bottom, color=color, edgecolor='grey', label=source)
    bottom += data[:, idx]

# Title and axis labels
ax1.set_title("Energy Source Distribution and Renewable Trends\nin Ecolandia (2023)", fontsize=16, fontweight='bold', loc='center', pad=15)
ax1.set_xlabel("Countries", fontsize=14, labelpad=10)
ax1.set_ylabel("Percentage of Total Energy", fontsize=14, labelpad=10)
ax1.set_ylim(0, 100)

# Overlay line plot for renewable energy percentages
ax2 = ax1.twinx()
ax2.plot(countries, renewable_percentages, color='cyan', marker='o', linestyle='-', linewidth=2, markersize=8, label='Total Renewable Energy')
ax2.set_ylabel("Renewable Energy (%)", fontsize=14, labelpad=10)
ax2.set_ylim(0, 100)

# Add percentage labels on each stack
for country_idx, country in enumerate(countries):
    cumulative = 0
    for value in data[country_idx]:
        ax1.text(country, cumulative + value / 2, f'{value}%', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
        cumulative += value

# Add legends
ax1.legend(title="Energy Sources", bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.legend(title="Trends", bbox_to_anchor=(1.05, 0.8), loc='upper left')

# Customize grid lines and adjust layout
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()