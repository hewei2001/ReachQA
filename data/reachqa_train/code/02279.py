import matplotlib.pyplot as plt
import numpy as np

# Data for the waterfall chart
events = [
    'Initial Investment', 
    'Q1 Product Launch', 
    'Q1 Revenue', 
    'Q2 Operations', 
    'Q2 Revenue', 
    'Q3 Expansion', 
    'Q3 Revenue', 
    'Q4 R&D', 
    'Q4 Revenue'
]
values = [500000, -100000, 150000, -50000, 200000, -150000, 300000, -100000, 400000]

# Calculate cumulative values and percentage changes
cumulative_values = np.cumsum(values)
cumulative_values = np.insert(cumulative_values, 0, 0)  # Starting point
values_with_start = np.insert(values, 0, 0)  # Include initial point
percentage_changes = np.diff(cumulative_values) / np.abs(cumulative_values[:-1]) * 100
percentage_changes = np.insert(percentage_changes, 0, 0)  # Include initial point

# Define color map using gradient
def color_gradient(value):
    return '#76c7c0' if value >= 0 else '#ff6b6b'

colors = [color_gradient(x) for x in values]

# Plot the waterfall chart
fig, ax = plt.subplots(figsize=(14, 8))

# Bars with gradient
for i in range(1, len(cumulative_values)):
    ax.bar(i, values_with_start[i], bottom=cumulative_values[i-1], color=colors[i-1], edgecolor='grey')

# Connect the bars with lines
for i in range(1, len(cumulative_values) - 1):
    ax.plot([i, i + 1], [cumulative_values[i], cumulative_values[i]], color='black', linestyle='--')

# Title and labels
ax.set_title("InnovateTech's Financial Journey in 2023\nQuarterly Impacts on Revenue", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Cumulative Revenue ($)", fontsize=12)
ax.set_xticks(range(1, len(events) + 1))
ax.set_xticklabels(events, rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Annotating each bar with amounts and percentage change
for i, value in enumerate(cumulative_values[1:], 1):
    # Amount annotation
    ax.text(i, cumulative_values[i] + (50000 if values_with_start[i] >= 0 else -100000), 
            f"${cumulative_values[i]:,}", ha='center', va='bottom' if values_with_start[i] >= 0 else 'top', 
            fontweight='bold', color='black')
    # Percentage annotation
    ax.text(i, cumulative_values[i] - (100000 if values_with_start[i] >= 0 else 200000), 
            f"({percentage_changes[i]:.1f}%)", ha='center', va='bottom' if values_with_start[i] >= 0 else 'top', 
            fontstyle='italic', fontsize=10, color='grey')

# Baseline for starting point
ax.axhline(y=0, color='grey', linewidth=0.8, linestyle='--')

# Adding a legend
custom_legend = [plt.Line2D([0], [0], color='#76c7c0', lw=4, label='Gain'),
                 plt.Line2D([0], [0], color='#ff6b6b', lw=4, label='Loss')]
ax.legend(handles=custom_legend, loc='upper left')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()