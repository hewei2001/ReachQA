import matplotlib.pyplot as plt
import numpy as np

# Data for the waterfall chart
funding_received = 500000
expenses_investments = {
    "Staff Salaries": -200000,
    "Books and Media Acquisition": -100000,
    "Maintenance and Utilities": -50000,
    "Community Programs & Workshops": -25000,
    "Technological Upgrades": -75000,
    "Misc. Operational Costs": -20000
}
ending_balance = funding_received + sum(expenses_investments.values())

# Data preparation
categories = ["Funding Received"] + list(expenses_investments.keys()) + ["Ending Balance"]
values = [funding_received] + list(expenses_investments.values()) + [ending_balance]
cumulative = np.cumsum([0] + values[:-1])

# Set up color coding
colors = ['green' if value >= 0 else 'red' for value in values]
colors[0] = 'blue'  # Starting value
colors[-1] = 'purple'  # Ending balance to stand out

# Plot
fig, ax = plt.subplots(figsize=(12, 7))

# Bars
bars = ax.bar(categories, values, bottom=cumulative, color=colors, edgecolor='gray')

# Add connecting lines to show progression
for i in range(1, len(values)):
    line_y = cumulative[i-1] + values[i-1]
    ax.plot([i-0.5, i-0.5], [line_y, cumulative[i]], color='black', linewidth=1.5, linestyle='--')

# Add text annotations for each bar
for bar, value, cumsum in zip(bars, values, cumulative):
    height = bar.get_height()
    ax.annotate(f'{value:+,}\n[{cumsum:,}]', xy=(bar.get_x() + bar.get_width() / 2, cumsum + height / 2),
                xytext=(0, 5), textcoords="offset points", ha='center', va='center', color='white', weight='bold')

# Setting labels and title
ax.set_xlabel('Budget Items', fontsize=12, weight='bold')
ax.set_ylabel('Amount in $', fontsize=12, weight='bold')
ax.set_title('Fiscal Dynamics of a Local Library\'s\nAnnual Budget Allocation', fontsize=14, weight='bold', pad=20)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure a tidy layout
plt.tight_layout()

# Display the plot
plt.show()