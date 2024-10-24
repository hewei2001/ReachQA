import numpy as np
import matplotlib.pyplot as plt

# Define months and renewable energy sources
months = ['January', 'February', 'March', 'April', 'May']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass']

# Data: Energy output in Gigawatt-hours (GWh) for each source
energy_data = np.array([
    [20, 15, 25, 10],  # January
    [25, 20, 30, 15],  # February
    [30, 25, 35, 20],  # March
    [40, 30, 40, 25],  # April
    [50, 35, 45, 30]   # May
])

# Calculate cumulative energy output
cumulative_energy = np.cumsum(energy_data.sum(axis=1))

# Colors for each energy source
colors = {
    'Solar': '#FFD700',   # Gold
    'Wind': '#1E90FF',    # Dodger Blue
    'Hydro': '#00FA9A',   # Medium Spring Green
    'Biomass': '#8B4513'  # Saddle Brown
}

# Create a figure and axis with subplots for additional complexity
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create an area chart using stackplot
ax1.stackplot(months, energy_data.T, labels=energy_sources, colors=[colors[source] for source in energy_sources], alpha=0.8)

# Add annotations for each source at the last data point
for i, source in enumerate(energy_sources):
    ax1.annotate(f'{energy_data[-1, i]} GWh', xy=(months[-1], energy_data[-1, i]),
                 xytext=(-10, 10), textcoords='offset points', ha='right', fontsize=9,
                 bbox=dict(boxstyle='round,pad=0.3', edgecolor=colors[source], facecolor='white', alpha=0.7))

# Secondary y-axis for cumulative energy output
ax2 = ax1.twinx()
ax2.plot(months, cumulative_energy, color='gray', marker='o', linestyle='--', linewidth=1.5, label='Cumulative Energy (GWh)')
ax2.set_ylabel('Cumulative Energy Output (GWh)', fontsize=12)

# Add grid lines
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# Title and labels
ax1.set_title("Renaissance of Renewable Energy Sources in Wonderland\nMonthly Energy Output (GWh), 2023", fontsize=16, weight='bold', loc='center')
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Energy Output (GWh)", fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Add legend with improved positioning
ax1.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1.1, 1), fontsize=10, title_fontsize='11')
ax2.legend(loc='upper right', bbox_to_anchor=(1.1, 0.85), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()