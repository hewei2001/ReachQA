import matplotlib.pyplot as plt
import numpy as np

# Original data
appliances = ['Washing Machines', 'Dishwashers', 'Toilets', 'Showers', 'Faucets']
original_data = [40, 15, 30, 50, 20]
conservation_measures = ['Washing Machines\n(Reduced by 37.5%)', 'Dishwashers\n(Reduced by 33.3%)', 'Toilets\n(Reduced by 33.3%)', 'Showers\n(Reduced by 30%)', 'Faucets\n(Reduced by 25%)']
reduced_data = [25, 10, 20, 35, 15]

# Water savings percentage data
savings_data = [((original - reduced) / original) * 100 for original, reduced in zip(original_data, reduced_data)]

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Set x-axis positions
x_pos = np.arange(len(appliances))

# Bar width
bar_width = 0.35

# Plot bars
ax1.bar(x_pos - bar_width/2, original_data, width=bar_width, label='Original', color='#6495ED', edgecolor='black', alpha=0.8)
ax1.bar(x_pos + bar_width/2, reduced_data, width=bar_width, label='Reduced', color='#DC143C', edgecolor='black', alpha=0.8)

# Add text labels for original data
for i, value in enumerate(original_data):
    ax1.text(x_pos[i] - bar_width/2, value + 2, f"{value}\ngallons/day", ha='center', va='bottom', fontsize=8, fontweight='bold')

# Add text labels for reduced data
for i, value in enumerate(reduced_data):
    ax1.text(x_pos[i] + bar_width/2, value + 2, f"{value}\ngallons/day", ha='center', va='bottom', fontsize=8, fontweight='bold')

# Set title
ax1.set_title("Average Water Usage in Household Appliances\nBefore and After Water-Saving Measures")

# Set x-axis and y-axis labels
ax1.set_xlabel('Appliance Type')
ax1.set_ylabel('Water Usage (gallons/day)')

# Set x-axis ticks
ax1.set_xticks(x_pos)
ax1.set_xticklabels(appliances, rotation=45, ha='right')

# Set y-axis ticks
ax1.set_yticks(range(0, max(max(original_data), max(reduced_data)) + 5, 5))

# Add grid lines
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
ax1.legend(loc='upper left')

# Create a secondary y-axis
ax2 = ax1.twinx()

# Plot water savings percentage line
ax2.plot(x_pos, savings_data, marker='o', linestyle='-', color='green', label='Water Savings (%)')

# Add text labels for water savings percentage
for i, value in enumerate(savings_data):
    ax2.text(x_pos[i], value + 1, f"{value:.1f}%", ha='center', va='bottom', fontsize=8, fontweight='bold')

# Set y-axis label
ax2.set_ylabel('Water Savings (%)')

# Set y-axis ticks
ax2.set_yticks(range(0, 41, 10))

# Add legend
ax2.legend(loc='upper right')

# Adjust layout to prevent text from being cut off
plt.tight_layout()

plt.show()