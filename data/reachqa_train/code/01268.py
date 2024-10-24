import matplotlib.pyplot as plt
import numpy as np

# Define the decades and the thematic innovations for each
decades = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
innovations = np.array([5, 8, 12, 15, 20, 25, 28, 30, 32, 35, 38])
std_devs = np.array([1.5, 2, 1, 3, 2, 2.5, 2, 2.2, 2.5, 3, 3.5])

# Calculate the percentage change from the previous decade
percentage_change = np.diff(innovations) / innovations[:-1] * 100
# Align percentage change data to decades
change_decades = decades[1:]

# Initialize the plot with 1x2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot the line chart with error bars on the first subplot
ax1.errorbar(decades, innovations, yerr=std_devs, fmt='-o', color='darkblue',
             ecolor='skyblue', elinewidth=2, capsize=4, capthick=2, alpha=0.8,
             label='Thematic Innovations')
ax1.set_title("Thematic Innovations Over Decades", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Decades", fontsize=12)
ax1.set_ylabel("Number of New Thematic Innovations", fontsize=12)
ax1.set_xticks(decades)
ax1.set_xticklabels(decades, rotation=45)
ax1.set_yticks(np.arange(0, 45, 5))
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left')

# Annotate the maximum innovation point
max_idx = np.argmax(innovations)
ax1.annotate('Peak Innovation', xy=(decades[max_idx], innovations[max_idx]), 
             xytext=(decades[max_idx]-10, innovations[max_idx]+5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Plot the bar chart for percentage changes on the second subplot
ax2.bar(change_decades, percentage_change, color='darkcyan', alpha=0.8)
ax2.set_title("Percentage Change in Innovations", fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel("Decades", fontsize=12)
ax2.set_ylabel("Percentage Change (%)", fontsize=12)
ax2.set_xticks(change_decades)
ax2.set_xticklabels(change_decades, rotation=45)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate major increase
max_change_idx = np.argmax(percentage_change)
ax2.annotate(f'Max Increase ({percentage_change[max_change_idx]:.1f}%)', 
             xy=(change_decades[max_change_idx], percentage_change[max_change_idx]), 
             xytext=(change_decades[max_change_idx]-10, percentage_change[max_change_idx]+10),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()