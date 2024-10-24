import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors and their corresponding average monthly sales
flavors = ['Vanilla Dream', 'Choco Fudge', 'Strawberry Bliss', 'Minty Fresh', 
           'Rocky Road', 'Pistachio Paradise', 'Caramel Swirl', 'Berry Burst']
sales = np.array([120, 150, 110, 90, 130, 95, 105, 140])

# Projected sales increase in percentage for the next month
projected_percentage_increase = np.array([5, 8, 7, 6, 10, 5, 9, 7])
projected_sales = sales * (1 + projected_percentage_increase / 100)

# Colors for each flavor
colors = plt.cm.coolwarm(np.linspace(0, 1, len(flavors)))

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the bars with colors
bars = ax.bar(flavors, sales, color=colors, edgecolor='black', label='Current Sales')

# Overlay line plot for projected sales
ax.plot(flavors, projected_sales, color='darkred', marker='o', linestyle='-', 
        linewidth=2, markersize=6, label='Projected Sales')

# Annotate each bar with the sales value
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval}', ha='center', va='bottom', fontsize=10)

# Annotate each point on the line plot
for i, proj_val in enumerate(projected_sales):
    ax.text(i, proj_val + 2, f'{int(proj_val)}', ha='center', va='bottom', fontsize=10, color='darkred')

# Titles and labels
ax.set_title("Average and Projected Monthly Ice Cream Sales\nat Frosty Delights", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Flavor", fontsize=12)
ax.set_ylabel("Sales (Units)", fontsize=12)

# Adjust x-axis labels to avoid overlap
ax.set_xticks(np.arange(len(flavors)))
ax.set_xticklabels(flavors, fontsize=10, rotation=30, ha='right')

# Horizontal grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Legend to distinguish current and projected sales
ax.legend()

# Automatically adjust layout for a better fit
plt.tight_layout()

# Display the plot
plt.show()