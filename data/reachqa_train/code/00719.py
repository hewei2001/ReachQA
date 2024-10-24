import matplotlib.pyplot as plt
import numpy as np

# Data Setup
initial_budget = 20000
regions = ["Initial Budget", "North America", "South America", "Europe", "Africa", "Asia", "Oceania", "End of Trip Savings"]
changes = [0, -2500, -1800, -3200, -1000, -2800, -1500, 1000]

# Calculate cumulative budget after each step
cumulative_budget = [initial_budget]
for change in changes[1:]:
    cumulative_budget.append(cumulative_budget[-1] + change)

# Determine colors for the bars
colors = ['#4287f5'] + ['#d9534f' if change < 0 else '#5cb85c' for change in changes[1:]]

# Plotting the Waterfall Chart
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.8

# Draw bars and connecting lines
for i in range(len(changes)):
    ax.bar(i, changes[i], bottom=cumulative_budget[i-1] if i > 0 else 0, width=bar_width, color=colors[i])

    # Connect bars with a thin line
    if i > 0:
        ax.plot([i-1 + bar_width / 2, i - bar_width / 2], [cumulative_budget[i-1]]*2, color='gray', linewidth=2)

# Annotate each bar with its resulting budget
for i, cumulative in enumerate(cumulative_budget):
    ax.text(i, cumulative, f"${cumulative:,.0f}", ha='center', va='bottom' if changes[i] >= 0 else 'top', fontweight='bold')

# Title and labels
ax.set_title('The Financial Journey of a Global Expedition:\nTracking Expenses and Savings', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Budget (in dollars)', fontsize=12)
ax.set_xticks(range(len(regions)))
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)

# Customize the grid and appearance
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.set_tick_params(width=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend setup
legend_elements = [plt.Line2D([0], [0], color='#4287f5', lw=4, label='Initial Budget'),
                   plt.Line2D([0], [0], color='#d9534f', lw=4, label='Expenses'),
                   plt.Line2D([0], [0], color='#5cb85c', lw=4, label='Savings')]
ax.legend(handles=legend_elements, loc='upper right', frameon=False, fontsize=10)

# Automatic adjustment to prevent overlap
plt.tight_layout()
plt.show()