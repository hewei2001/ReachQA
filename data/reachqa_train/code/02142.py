import matplotlib.pyplot as plt
import numpy as np

# Define energy sources and their contribution percentages
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
percentages = [40, 30, 15, 10, 5]  # Percent contributions to total energy consumption

# Colors for the bars
colors = ['#FFD700', '#00BFFF', '#32CD32', '#8B4513', '#FF6347']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot a horizontal bar chart
bars = ax.barh(energy_sources, percentages, color=colors)

# Add percentage labels on each bar
for bar, percentage in zip(bars, percentages):
    ax.text(bar.get_width() - 3, bar.get_y() + bar.get_height() / 2, f'{percentage}%', 
            va='center', ha='right', color='white', fontsize=12, fontweight='bold')

# Add title and labels
ax.set_title('Energy Sources in NeoTerra City\n2050 Renewable Energy Mix', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Percentage of Total Energy Consumption', fontsize=12)
ax.set_xlim(0, 50)  # Fix x-limit to clearly show full percentages

# Customize y-axis
ax.set_yticks(range(len(energy_sources)))
ax.set_yticklabels(energy_sources, fontsize=11)

# Add grid lines for better visualization
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend with customized handles
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
ax.legend(handles, energy_sources, title='Energy Sources', loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()