import matplotlib.pyplot as plt
import numpy as np

# Initial carbon emissions in million tons
initial_emissions = 100

# Impacts of initiatives on emissions in million tons
data = [
    initial_emissions,  # Initial emissions
    -15,  # Reduction from renewable energy
    -10,  # Reduction from public transport
    -8,   # Reduction from waste management
    -12,  # Reduction from tree planting
    -5    # Other reductions
]

# Labels for the chart steps
labels = [
    "Initial Emissions",
    "Renewable Energy",
    "Public Transport",
    "Waste Reduction",
    "Tree Planting",
    "Miscellaneous"
]

# Calculating cumulative impacts
steps = np.zeros(len(data) + 1)
steps[1:] = np.cumsum(data)

# Color coding: Initial in blue, reductions in green
bar_color = ['#1f77b4'] + ['#2ca02c' if x < 0 else '#d62728' for x in data[1:]]

# Creating the waterfall chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars and connect with lines
for i, (val, step, label, color) in enumerate(zip(data, steps, labels, bar_color)):
    ax.bar(i, val, bottom=step, color=color, edgecolor='gray', width=0.6, label=label if i == 0 else "")
    ax.text(i, step + val/2, f'{abs(val):.1f}', ha='center', va='center', color='white')
    if i > 0:  # Draw connecting line from previous top
        ax.plot([i-1, i], [steps[i], steps[i]], color='black', linestyle='-', linewidth=0.8)

# Adding a horizontal line indicating the initial emissions level
ax.plot([-0.5, len(data)-0.5], [initial_emissions, initial_emissions], 'k--', linewidth=0.8, label='Initial Level')

# Customize plot aesthetics
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylabel("Carbon Emissions (Million Tons)")
ax.set_title("Impact of Conservation Initiatives in Greenburg:\nA Carbon Emissions Waterfall Chart", fontsize=14, fontweight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate final emissions level
final_emissions = initial_emissions + sum(data[1:])
ax.text(len(data) - 1, final_emissions - 3, f'Final Emissions\n{final_emissions:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Ensuring layout is clear and organized
plt.tight_layout()

# Display the plot
plt.show()