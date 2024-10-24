import matplotlib.pyplot as plt
import numpy as np

# Water resource management data for Martian Colony X
labels = ["Initial Reserves", "Ice Extraction", "Recycling", "Resident Usage", "Agriculture", "Industry", "Ending Balance"]
values = [500, 200, 150, -180, -100, -120, 50]  # Added an Ending Balance value

# Calculate cumulative sum to get the positions for waterfall chart
cumulative_values = np.cumsum(values)
step = np.arange(len(values))

# Color coding for the bars
colors = ["#4CAF50" if x >= 0 else "#FF5722" for x in values]  # Green for inflow, red for outflow
colors[0] = "#2196F3"  # Blue for initial reserves
colors[-1] = "#9C27B0"  # Purple for ending balance

# Plot the waterfall chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(step, cumulative_values, width=0.6, color=colors, edgecolor='black')

# Connect each bar with lines to show progression
for i in range(1, len(cumulative_values)):
    ax.plot([step[i - 1], step[i]], [cumulative_values[i - 1], cumulative_values[i]], color='black', linestyle='--', linewidth=0.8)

# Add data labels on bars
for i, (label, value) in enumerate(zip(labels, cumulative_values)):
    ax.text(i, value + (20 if value >= 0 else -25), f'{value}', ha='center', va='bottom' if value >= 0 else 'top', color='black', fontweight='bold')

# Customize the plot
ax.set_title("Monthly Water Resource Management\nin Martian Colony X", fontsize=16, weight='bold')
ax.set_ylabel("Water Reserves (thousand liters)", fontsize=12)
ax.set_xticks(step)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Legend for inflow and outflow
legend_labels = ['Inflow', 'Outflow', 'Initial Reserves', 'Ending Balance']
legend_colors = ['#4CAF50', '#FF5722', '#2196F3', '#9C27B0']
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in legend_colors]
ax.legend(handles, legend_labels, loc='upper right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()