import matplotlib.pyplot as plt
import numpy as np

# Define stages of automation and corresponding production volume changes in thousands of units
stages = ['Initial Production', 'Material Handling', 'Assembly Line', 
          'Quality Inspection', 'Packaging', 'Other Factors', 'Final Production']
production_changes = [500, 80, 120, 60, 50, -30, 780]  # Thousands of units

# Additional data for overlay line plot: hypothetical cost (in thousands of dollars)
costs = [100, 20, 30, 25, 15, 5, 70]  # Thousands of dollars

# Calculate starting and ending values for each stage
starting_values = np.zeros(len(stages))
ending_values = np.zeros(len(stages))

starting_values[0] = production_changes[0]
for i in range(1, len(production_changes)):
    ending_values[i-1] = starting_values[i-1] + production_changes[i]
    starting_values[i] = ending_values[i-1]

# Set color scheme: positive changes in blue and negative changes in red
colors = ['#6BAED6' if x >= 0 else '#F08080' for x in production_changes]

# Plotting the Waterfall Chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Draw bars with connection lines to depict progression
for i in range(len(stages)):
    ax1.bar(stages[i], production_changes[i], bottom=starting_values[i], 
           color=colors[i], edgecolor='black', linewidth=1.2)
    if i > 0:
        ax1.plot([i-1, i], [ending_values[i-1], starting_values[i]], 
                color='gray', linestyle='--', linewidth=1.5)

# Annotations for value changes and final values
for i in range(len(stages)):
    ax1.annotate(f"{production_changes[i]:+}", 
                (i, starting_values[i] + production_changes[i] / 2), 
                ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    if i < len(stages) - 1:
        ax1.annotate(f"{ending_values[i]}", 
                    (i, ending_values[i]), 
                    textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='black')

# Overlay Line Plot for Costs
ax2 = ax1.twinx()
ax2.plot(stages, costs, color='purple', marker='o', linestyle='-', linewidth=2, markersize=8, label='Cost')
ax2.set_ylabel('Cost Associated with Each Stage\n(Thousands of Dollars)', fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Add annotations for the line plot
for i, cost in enumerate(costs):
    ax2.annotate(f"{cost}", 
                 (i, cost), 
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='purple')

# Enhance visual presentation
ax1.set_title('Evolving Contribution of Automation\nin a High-Tech Factory: 2022 Overview', 
             fontsize=16, pad=20)
ax1.set_ylabel('Change in Production Volume\n(Thousands of Units)', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_axisbelow(True)

# Customize x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)

# Add legend
bars_legend = [plt.Rectangle((0,0),1,1, color=color) for color in ['#6BAED6', '#F08080']]
ax1.legend(bars_legend, ['Increase', 'Decrease'], title='Production Change', title_fontsize=12, fontsize=10, loc='upper left')
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()