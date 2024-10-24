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

# Cumulative sums to determine the positions for each bar
cumulative_profit = np.cumsum(profit_changes)

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Color settings for each bar
colors = ['#1f77b4', '#2ca02c', '#2ca02c', '#d62728', '#d62728', '#9467bd']

# Create bars for the waterfall chart
bars = ax.bar(categories, cumulative_profit, color=colors, width=0.4, edgecolor='gray')

# Connect bars with lines to show the progression
for i in range(1, len(cumulative_profit)):
    ax.plot(
        [i - 0.5, i - 0.5],
        [cumulative_profit[i - 1], cumulative_profit[i]],
        color='gray',
        linestyle='--',
        linewidth=1
    )

# Annotate the bars with their respective values
for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        yval,
        f'${yval:.2f}M',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# Add chart title and axis labels
ax.set_title(
    'Retail Success Ladder:\nProfit Increments of a Boutique Chain',
    fontsize=16, fontweight='bold'
)
ax.set_ylabel('Profit in Millions ($)', fontsize=12)
ax.set_xlabel('Categories', fontsize=12)

# Adjust x-ticks for better readability
plt.xticks(rotation=30, ha='right')

# Automatic adjustment of subplot parameters for better layout
plt.tight_layout()

# Display the chart
plt.show()