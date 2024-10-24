import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Define stages and corresponding cash flow values
stages = [
    "Initial Investment", "R&D Expenses", "Marketing",
    "Series A Funding", "Operational Costs", "Product Sales",
    "Series B Funding", "Expansion Costs", "Net Profit"
]

# Cash flow changes for each stage
values = [500000, -150000, -80000, 300000, -120000, 250000, 400000, -200000, 300000]

# Generate gradient colors for positive and negative values
def get_gradient_color(value):
    if value >= 0:
        # Green gradient
        return plt.cm.Greens(value / max(values))
    else:
        # Red gradient
        return plt.cm.Reds(abs(value) / abs(min(values)))

colors = [get_gradient_color(value) for value in values]

# Calculate cumulative cash flow starting from zero
cumulative_cashflow = np.cumsum(values)
cumulative_cashflow = np.insert(cumulative_cashflow, 0, 0)

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Draw bars for each stage
for i in range(len(stages)):
    start = cumulative_cashflow[i]
    change = values[i]
    ax.bar(i + 1, change, bottom=start, color=colors[i], edgecolor='black')
    ax.plot([i, i + 1], [start, start], color='black', lw=1)

# Add gradient lines for zero and milestones (e.g., break-even)
ax.axhline(0, color='gray', linewidth=1.5, linestyle='--')
ax.axhline(y=cumulative_cashflow[-1], color='gray', linewidth=1.5, linestyle=':', label='Final Profit Level')

# Annotate bars with changes and arrows
for i, (value, total) in enumerate(zip(values, cumulative_cashflow[1:])):
    y_pos = total - value / 2 if value < 0 else total - value / 2
    ax.text(i + 1, y_pos, f"${value:,}", ha='center', va='center', fontsize=10, color='white' if value < 0 else 'black')
    ax.add_patch(FancyArrowPatch((i + 1, y_pos), (i + 1, y_pos + (value / 3)), 
                  arrowstyle='->', color='black'))

# Set the title and labels
ax.set_title("Tech Innovations Inc.\nInvestment & Profitability Journey", fontsize=16, fontweight='bold')
ax.set_xticks(range(1, len(stages) + 1))
ax.set_xticklabels(stages, rotation=45, ha='right', fontsize=9)
ax.set_ylabel("Cumulative Cash Flow ($)")

# Customize spines and grid
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Ensure layout is tidy
plt.tight_layout()

# Display the chart
plt.show()