import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define financial events with contextual data
labels = [
    "Initial Capital", 
    "Revenue from Bestsellers", 
    "New Author Advances", 
    "Marketing Campaigns", 
    "Operational Costs", 
    "Ending Balance"
]
values = [800, 500, -150, -120, -180, 850]  # Financial movements (in thousand gold coins)

# Calculate cumulative values for the waterfall chart
cumulative_values = np.cumsum(values)
step = np.arange(len(values))

# Define colors for bars
colors = ["#3498DB" if x >= 0 else "#E74C3C" for x in values]
colors[0] = "#2980B9"  # Darker blue for initial capital
colors[-1] = "#8E44AD"  # Purple for ending balance

# Plot the waterfall chart
fig, ax = plt.subplots(figsize=(12, 7))
bar_container = ax.bar(step, cumulative_values, width=0.6, color=colors, edgecolor='black', alpha=0.9)

# Connect bars with arrows to show progression
for i in range(1, len(cumulative_values)):
    ax.annotate(
        '', xy=(step[i], cumulative_values[i]), xytext=(step[i - 1], cumulative_values[i - 1]),
        arrowprops=dict(arrowstyle='->', color='black', lw=1.5)
    )

# Add labels above bars and percentage change
for i, (label, value) in enumerate(zip(labels, cumulative_values)):
    ax.text(
        i, value + (20 if value >= 0 else -25), 
        f'{value}K\n({(values[i] / abs(values[0]) * 100):+.1f}%)' if i > 0 else f'{value}K',
        ha='center', va='bottom' if value >= 0 else 'top', color='black', fontweight='bold'
    )

# Set titles and labels
ax.set_title(
    "Yearly Financial Performance of\nQuill & Tome Publishing", 
    fontsize=16, fontweight='bold', pad=20, multialignment='center'
)
ax.set_ylabel("Net Capital (in thousand gold coins)", fontsize=12)
ax.set_xticks(step)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add legend with icons matching bar styles
legend_labels = ['Gains', 'Losses', 'Initial Capital', 'Ending Balance']
legend_colors = ['#3498DB', '#E74C3C', '#2980B9', '#8E44AD']
handles = [mpatches.Patch(color=color) for color in legend_colors]
ax.legend(handles, legend_labels, loc='upper left', frameon=False, fontsize=10)

# Enhance presentation with layout adjustments
plt.tight_layout()

# Show the plot
plt.show()