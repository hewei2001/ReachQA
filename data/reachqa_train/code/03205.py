import matplotlib.pyplot as plt
import numpy as np

# Define the phases and their corresponding costs
phases = [
    "Initial Budget",
    "Material Cost Hike",
    "Labor Wage Increase",
    "Design Change Costs",
    "Env. Compliance",
    "Delay Penalties",
    "Final Cost"
]

# Define the cost changes (in million dollars)
cost_changes = np.array([120, 20, 15, 12, 7, 10, 0])  # Last value is zero for final tally
base_values = np.zeros_like(cost_changes)

# Initialize the first base value
base_values[0] = cost_changes[0]

# Calculate base values and bar heights for each phase
for i in range(1, len(cost_changes)):
    base_values[i] = base_values[i-1] + cost_changes[i-1]

# Calculate the adjustments for each phase
adjustments = base_values + cost_changes

# Create the waterfall plot
fig, ax = plt.subplots(figsize=(14, 8))

# Loop through the cost changes and create bars with color coding
colors = ['green' if cost > 0 else 'red' for cost in cost_changes[:-1]]
colors.append('blue')  # Final cost color

for i in range(len(phases) - 1):
    ax.bar(phases[i], cost_changes[i], bottom=base_values[i], 
           color=colors[i], edgecolor='black')
    ax.plot([i-0.4, i+0.4], [base_values[i] + cost_changes[i]]*2, color='grey', linewidth=0.7)
    ax.text(i, adjustments[i] + 2, f"${adjustments[i]}M", ha='center', va='bottom', color='black')

# Draw the final adjusted cost as a separate bar
ax.bar(phases[-1], adjustments[-1], color=colors[-1], edgecolor='black')
ax.text(len(phases) - 1, adjustments[-1] + 2, f"${adjustments[-1]}M", ha='center', va='bottom', color='black')

# Title and labels
ax.set_title('The Architectural Journey: \nBuilding Costs Over Time for "The Pinnacle Tower"', fontsize=16, fontweight='bold')
ax.set_ylabel('Cost in Million USD', fontsize=12)
ax.set_xticks(range(len(phases)))
ax.set_xticklabels(phases, rotation=45, ha='right', fontsize=10)

# Add horizontal grid lines and finalize the layout
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()