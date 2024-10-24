import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors and their corresponding average monthly sales
flavors = ['Vanilla Dream', 'Choco Fudge', 'Strawberry Bliss', 'Minty Fresh', 'Rocky Road', 'Pistachio Paradise', 'Caramel Swirl', 'Berry Burst']
sales = np.array([120, 150, 110, 90, 130, 95, 105, 140])  # Sales in units

# Colors for each flavor
colors = plt.cm.coolwarm(np.linspace(0, 1, len(flavors)))

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bars with colors
bars = ax.bar(flavors, sales, color=colors, edgecolor='black')

# Annotate each bar with the sales value
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval}', ha='center', va='bottom', fontsize=10)

# Title and labels
ax.set_title("Average Monthly Ice Cream Sales\nat Frosty Delights", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Flavor", fontsize=12)
ax.set_ylabel("Sales (Units)", fontsize=12)

# Adjust x-axis labels to avoid overlap
ax.set_xticks(np.arange(len(flavors)))
ax.set_xticklabels(flavors, fontsize=10, rotation=30, ha='right')

# Horizontal grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout for a better fit
plt.tight_layout()

# Display the plot
plt.show()