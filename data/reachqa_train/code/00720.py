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

# Determine colors for the bars with a gradient palette
colors = ['#00274d']  # Initial color for starting budget
for change in changes[1:]:
    if change < 0:
        colors.append('#f25352')  # Expenses color
    else:
        colors.append('#34a853')  # Savings color

# Identify max expense and savings for highlighting
max_expense = min(changes[1:])
max_saving = max(changes[1:])
highlight_colors = ['#ff6347' if change == max_expense else '#66cdaa' if change == max_saving else color for change, color in zip(changes[1:], colors[1:])]

# Plotting the Waterfall Chart
fig, ax = plt.subplots(figsize=(14, 9))
bar_width = 0.8

# Draw bars and connecting lines
for i in range(len(changes)):
    ax.bar(i, changes[i], bottom=cumulative_budget[i-1] if i > 0 else 0, width=bar_width, color=highlight_colors[i-1] if i > 0 else colors[0])

    # Connect bars with a thin line
    if i > 0:
        ax.plot([i-1 + bar_width / 2, i - bar_width / 2], [cumulative_budget[i-1]]*2, color='gray', linewidth=2, linestyle='--')

# Annotate each bar with its resulting budget
for i, cumulative in enumerate(cumulative_budget):
    ax.text(i, cumulative, f"${cumulative:,.0f}", ha='center', va='bottom' if changes[i] >= 0 else 'top', fontweight='bold', fontsize=10)

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

# Enhance visual appeal
ax.set_facecolor('#f8f8ff')

# Legend setup
legend_elements = [
    plt.Line2D([0], [0], color='#00274d', lw=4, label='Initial Budget'),
    plt.Line2D([0], [0], color='#f25352', lw=4, label='Expenses'),
    plt.Line2D([0], [0], color='#34a853', lw=4, label='Savings'),
    plt.Line2D([0], [0], color='#ff6347', lw=4, label='Max Expense'),
    plt.Line2D([0], [0], color='#66cdaa', lw=4, label='Max Saving')
]
ax.legend(handles=legend_elements, loc='upper right', frameon=False, fontsize=10)

# Automatic adjustment to prevent overlap
plt.tight_layout()
plt.show()