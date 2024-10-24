import matplotlib.pyplot as plt
import numpy as np

# Define a larger set of events with subcategories (MWh changes)
events = [
    "Baseline", 
    "Solar Arrays", "Wind Turbines", "Geothermal", "Hydro",  # Renewable sources
    "Efficient Appliances", "Smart Grids", "LED Lighting",  # Efficiency improvements
    "Sandstorm Surge", "Seasonal Variability",  # Environmental impacts
    "Agri Optimization", "Waste Management", "Water Recycling",  # Sustainability measures
    "Equipment Malfunction", "Energy Theft",  # Operational issues
    "Recycling Efficiency", "Carbon Capture",  # Environmental mitigation
    "Net"
]

# Define the energy changes for each event
changes = np.array([
    5000, 
    1000, 500, -300, 200,  # Renewables
    -500, -400, -250,  # Efficiency
    700, 150,  # Environmental impacts
    -300, -200, -100,  # Sustainability
    600, 200,  # Operational issues
    -150, -350  # Mitigation
])
cumulative = np.cumsum(changes)

# Cumulative changes including starting baseline
cumulative = np.insert(cumulative, 0, 0)
end_total = cumulative[-1]

# Define colors for different categories
colors = ['blue'] + ['green', 'green', 'green', 'green'] + \
         ['orange', 'orange', 'orange'] + ['red', 'red'] + \
         ['olive', 'olive', 'olive'] + ['purple', 'purple'] + \
         ['teal', 'teal'] + ['purple']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot waterfall chart
bar_width = 0.5
ax.bar(events, np.append(changes, end_total), color=colors, edgecolor='black', width=bar_width)

# Draw connecting lines
for i in range(1, len(events) - 1):
    ax.plot([i - 1, i], [cumulative[i - 1], cumulative[i]], 'k-', lw=2)

# Set title and labels
ax.set_title('Mars Colony Energy Consumption Changes\n"Red Dune Haven": Detailed Breakdown', fontsize=16, pad=20)
ax.set_xlabel('Events', fontsize=12)
ax.set_ylabel('Energy Consumption Change (MWh)', fontsize=12)

# Annotate bars with the change in energy
for i, change in enumerate(np.append(changes, end_total)):
    ax.text(i, change + (150 if change >= 0 else -150), 
            f'{change:+}', ha='center', va='bottom' if change >= 0 else 'top', 
            fontsize=10, color='black')

# Rotate x-axis labels and manage text overflow
ax.set_xticklabels(events, rotation=45, ha='right', fontsize=9, wrap=True)

# Add grid for clarity
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Add a legend to explain color coding
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='blue', lw=4, label='Baseline'),
    Line2D([0], [0], color='green', lw=4, label='Renewable Energy Sources'),
    Line2D([0], [0], color='orange', lw=4, label='Efficiency Improvements'),
    Line2D([0], [0], color='red', lw=4, label='Environmental Impacts'),
    Line2D([0], [0], color='olive', lw=4, label='Sustainability Measures'),
    Line2D([0], [0], color='purple', lw=4, label='Operational Issues'),
    Line2D([0], [0], color='teal', lw=4, label='Environmental Mitigation')
]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))

# Use tight layout to avoid overlapping elements
plt.tight_layout()

# Show the plot
plt.show()