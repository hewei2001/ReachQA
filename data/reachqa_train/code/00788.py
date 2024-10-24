import matplotlib.pyplot as plt
import numpy as np

# Data definition
categories = ['Initial Budget', 'Campaign Success', 'Unexpected Costs', 'Reallocations',
              'Efficiency Savings', 'New Initiatives', 'Year-End Adjustment', 'Final Budget']
budget_changes = [1000000, 200000, -150000, -100000, 50000, -200000, 100000]

# Cumulative budget calculation for plotting
cumulative = np.cumsum(budget_changes)
cumulative_with_start = np.insert(cumulative, 0, 0)

# Color coding based on budget changes
colors = ['blue'] + ['green' if x >= 0 else 'red' for x in budget_changes]

# New data for the additional subplot (e.g., cumulative monthly changes)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
monthly_cumulative = [0, 150000, 180000, 170000, 210000, 190000, 150000, 250000]

# Plot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot the original waterfall chart
bars = ax1.bar(categories, np.append(budget_changes, cumulative[-1]), 
               color=colors, edgecolor='black', linewidth=0.7)

for i in range(1, len(bars)):
    ax1.plot([i-1, i], [cumulative_with_start[i], cumulative_with_start[i]], 
             color='black', linestyle='-', linewidth=1)

for i, bar in enumerate(bars):
    if i < len(budget_changes):
        yval = budget_changes[i]
    else:
        yval = cumulative[-1]
    ax1.text(bar.get_x() + bar.get_width() / 2, cumulative_with_start[i] + yval/2, 
             f"${yval:,.0f}", ha='center', va='center', color='white' if yval < 0 else 'black', weight='bold')

ax1.set_title('Annual Marketing Campaign Budget Impact\nA Waterfall Analysis', fontsize=16, fontweight='bold')
ax1.set_ylabel('Budget Impact (USD)', fontsize=12)
ax1.set_xlabel('Budget Categories', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)
plt.sca(ax1)
plt.xticks(rotation=45, ha='right')
ax1.set_axisbelow(True)
ax1.axhline(0, color='black', linewidth=0.8)

# Plot the new subplot - line chart for monthly cumulative changes
ax2.plot(months, monthly_cumulative, marker='o', color='purple', linestyle='-', linewidth=2)
ax2.fill_between(months, monthly_cumulative, color='purple', alpha=0.1)
for i, month in enumerate(months):
    ax2.text(month, monthly_cumulative[i] + 10000, f"${monthly_cumulative[i]:,.0f}", ha='center', va='bottom', color='black')

ax2.set_title('Cumulative Budget Over Time\nMonthly Breakdown', fontsize=16, fontweight='bold')
ax2.set_ylabel('Cumulative Budget (USD)', fontsize=12)
ax2.set_xlabel('Month', fontsize=12)
ax2.yaxis.grid(True, linestyle='--', alpha=0.6)
ax2.set_axisbelow(True)
ax2.axhline(0, color='black', linewidth=0.8)

# Layout adjustments
plt.tight_layout()

# Display the plot
plt.show()