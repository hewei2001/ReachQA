import matplotlib.pyplot as plt
import numpy as np

# Define more quarters and comprehensive data
quarters = [f'Year {y} Q{q}' for y in range(1, 4) for q in range(1, 5)] + ['Year 4 Q1', 'Year 4 Q2']
values_revenue = [500, 200, -150, 300, 250, -200, 400, -100, 500, -50, 600, -300, 700, -150]
values_expenses = [300, 100, 100, 150, 200, 150, 250, 100, 300, 50, 300, 100, 350, 100]
net_values = np.array(values_revenue) - np.array(values_expenses)

# Colors based on net values
colors = ['green' if v >= 0 else 'red' for v in net_values]

# Cumulative balances
cumulative_net = np.cumsum(net_values)

# Define figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot revenue and expenses in the background for comparison
ax.bar(quarters, values_revenue, color='lightgreen', label='Revenue', alpha=0.5, edgecolor='grey')
ax.bar(quarters, values_expenses, color='lightcoral', label='Expenses', alpha=0.5, edgecolor='grey')

# Plot net changes with connection lines
ax.bar(quarters, net_values, color=colors, edgecolor='grey', linewidth=0.8, label='Net Change')
ax.plot(quarters, cumulative_net, color='blue', marker='o', linestyle='--', linewidth=2, label='Cumulative Net')

# Adding text annotations for net change and cumulative balance
for i in range(len(net_values)):
    y_offset = net_values[i] / 2
    ax.text(i, y_offset, f'{net_values[i]}', ha='center', va='center', color='white', fontweight='bold', fontsize=9)
    ax.text(i, cumulative_net[i], f'{cumulative_net[i]}', va='bottom' if net_values[i] > 0 else 'top', ha='center', fontsize=9, color='blue')

# Customizing the chart
ax.set_title('Financial Performance Analysis of Tech Startup\nRevenue, Expenses, and Net Balance Over Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Financial Balance ($k)', fontsize=12)
ax.set_ylim(min(min(cumulative_net)-100, min(values_expenses))-50, max(max(cumulative_net)+100, max(values_revenue))+100)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add legend
ax.legend(loc='upper left')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()