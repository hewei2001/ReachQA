import matplotlib.pyplot as plt
import numpy as np

# Initial carbon emissions in million tons
initial_emissions = 100

# Extended impacts of initiatives on emissions in million tons
data = [
    initial_emissions,  # Initial emissions
    -15,  # Reduction from renewable energy
    -10,  # Reduction from public transport
    -8,   # Reduction from waste management
    -12,  # Reduction from tree planting
    -5,   # Other reductions
    -7,   # Energy efficiency
    -6,   # Water conservation
    -9,   # Agricultural practices
    -4,   # Eco-friendly technologies
    -3    # Community initiatives
]

# Labels for the chart steps
labels = [
    "Initial Emissions",
    "Renewable Energy",
    "Public Transport",
    "Waste Reduction",
    "Tree Planting",
    "Miscellaneous",
    "Energy Efficiency",
    "Water Conservation",
    "Agricultural Practices",
    "Eco-friendly Tech",
    "Community Initiatives"
]

# Calculating cumulative impacts
steps = np.zeros(len(data) + 1)
steps[1:] = np.cumsum(data)

# Color coding: Initial in blue, reductions in different shades of green
bar_color = ['#1f77b4'] + ['#2ca02c' if x < 0 else '#d62728' for x in data[1:]]

# Calculate percentage reductions from initial emissions
percentage_reductions = [(x / initial_emissions) * 100 for x in data[1:]]

# Creating the waterfall chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars and connect with lines
for i, (val, step, label, color) in enumerate(zip(data, steps, labels, bar_color)):
    ax.bar(i, val, bottom=step, color=color, edgecolor='gray', width=0.6)
    ax.text(i, step + val/2, f'{abs(val):.1f}\n({abs(percentage_reductions[i-1]):.1f}%)' if i > 0 else f'{abs(val):.1f}', 
            ha='center', va='center', color='white')
    if i > 0:
        ax.plot([i-1, i], [steps[i], steps[i]], color='black', linestyle='-', linewidth=0.8)

# Adding a horizontal line indicating the initial emissions level
ax.plot([-0.5, len(data)-0.5], [initial_emissions, initial_emissions], 'k--', linewidth=0.8, label='Initial Level')

# Customize plot aesthetics
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylabel("Carbon Emissions (Million Tons)")
ax.set_title("Impact of Conservation Initiatives in Greenburg:\nA Complex Carbon Emissions Waterfall Chart", 
             fontsize=14, fontweight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate final emissions level
final_emissions = initial_emissions + sum(data[1:])
ax.text(len(data) - 1, final_emissions - 5, f'Final Emissions\n{final_emissions:.1f}', ha='center', va='bottom', 
        fontsize=10, fontweight='bold', color='black')

# Secondary y-axis for cost savings or additional metrics
ax2 = ax.twinx()
# Example data for cost savings (in million USD)
cost_savings = np.array([0, 30, 25, 18, 22, 10, 20, 15, 28, 12, 8])
ax2.plot(range(len(data)), cost_savings.cumsum(), color='orange', linestyle='--', linewidth=2, label='Cumulative Cost Savings')
ax2.set_ylabel('Cumulative Cost Savings (Million USD)')
ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.9), fontsize=10)

# Adjust layout for clarity
plt.tight_layout()
plt.show()