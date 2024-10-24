import matplotlib.pyplot as plt
import numpy as np

# Define the years and index changes
years = [f'Year {i}' for i in range(1, 11)]
changes = [0, 5, 3, -4, 6, -2, 7, 4, -3, 5]  # Year 1 as baseline, others are incremental changes

# Starting point of the public health index
start_index = 100

# Calculate cumulative values for plotting
values = np.cumsum([start_index] + changes[:-1])

# Define colors for gains and losses
colors = ['g' if change > 0 else 'r' for change in changes]

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot bars with color coding
bars = ax.bar(years, changes, bottom=values, color=colors, width=0.5, edgecolor='black')

# Highlight the total change using a different color (blue)
final_index = start_index + sum(changes)
ax.bar(years[-1], final_index - start_index, bottom=start_index, color='b', alpha=0.7, width=0.5)

# Add annotations to bars
for i, (bar, change) in enumerate(zip(bars, changes)):
    height = bar.get_height()
    final_value = values[i] + change
    ax.annotate(f'{height:+}\n({final_value})', 
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                xytext=(0, 0), textcoords='offset points', ha='center', va='center', color='white', fontsize=9)

# Draw lines to connect the bars
for i in range(1, len(values)):
    ax.plot([i - 1 + 0.5, i + 0.5], [values[i - 1], values[i]], 'k--', linewidth=0.8)

# Add title and labels with adjustments for readability
ax.set_title("Decade of Health Initiatives:\nImpact on Healthville's Public Health Index", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Public Health Index Change", fontsize=12)

# Add legend
ax.legend(["Net Change (Final Index)"], loc='upper left', fontsize=10)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()