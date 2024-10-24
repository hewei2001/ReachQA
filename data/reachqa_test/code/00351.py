import matplotlib.pyplot as plt
import numpy as np

# Expanded categories of student expenditures
categories = [
    'Housing', 'Food: Groceries', 'Food: Dining Out', 'Transportation',
    'Entertainment', 'Utilities', 'Health', 'Education', 'Savings',
    'Clothing', 'Insurance', 'Miscellaneous'
]

# Corresponding expenditures for each category in USD
expenses = [800, 150, 100, 150, 100, 200, 75, 120, 50, 60, 30, 40]

# Sub-categories for 'Food'
food_sub_categories = ['Groceries', 'Dining Out']
food_expenses = [150, 100]

# Define colors for each category for better visual separation
colors = [
    '#FF9999', '#66B3FF', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700',
    '#FF6F61', '#B6B6B4', '#6A5ACD', '#8B0000', '#4682B4', '#7FFFD4'
]

# Calculate percentages
total_expense = sum(expenses)
percentages = [(expense / total_expense) * 100 for expense in expenses]

# Create a figure with a secondary y-axis
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plotting the horizontal stacked bar chart
bars = ax1.barh(categories, expenses, color=colors, edgecolor='black', height=0.5)

# Plot the percentages on the secondary x-axis
ax2 = ax1.twiny()
ax2.set_xlim(0, total_expense)
ax2.set_xticks(np.arange(0, total_expense, 100))
ax2.set_xlabel('Percentage of Total Expenditure (%)', fontsize=12)

# Title and labels
ax1.set_title('Average Monthly Expenditure for University Students\nUrban University Town',
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Expenditure (USD)', fontsize=12)
ax1.set_ylabel('Categories', fontsize=12)

# Annotate bars with expenditure amounts and percentages
for bar, pct in zip(bars, percentages):
    ax1.text(bar.get_width() + 10, bar.get_y() + bar.get_height() / 2,
             f'${bar.get_width():.0f} ({pct:.1f}%)', va='center', fontsize=10)

# Error bars simulating variability in expenditures
np.random.seed(0)
error = np.random.normal(10, 5, size=len(expenses))
ax1.errorbar(expenses, range(len(expenses)), xerr=error, fmt='o', color='black', capsize=3)

# Customize y-ticks and alignment
ax1.set_yticks(range(len(categories)))
ax1.set_yticklabels(categories, fontsize=11)
ax1.tick_params(axis='y', which='both', length=0)

# Add grid lines for easy value estimation
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust the layout
fig.tight_layout()

# Display the plot
plt.show()