import matplotlib.pyplot as plt
import numpy as np

# Define the data
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
revenue_changes = [100, -20, 15, -30, 50, 0, 20, -15, -50, 30, 0, 40]
initial_revenue = 50  # Starting point (in million dollars)

# Calculate the values needed for the waterfall chart
total_revenue = initial_revenue
revenue_values = [initial_revenue]

for change in revenue_changes:
    total_revenue += change
    revenue_values.append(total_revenue)

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 9))

# Define colors with gradients based on value
colors = ['green' if x >= 0 else 'red' for x in revenue_changes]
edge_colors = ['darkgreen' if x >= 0 else 'darkred' for x in revenue_changes]

# Plotting the waterfall chart
bars = ax.bar(months, revenue_changes, bottom=revenue_values[:-1],
              color=colors, edgecolor=edge_colors, linewidth=1.5)

# Apply a unique style for the total bar
bars[-1].set_color('mediumblue')
bars[-1].set_edgecolor('navy')
bars[-1].set_label('Total Revenue')

# Enhanced annotations
for i, (bar, change) in enumerate(zip(bars, revenue_changes)):
    yval = bar.get_height()
    label_position = yval + revenue_values[i] if change >= 0 else revenue_values[i]
    ax.text(bar.get_x() + bar.get_width() / 2, label_position,
            f'{change:+}\n({revenue_values[i+1]:.0f}M)', ha='center',
            va='bottom' if change < 0 else 'top', fontsize=9, color='darkblue')

# Draw a marker for the total revenue at the end
ax.plot([months[-1]], [revenue_values[-1]], 'bD')
ax.annotate(f'Total: {revenue_values[-1]:.0f}M', xy=(11, revenue_values[-1]),
            xytext=(11.5, revenue_values[-1] * 1.05),
            arrowprops=dict(arrowstyle='->', lw=1, color='blue'), fontsize=10)

# Additional elements
cumulative_line = ax.plot(months, revenue_values[1:], 'o-', color='gray', label='Cumulative Revenue')
ax.fill_between(months, revenue_values[1:], color='gray', alpha=0.1)

# Add thematic elements and grid
ax.set_title("Blockbuster Box Office: A Year in Review\n'Epic Adventure' 2023", fontsize=16, weight='bold', loc='center')
ax.set_ylabel('Revenue Change (in million $)', fontsize=12)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylim(min(revenue_values) * 0.95, max(revenue_values) * 1.15)
ax.axhline(0, color='black', linewidth=0.8)

# Customize the grid and labels
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(loc='upper left')

# Display the plot
plt.show()