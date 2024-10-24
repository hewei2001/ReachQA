import matplotlib.pyplot as plt
import numpy as np

# Data construction for waterfall chart
categories = [
    "2010 Emissions", "Industrial Growth", "Wind Power", "Solar Power",
    "Efficiency Improvements", "Industrial Practices", "2020 Emissions"
]
emissions_changes = np.array([100, 15, -25, -30, -20, -10, 30])

# Calculate cumulative positions for waterfall steps
cumulative_changes = np.cumsum(emissions_changes)
y_base = np.hstack(([0], cumulative_changes[:-1]))

# Define colors for bars
colors = ["grey"] + ["red" if x > 0 else "green" for x in emissions_changes[1:-1]] + ["grey"]

# Create waterfall plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each bar in the waterfall chart
for i in range(len(emissions_changes)):
    ax.bar(categories[i], emissions_changes[i], bottom=y_base[i], color=colors[i], edgecolor='black')

# Draw lines between bars
for i in range(1, len(emissions_changes)):
    line_x = [i-1, i]
    line_y = [cumulative_changes[i-1], cumulative_changes[i-1]]
    ax.plot(line_x, line_y, color='black', linewidth=0.7)

# Add data labels on each bar
for i, (change, y) in enumerate(zip(emissions_changes, cumulative_changes)):
    ax.text(i, y_base[i] + change/2, f'{change}', ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    if i == 0 or i == len(emissions_changes) - 1:
        ax.text(i, y, f'{y}', ha='center', va='bottom' if change >= 0 else 'top', fontsize=10, fontweight='bold', color='black')

# Overlay: Line plot for hypothetical trend
hypothetical_trend = np.linspace(100, 200, len(categories))  # Hypothetical increasing trend
ax.plot(categories, hypothetical_trend, color='blue', linestyle='--', marker='o', label='Hypothetical Growth Scenario')

# Annotations for overlay plot
for i, value in enumerate(hypothetical_trend):
    ax.text(i, value, f'{int(value)}', ha='center', va='bottom', fontsize=9, color='blue')

# Configure plot aesthetics
ax.set_title("Decade of Change:\nGreenville's Renewable Energy Impact on Carbon Emissions", fontsize=16, fontweight='bold')
ax.set_ylabel('Net Change in Carbon Emissions (MtCO2)', fontsize=12)
ax.set_xlabel('Contributing Factors', fontsize=12)
ax.axhline(0, color='black', linewidth=0.8)

# Improve x-tick appearance
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

# Add a legend to differentiate waterfall and overlay plot
ax.legend(loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()