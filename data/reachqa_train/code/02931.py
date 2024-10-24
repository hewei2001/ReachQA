import matplotlib.pyplot as plt
import numpy as np

# Extended data for transport modes across multiple years
transport_modes = ['Hyperloop', 'Flying Cars', 'MagLev Trains', 'Teleports', 'Autonomous Buses', 
                   'Electric Scooters', 'Solar Wings', 'Quantum Pods']
years = ['2050', '2060', '2070']

# Adoption rates for each transport mode over the years (in thousands)
adoption_rates = np.array([
    [80, 100, 120],  # Hyperloop
    [120, 150, 180],  # Flying Cars
    [150, 160, 170],  # MagLev Trains
    [60, 80, 100],    # Teleports
    [90, 110, 130],   # Autonomous Buses
    [50, 70, 90],     # Electric Scooters
    [40, 60, 80],     # Solar Wings
    [30, 50, 70]      # Quantum Pods
])

# Colors and patterns for each transport mode
colors = ['#6a5acd', '#ff69b4', '#ff8c00', '#32cd32', '#4682b4', '#1e90ff', '#ffa500', '#b03060']
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', '*']

# Number of transport modes
n_modes = len(transport_modes)
bar_width = 0.25
x_positions = np.arange(n_modes)

fig, ax = plt.subplots(figsize=(14, 9))

# Plot grouped bar chart for each year
for i, year in enumerate(years):
    ax.bar(x_positions + i * bar_width, adoption_rates[:, i], width=bar_width, color=colors, edgecolor='black', hatch=hatches[i], label=f'Year {year}')

# Adding titles and labels
ax.set_title('Transport Mode Adoption Rates across Different Future Years\nA Complex Chart for Mathematical Analysis', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Transport Modes', fontsize=14)
ax.set_ylabel('Adoption Rate (in thousands)', fontsize=14)

# Assign the x-ticks and labels
ax.set_xticks(x_positions + bar_width)
ax.set_xticklabels(transport_modes, fontsize=12, rotation=30, ha='right')

# Annotating the bars with their respective values and percentage change
for i in range(n_modes):
    for j in range(len(years)):
        yval = adoption_rates[i, j]
        xval = x_positions[i] + j * bar_width
        ax.text(xval, yval + 2, f'{yval}k', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add a legend to describe each year
ax.legend(title='Year', title_fontsize='12', loc='upper left', fontsize=10, frameon=False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()