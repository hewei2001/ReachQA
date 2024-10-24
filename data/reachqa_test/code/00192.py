import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Original data for coffee consumption and self-reported efficiency scores
coffee_consumption = np.array([0, 1, 2, 3, 4, 5, 6])
efficiency_scores = np.array([5.5, 6.1, 7.0, 8.2, 8.5, 8.4, 7.8])

# Construct new data: average break duration after coffee consumption (in minutes)
break_durations = np.array([30, 28, 25, 20, 22, 23, 24])

# Create the figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Subplot 1: Scatter plot with a spline fitting line
ax1.scatter(coffee_consumption, efficiency_scores, color='tab:blue', alpha=0.7, edgecolors='w', s=100)
spline = interpolate.splrep(coffee_consumption, efficiency_scores, s=0)
smooth_x = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
smooth_y = interpolate.splev(smooth_x, spline)
ax1.plot(smooth_x, smooth_y, color='tab:orange', lw=2, label='Efficiency Trend')
ax1.set_title('Remote Work Efficiency vs.\nCoffee Consumption', fontsize=14, weight='bold', ha='center')
ax1.set_xlabel('Cups of Coffee Consumed per Day', fontsize=12)
ax1.set_ylabel('Efficiency Score (1-10)', fontsize=12)

# Annotations for significant observations
annotations = {0: 'Non-coffee drinkers', 3: 'Peak Efficiency', 6: 'Over-caffeination?'}
for cups, text in annotations.items():
    idx = np.where(coffee_consumption == cups)[0][0]
    ax1.annotate(text, xy=(cups, efficiency_scores[idx]), 
                 xytext=(cups, efficiency_scores[idx] + 0.5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='center',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_xlim(-0.5, 6.5)
ax1.set_ylim(5, 10)
ax1.legend(loc='lower right', fontsize=10)

# Subplot 2: Bar plot for break durations
ax2.bar(coffee_consumption, break_durations, color='tab:green', alpha=0.7, edgecolor='black', width=0.6)
ax2.set_title('Break Duration after Coffee Consumption', fontsize=14, weight='bold')
ax2.set_xlabel('Cups of Coffee Consumed per Day', fontsize=12)
ax2.set_ylabel('Average Break Duration (minutes)', fontsize=12)

# Show the figure layout without overlapping
plt.tight_layout()
plt.show()