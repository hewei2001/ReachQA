import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy capacity changes
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
capacity_changes = np.array([50, 30, -10, 60, 80, -20, 70, 50, -15, 90, 40, 30])
initial_capacity = 500

# Cumulative capacity calculation
cumulative_capacity = np.concatenate(([initial_capacity], initial_capacity + np.cumsum(capacity_changes)))

# Calculate percentage change for additional overlay using previous cumulative capacity values
previous_cumulative = cumulative_capacity[:-1]
percentage_changes = (capacity_changes / previous_cumulative) * 100

# New hypothetical data: solar intensity index for each month
solar_intensity = [75, 80, 78, 85, 88, 90, 95, 85, 82, 80, 77, 76]

# Waterfall chart
fig, ax1 = plt.subplots(figsize=(14, 9))

colors = ['green' if change >= 0 else 'red' for change in capacity_changes]
ax1.axhline(initial_capacity, linestyle='--', color='black', linewidth=1, label='Starting Capacity')

prev_value = initial_capacity
for i, (month, change) in enumerate(zip(months, capacity_changes)):
    ax1.bar(month, change, bottom=prev_value, color=colors[i], edgecolor='black', linewidth=0.6)
    ax1.text(i, prev_value + change/2, f'{change:+}', ha='center', va='center', fontsize=10, color='white')
    ax1.text(i, prev_value + change, f'{cumulative_capacity[i+1]:.0f}', ha='center', va='bottom', fontsize=9, color='black')
    prev_value += change

ax1.plot(np.arange(len(months)+1) - 0.5, cumulative_capacity, marker='o', color='blue', label='Cumulative Capacity', linewidth=1.5, zorder=3)
ax1.set_title('EcoLand Renewable Energy Growth: 2023 Overview\nand Solar Intensity Impact', fontsize=16, pad=20)
ax1.set_xlabel('Months', fontsize=14)
ax1.set_ylabel('Capacity (MW)', fontsize=14, color='black')

# Second y-axis for solar intensity
ax2 = ax1.twinx()
ax2.plot(months, solar_intensity, color='orange', linestyle='--', marker='s', label='Solar Intensity Index', linewidth=1.5)
ax2.set_ylabel('Solar Intensity Index', fontsize=14, color='orange')

ax1.grid(True, linestyle='--', alpha=0.6, axis='y')
ax1.set_xlim(-0.5, len(months) - 0.5)
ax1.set_xticklabels(months, rotation=45, ha='right')

# Legends for both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()