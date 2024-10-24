import matplotlib.pyplot as plt
import numpy as np

# Data representing changes in renewable energy capacity in Megawatts (MW)
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
capacity_changes = np.array([50, 30, -10, 60, 80, -20, 70, 50, -15, 90, 40, 30])

# Initial renewable energy capacity at the start of the year
initial_capacity = 500

# Calculate cumulative capacity over the months
cumulative_capacity = np.concatenate(([initial_capacity], initial_capacity + np.cumsum(capacity_changes)))

# Determine the colors for the bars
colors = ['green' if change >= 0 else 'red' for change in capacity_changes]

# Plot the waterfall chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot initial capacity line
ax.axhline(initial_capacity, linestyle='--', color='black', linewidth=1, label='Starting Capacity')

# Bars and annotations
prev_value = initial_capacity
for i, (month, change) in enumerate(zip(months, capacity_changes)):
    ax.bar(month, change, bottom=prev_value, color=colors[i], edgecolor='black', linewidth=0.6)
    ax.text(i, prev_value + change/2, f'{change:+}', ha='center', va='center', fontsize=10, color='white')
    ax.text(i, prev_value + change, f'{cumulative_capacity[i+1]:.0f}', ha='center', va='bottom', fontsize=9, color='black')
    prev_value += change

# Add a line indicating the cumulative capacity
ax.plot(np.arange(len(months)+1) - 0.5, cumulative_capacity, marker='o', color='blue', label='Cumulative Capacity', linewidth=1.5, zorder=3)

# Titles and labels
ax.set_title('EcoLand Renewable Energy Growth\n2023 Overview', fontsize=16, pad=20)
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Capacity (MW)', fontsize=14)

# Enhance aesthetics
ax.grid(True, linestyle='--', alpha=0.6, axis='y')
ax.set_xlim(-0.5, len(months) - 0.5)

# Adjust x-axis labels to prevent overlapping
ax.set_xticklabels(months, rotation=45, ha='right')

# Adding legend
ax.legend(loc='upper left', fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()