import matplotlib.pyplot as plt
import numpy as np

# Monthly labels
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Data for coffee types (in thousands)
espresso = np.array([20, 25, 23, 30, 33, 35, 40, 42, 38, 36, 31, 29])
latte = np.array([15, 18, 17, 25, 28, 30, 32, 35, 34, 33, 28, 26])
cappuccino = np.array([10, 13, 12, 18, 20, 22, 25, 27, 26, 25, 22, 20])

# Calculate total sales for each month
total_sales = espresso + latte + cappuccino

# Calculate quarterly sales
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
quarter_sales = [
    np.sum(total_sales[0:3]),  # Q1
    np.sum(total_sales[3:6]),  # Q2
    np.sum(total_sales[6:9]),  # Q3
    np.sum(total_sales[9:12])  # Q4
]

# Set up subplot configuration
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot - Stacked Area Chart
ax1.stackplot(
    months, espresso, latte, cappuccino,
    labels=['Espresso', 'Latte', 'Cappuccino'],
    colors=['#8B4513', '#DEB887', '#D2B48C'],
    alpha=0.8
)
ax1.set_title('Monthly Coffee Sales Trends\nin 2023', fontsize=14, fontweight='bold', pad=10)
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Cups Sold (in thousands)', fontsize=12)
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Second subplot - Bar Chart for Quarterly Sales
ax2.bar(quarters, quarter_sales, color=['#A0522D', '#DAA520', '#CD853F', '#F4A460'])
ax2.set_title('Quarterly Coffee Sales Totals\nin 2023', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Quarters', fontsize=12)
ax2.set_ylabel('Total Cups Sold (in thousands)', fontsize=12)
ax2.set_ylim(0, max(quarter_sales) + 20)
for i, v in enumerate(quarter_sales):
    ax2.text(i, v + 2, str(v), ha='center', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()