import matplotlib.pyplot as plt
import numpy as np

# Step ranges and frequency of employees
step_ranges = [
    '0-2000', '2000-5000', '5000-7500', 
    '7500-10000', '10000-15000', '15000-20000'
]
frequency = np.array([12, 58, 32, 18, 7, 3])

# Cumulative frequency for the line plot
cumulative_frequency = np.cumsum(frequency)

# Bins for the histogram
bins = [0, 2000, 5000, 7500, 10000, 15000, 20000]

# Plotting setup
fig, ax1 = plt.subplots(figsize=(12, 8))

# Histogram plot
ax1.hist(bins[:-1], bins=bins, weights=frequency, color='lightseagreen', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Step Count Range', fontsize=14)
ax1.set_ylabel('Number of Employees', fontsize=14, color='black')
ax1.set_xticks(bins)
ax1.set_ylim(0, max(frequency) + 5)
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Overlay line plot for cumulative frequency
ax2 = ax1.twinx()
ax2.plot(bins[:-1], cumulative_frequency, color='salmon', marker='o', linestyle='-', linewidth=2, markersize=8, label='Cumulative Frequency')
ax2.set_ylabel('Cumulative Number of Employees', fontsize=14, color='salmon')
ax2.set_ylim(0, max(cumulative_frequency) + 10)

# Add text annotations for bars
for i, (x, y) in enumerate(zip(bins[:-1], frequency)):
    ax1.text(x + (bins[i+1] - x) / 2, y + 1, f'{step_ranges[i]}: {y}', fontsize=10, ha='center', va='bottom')

# Adding legends
ax1.legend(['Step Frequency'], loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# Multi-line title
plt.title('Daily Steps Distribution and Cumulative Frequency\nin a Tech Company', fontsize=16, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()