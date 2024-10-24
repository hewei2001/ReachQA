import matplotlib.pyplot as plt
import numpy as np

# Define quarters and net changes
quarters = ['Q0 (Start)', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5']
values = [500, 150, -50, 200, -100, 300]  # Starting investment and quarterly changes

# Colors for positive and negative changes
colors = ['green' if v >= 0 else 'red' for v in values]

# Calculate cumulative values
cumulative = np.cumsum(values)

# Adjust cumulative for waterfall chart appearance
cumulative_adjusted = np.insert(cumulative[:-1], 0, 0)

# Define figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars with connection lines
ax.bar(quarters, values, color=colors, edgecolor='grey', linewidth=0.8)
ax.plot(quarters, cumulative, color='blue', marker='o', linestyle='--', linewidth=1.5)

# Adding text for each quarter's change and cumulative balance
for i in range(len(values)):
    y_offset = values[i] / 2
    ax.text(i, cumulative_adjusted[i] + y_offset, f'{values[i]}', ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, cumulative[i], f'{cumulative[i]}', va='bottom' if values[i] > 0 else 'top', ha='center', fontsize=9, color='blue')

# Customizing the chart
ax.set_title('The Rise and Fall of a Tech Startup:\nQuarterly Financial Analysis', fontsize=14, fontweight='bold')
ax.set_ylabel('Financial Balance ($k)', fontsize=12)
ax.set_ylim(min(cumulative_adjusted)-50, max(cumulative)+100)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Legend
ax.legend(['Net Balance'], loc='upper left')

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()