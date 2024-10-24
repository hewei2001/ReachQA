import matplotlib.pyplot as plt
import numpy as np

# Define the initial balance and quarter-specific financial changes
initial_balance = 200  # in thousands USD
changes = [50, -20, 70, -30, 100, -50, 80, -40]  # each in thousands USD

# Labels for each change
labels = ['Q1 Sales', 'Q1 Marketing', 'Q2 Sales', 'Q2 Ops', 
          'Q3 Launch', 'Q3 Costs', 'Q4 Sales', 'Q4 Expenses']

# Calculate cumulative values to use for positioning the bars
cumulative = np.array([initial_balance] + list(np.cumsum(changes) + initial_balance))

# Calculate the step points for the waterfall
step_points = np.arange(len(labels) + 1)

# Set colors for gains (positive) and losses (negative)
colors = ['green' if x >= 0 else 'red' for x in changes]

# Plotting the waterfall chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(step_points[1:], changes, width=0.5, bottom=cumulative[:-1], color=colors, edgecolor='black')
ax.bar(step_points[0], initial_balance, width=0.5, color='blue', edgecolor='black')  # Initial balance

# Connecting lines between bars
for i in range(len(cumulative) - 1):
    ax.plot([step_points[i+1], step_points[i+1]], [cumulative[i], cumulative[i+1]], color='black', linewidth=0.5)

# Set labels and title
ax.set_xticks(step_points)
ax.set_xticklabels(['Start'] + labels, rotation=45, ha='right')
ax.set_title('Financial Journey of TechTrend Innovations\nin 2023', fontsize=14, fontweight='bold')
ax.set_ylabel('Profit/Loss (in thousands USD)', fontsize=12)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Annotate each bar with the value change
for i, change in enumerate(changes):
    ax.annotate(f'{change:+}', xy=(step_points[i+1], cumulative[i] + change/2), 
                xytext=(0, 10), textcoords='offset points', ha='center', color='black')

# Adjust layout to prevent overlap and display the plot
plt.tight_layout()
plt.show()