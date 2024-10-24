import matplotlib.pyplot as plt

# Data Setup
initial_balance = 500000
quarterly_changes = [
    ("Initial Balance", 0),
    ("Q1 Revenue", 150000),
    ("Q1 Expenses", -50000),
    ("Q1 Investment", -20000),
    ("Q2 Revenue", 200000),
    ("Q2 Expenses", -80000),
    ("Q3 Revenue", 180000),
    ("Q3 Expenses", -100000),
    ("Q3 Investment", -30000),
    ("Q4 Revenue", 220000),
    ("Q4 Expenses", -150000),
    ("Net Income", 0)  # Placeholder for final balance
]

# Calculate cumulative balance
cumulative_balance = [initial_balance]
for label, change in quarterly_changes[1:]:
    cumulative_balance.append(cumulative_balance[-1] + change)

# Update the net income value based on the final balance
quarterly_changes[-1] = ("Net Income", cumulative_balance[-1])

# Calculate expected balance (linear projection with slight growth)
expected_growth_rate = 0.025  # 2.5% growth per quarter
expected_balance = [initial_balance]
for i in range(1, len(cumulative_balance)):
    expected_balance.append(expected_balance[-1] * (1 + expected_growth_rate))

# Determine colors for the bars
colors = ['#348ABD']  # Initial balance color
for label, change in quarterly_changes[1:-1]:
    if 'Revenue' in label:
        colors.append('#A0D568')  # Revenue increase color
    elif 'Expenses' in label:
        colors.append('#FF7979')  # Expense decrease color
    else:  # Investment
        colors.append('#F5D76E')  # Investment color
colors.append('#34A853' if cumulative_balance[-1] >= initial_balance else '#FF7979')  # Net income color

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.6

# Draw bars for waterfall chart
for i, (label, change) in enumerate(quarterly_changes):
    ax.bar(i, change if i != 0 else cumulative_balance[0], bottom=cumulative_balance[i-1] if i > 0 else 0, width=bar_width, color=colors[i])
    if i > 0:
        ax.plot([i-1 + bar_width / 2, i - bar_width / 2], [cumulative_balance[i-1]]*2, color='gray', linewidth=2, linestyle='--')

# Annotate each bar with its resulting balance
for i, cumulative in enumerate(cumulative_balance):
    ax.text(i, cumulative, f"${cumulative:,.0f}", ha='center', va='bottom' if i != 0 and quarterly_changes[i][1] >= 0 else 'top', fontweight='bold', fontsize=10)

# Overlay line plot for expected balance
ax.plot(range(len(expected_balance)), expected_balance, marker='o', linestyle='-', color='purple', linewidth=2, markersize=8, label='Expected Balance')
for i, expected in enumerate(expected_balance):
    ax.text(i, expected, f"${expected:,.0f}", ha='center', va='bottom', color='purple', fontsize=9)

# Title and labels
ax.set_title('InnovateX Annual Financial Performance\nTracking Actual and Expected Balances', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Balance (in dollars)', fontsize=12)
ax.set_xticks(range(len(quarterly_changes)))
ax.set_xticklabels([label for label, _ in quarterly_changes], rotation=45, ha='right', fontsize=10)

# Customize grid and appearance
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.set_tick_params(width=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_facecolor('#f8f8ff')

# Legend setup
legend_elements = [
    plt.Line2D([0], [0], color='#348ABD', lw=4, label='Initial Balance'),
    plt.Line2D([0], [0], color='#A0D568', lw=4, label='Revenue Increase'),
    plt.Line2D([0], [0], color='#FF7979', lw=4, label='Expense Decrease'),
    plt.Line2D([0], [0], color='#F5D76E', lw=4, label='Investment'),
    plt.Line2D([0], [0], color='#34A853', lw=4, label='Net Income Increase'),
    plt.Line2D([0], [0], color='purple', lw=2, marker='o', label='Expected Balance')
]
ax.legend(handles=legend_elements, loc='upper left', frameon=False, fontsize=10)

# Automatic adjustment to prevent overlap
plt.tight_layout()
plt.show()