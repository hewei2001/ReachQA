import matplotlib.pyplot as plt
import numpy as np

# Water resource management data for Martian Colony X
labels = ["Initial Reserves", "Ice Extraction", "Recycling", "Resident Usage", "Agriculture", "Industry", "Ending Balance"]
values = [500, 200, 150, -180, -100, -120]

# Calculate cumulative sum for the waterfall chart, including ending balance
cumulative_values = np.cumsum([values[0]] + values[1:] + [0])  # add 0 to reflect the ending balance
steps = np.arange(len(labels))  # steps now matches the number of labels

# Water usage breakdown for the pie chart
usage_labels = ["Resident Usage", "Agriculture", "Industry"]
usage_values = [180, 100, 120]

# Color coding for the waterfall bars
colors = ["#4CAF50" if x >= 0 else "#FF5722" for x in values]  
colors[0] = "#2196F3"  
colors.append("#9C27B0")  # add color for ending balance

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Waterfall chart
ax1.bar(steps, cumulative_values, width=0.6, color=colors, edgecolor='black')
for i in range(1, len(cumulative_values)):
    ax1.plot([steps[i - 1], steps[i]], [cumulative_values[i - 1], cumulative_values[i]], color='black', linestyle='--', linewidth=0.8)

for i, (label, value) in enumerate(zip(labels, cumulative_values)):
    ax1.text(i, value + (20 if value >= 0 else -25), f'{value}', ha='center', va='bottom' if value >= 0 else 'top', color='black', fontweight='bold')

ax1.set_title("Monthly Water Resource Management\nin Martian Colony X", fontsize=14, weight='bold')
ax1.set_ylabel("Water Reserves (thousand liters)", fontsize=12)
ax1.set_xticks(steps)
ax1.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

legend_labels = ['Inflow', 'Outflow', 'Initial Reserves', 'Ending Balance']
legend_colors = ['#4CAF50', '#FF5722', '#2196F3', '#9C27B0']
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in legend_colors]
ax1.legend(handles, legend_labels, loc='upper right')

# Pie chart of water usage
ax2.pie(usage_values, labels=usage_labels, autopct='%1.1f%%', startangle=140, colors=['#FFC107', '#3F51B5', '#FF9800'])
ax2.set_title("Water Usage Distribution\nby Sector", fontsize=14, weight='bold')

plt.tight_layout()
plt.show()