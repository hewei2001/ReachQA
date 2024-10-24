import matplotlib.pyplot as plt
import numpy as np

# Define the data for the waterfall chart
emissions_labels = [
    'Initial Emissions', 'Industrial Growth', 'Increased Vehicle Use',
    'Renewable Energy Adoption', 'Tree Planting', 'Energy Efficiency Programs',
    'Final Emissions'
]
emissions_values = [1000, 300, 150, -200, -100, -150]
final_emission = 1000 + sum(emissions_values)

# Include the final emission in the data for plotting
emissions_values.append(final_emission - 1000)

# Calculate the positions on the y-axis for each step
emissions_start = np.zeros(len(emissions_values))
emissions_start[1:] = np.cumsum(emissions_values[:-1])

# Define colors for positive and negative contributions
colors = ['#6da34d' if x >= 0 else '#e06c75' for x in emissions_values]

# Create the waterfall chart
fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(emissions_labels, emissions_values, bottom=emissions_start, color=colors, edgecolor='black')

# Add a connecting line between bars to emphasize the flow
for i in range(1, len(emissions_values)):
    ax.plot([i - 1, i], [emissions_start[i], emissions_start[i]], color='black', linestyle='-', linewidth=0.5)

# Enhance the plot with labels and titles
ax.set_title('Annual Carbon Emissions in EcoVille\nImpact of Activities and Initiatives', fontsize=16, pad=20)
ax.set_ylabel('Carbon Emissions (Metric Tons)', fontsize=12)
ax.set_xlabel('Emission Activities and Reductions', fontsize=12)

# Add values on top of each bar
for i, (bar, value) in enumerate(zip(bars, emissions_values)):
    yval = bar.get_height() + emissions_start[i]
    ax.text(bar.get_x() + bar.get_width() / 2, yval + (10 if value >= 0 else -15), f'{yval:.0f}', 
            ha='center', va='bottom' if value >= 0 else 'top', color='black', fontsize=10, weight='bold')

# Adjust x-tick labels to prevent overlapping
plt.xticks(rotation=30, ha='right', fontsize=10)

# Grid and layout adjustments
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()