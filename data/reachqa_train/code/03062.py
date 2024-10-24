import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass']
energy_production = np.array([1200, 1400, 1600, 400, 600])  # in TWh

# Calculate total production for percentage calculation
total_production = np.sum(energy_production)

# Colors for the bars
colors = ['#FFD700', '#00BFFF', '#32CD32', '#FF6347', '#8B4513']

# Create positions for the bars on the x-axis
positions = np.arange(len(energy_sources))

# Create the figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar chart
bars = ax.bar(positions, energy_production, color=colors, width=0.6)

# Set x-ticks and labels
ax.set_xticks(positions)
ax.set_xticklabels(energy_sources, fontsize=12, rotation=45, ha='right')

# Set the y-axis label
ax.set_ylabel('Energy Production (TWh)', fontsize=14)

# Set the chart title
ax.set_title('Renewable Energy Revolution:\nGlobal Production Shares in 2023', 
             fontsize=16, fontweight='bold', pad=20)

# Annotate each bar with its value and percentage share
for bar, production in zip(bars, energy_production):
    height = bar.get_height()
    percentage = (production / total_production) * 100
    ax.annotate(f'{production} TWh\n({percentage:.1f}%)',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # Offset to display above the bar
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10, color='black')

# Customize y-axis grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()