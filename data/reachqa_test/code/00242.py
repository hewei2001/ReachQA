import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Define activities and their respective energy consumption changes
activities = [
    'Base Load', 'Morning Appliances', 'Heating/Cooling', 'Lighting', 
    'Entertainment', 'Cooking', 'EV Charging', 'Solar Generation'
]
energy_changes = [5, 2, 3, 1, 2, 4, 10, -6]

# Calculate cumulative energy starting from zero
start_value = 0
cumulative_energy = [start_value]
for change in energy_changes:
    cumulative_energy.append(cumulative_energy[-1] + change)

# Define a more nuanced color palette
colors = ['#88c999' if x >= 0 else '#ff6b6b' for x in energy_changes]

# Plotting the waterfall chart
fig, ax = plt.subplots(figsize=(14, 8))

# Draw bars with a gradient effect using hatch patterns
hatches = ['/', '\\', 'x', '+', '.', '*', 'o', '-']

for i, (activity, change, color) in enumerate(zip(activities, energy_changes, colors)):
    ax.bar(i, change, bottom=cumulative_energy[i], color=color, edgecolor='black', linewidth=0.8, hatch=hatches[i % len(hatches)])
    # Annotation for both value and percentage change
    percentage = (change / cumulative_energy[-1]) * 100
    ax.text(i, cumulative_energy[i] + change/2, f'{change:+} kWh\n({percentage:.1f}%)', ha='center', va='center', 
            color='black', fontweight='bold', fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# Connectors with custom markers
for i in range(1, len(cumulative_energy) - 1):
    connector = FancyArrowPatch((i-1, cumulative_energy[i]), (i, cumulative_energy[i]), 
                                arrowstyle='-|>', color='gray', linewidth=0.5, mutation_scale=10)
    ax.add_patch(connector)

# Final dashed line to the final total
ax.plot([0, len(energy_changes) - 1], [cumulative_energy[-1], cumulative_energy[-1]], "k--", linewidth=0.8)

# Customizing the plot
ax.set_xticks(range(len(activities)))
ax.set_xticklabels(activities, rotation=45, ha='right', fontsize=10)
ax.set_ylabel('Energy Consumption (kWh)', fontsize=14)
ax.set_title('Energy Consumption Waterfall in a Smart Home\nVisualizing Daily Energy Flow', fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Background gradient
ax.set_facecolor('#f7f7f7')

# Legend indicating the type of activity
legend_elements = [
    plt.Line2D([0], [0], color='#88c999', lw=4, label='Positive Change'),
    plt.Line2D([0], [0], color='#ff6b6b', lw=4, label='Negative Change')
]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1), title='Change Type', frameon=False)

# Ensure layout fits
plt.tight_layout()

# Display plot
plt.show()