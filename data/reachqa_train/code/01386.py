import matplotlib.pyplot as plt
import numpy as np

# Define the years and index changes over a longer period
years = [f'Year {i}' for i in range(1, 21)]
changes = [0, 5, 3, -4, 6, -2, 7, 4, -3, 5, 2, -1, 5, -3, 4, -2, 3, -5, 6, 4]  # Incremental changes

# Starting point of the public health index
start_index = 100

# Calculate cumulative values for plotting
values = np.cumsum([start_index] + changes[:-1])

# Define multiple data series for different health metrics
life_expectancy_changes = [0, 2, 1, -2, 3, -1, 2, 1, 0, 1, 3, -1, 2, -2, 1, 0, 1, -1, 2, 2]
healthcare_spending_changes = [0, 4, 3, -3, 4, -1, 5, 3, -2, 4, 1, 0, 2, -1, 3, 1, 2, -2, 3, 4]

# Define cumulative values for other metrics
life_expectancy_values = np.cumsum([start_index] + life_expectancy_changes[:-1])
healthcare_spending_values = np.cumsum([start_index] + healthcare_spending_changes[:-1])

# Initialize plot with subplots for comparison
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
ax1, ax2 = axes

# Plot the first bar chart for Public Health Index
colors = ['g' if change > 0 else 'r' for change in changes]
bars = ax1.bar(years, changes, bottom=values, color=colors, width=0.5, edgecolor='black')
ax1.bar(years[-1], start_index + sum(changes) - start_index, bottom=start_index, color='b', alpha=0.7, width=0.5)

# Annotations for the first chart
for i, (bar, change) in enumerate(zip(bars, changes)):
    height = bar.get_height()
    final_value = values[i] + change
    ax1.annotate(f'{height:+}\n({final_value})', 
                 xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                 xytext=(0, 0), textcoords='offset points', ha='center', va='center', color='white', fontsize=8)

# Plot lines to connect the bars
for i in range(1, len(values)):
    ax1.plot([i - 1 + 0.5, i + 0.5], [values[i - 1], values[i]], 'k--', linewidth=0.8)

# Title and labels for the first chart
ax1.set_title("Long-Term Health Trends: Impact on Public Health Index and Related Metrics", fontsize=14, fontweight='bold')
ax1.set_ylabel("Public Health Index Change", fontsize=12)
ax1.legend(["Net Change (Final Index)"], loc='upper left', fontsize=10)

# Second subplot for additional metrics
ax2.plot(years, life_expectancy_values, marker='o', linestyle='-', color='m', label='Life Expectancy Index')
ax2.plot(years, healthcare_spending_values, marker='s', linestyle='-', color='c', label='Healthcare Spending Index')

# Annotations for the second chart
for i, (year, le_val, hs_val) in enumerate(zip(years, life_expectancy_values, healthcare_spending_values)):
    ax2.annotate(f'{le_val}', xy=(i, le_val), xytext=(0, 5), textcoords='offset points', ha='center', fontsize=8, color='m')
    ax2.annotate(f'{hs_val}', xy=(i, hs_val), xytext=(0, -10), textcoords='offset points', ha='center', fontsize=8, color='c')

# Title, labels, and legend for the second chart
ax2.set_ylabel("Index Value", fontsize=12)
ax2.set_xlabel("Year", fontsize=12)
ax2.legend(loc='upper left', fontsize=10)

# Customize grid and ticks
for ax in axes:
    ax.grid(True, linestyle='--', alpha=0.5)
ax2.set_xticks(range(len(years)))
ax2.set_xticklabels(years, rotation=45)

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()