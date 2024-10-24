import matplotlib.pyplot as plt
import numpy as np

# Define the categories and corresponding profit changes
categories = [
    "Beginning Balance", "Sales Growth", "Cost Reductions",
    "New Store Investments", "Marketing Expenses", "Year-end Net Profit"
]

# Profit changes for each category in millions
profit_changes = [2.0, 1.5, 0.5, -0.8, -0.3]
# Calculating the total for the final category
profit_changes.append(sum(profit_changes))

# Cumulative sums for positions of each bar in the waterfall chart
cumulative_profit = np.cumsum(profit_changes)

# Additional related dataset for line chart
quarters = ["Q1", "Q2", "Q3", "Q4"]
quarterly_revenue = [1.8, 2.5, 3.0, 2.7]  # Revenue in millions for each quarter

# Initialize the plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Waterfall Chart
colors = ['#1f77b4', '#2ca02c', '#2ca02c', '#d62728', '#d62728', '#9467bd']
bars = ax1.bar(categories, cumulative_profit, color=colors, width=0.4, edgecolor='gray')

for i in range(1, len(cumulative_profit)):
    ax1.plot(
        [i - 0.5, i - 0.5],
        [cumulative_profit[i - 1], cumulative_profit[i]],
        color='gray',
        linestyle='--',
        linewidth=1
    )

for bar in bars:
    yval = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width()/2,
        yval,
        f'${yval:.2f}M',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

ax1.set_title('Retail Success Ladder:\nProfit Increments of a Boutique Chain', fontsize=14, fontweight='bold')
ax1.set_ylabel('Profit in Millions ($)', fontsize=12)
ax1.set_xlabel('Categories', fontsize=12)
ax1.set_xticklabels(categories, rotation=30, ha='right')

# Line Chart
ax2.plot(quarters, quarterly_revenue, marker='o', color='#ff7f0e', linestyle='-', linewidth=2, label='Revenue')
ax2.fill_between(quarters, quarterly_revenue, color='#ff7f0e', alpha=0.2)

for i, value in enumerate(quarterly_revenue):
    ax2.text(quarters[i], value + 0.05, f'{value:.1f}M', ha='center', va='bottom', fontsize=10)

ax2.set_title('Quarterly Revenue Trend\nfor the Financial Year', fontsize=14, fontweight='bold')
ax2.set_ylabel('Revenue in Millions ($)', fontsize=12)
ax2.set_xlabel('Quarters', fontsize=12)
ax2.set_xticks(quarters)
ax2.legend(loc='upper left')

# Automatic adjustment of subplot parameters
plt.tight_layout()

# Display the charts
plt.show()