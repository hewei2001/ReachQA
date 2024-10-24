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

# Colors for each energy source
colors = ['#8B4513', '#4682B4', '#FFD700', '#32CD32', '#FFA500']

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Bottom position for each bar stack
bottom = np.zeros(len(countries))

# Plot each energy source as a stack on the bar chart
for idx, (source, color) in enumerate(zip(energy_sources, colors)):
    ax.bar(countries, data[:, idx], bottom=bottom, color=color, edgecolor='grey', label=source)
    bottom += data[:, idx]

# Title and axis labels
ax.set_title("Energy Source Distribution in Ecolandia (2023)", fontsize=18, fontweight='bold', loc='center', pad=20)
ax.set_xlabel("Countries", fontsize=14, labelpad=10)
ax.set_ylabel("Percentage of Total Energy", fontsize=14, labelpad=10)
ax.set_ylim(0, 100)  # Ensure y-axis goes from 0 to 100 for percentage clarity

# Add percentage labels on each stack
for country_idx, country in enumerate(countries):
    cumulative = 0
    for source_idx, value in enumerate(data[country_idx]):
        ax.text(country, cumulative + value / 2, f'{value}%', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
        cumulative += value

# Add legend
ax.legend(title="Energy Sources", bbox_to_anchor=(1.05, 1), loc='upper left')

# Customize grid lines and adjust layout
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()