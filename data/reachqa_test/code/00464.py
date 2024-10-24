import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Data for the funnel chart
stages = ['Sports Enthusiasts', 'Event Awareness', 'Ticket Purchases', 'Attendance']
values = [500, 250, 100, 60]  # Values in thousands
conversion_rates = [100, 50, 40, 60]  # Conversion rates in percentage

# Prepare figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Define colors for each stage
colors = ['#4CAF50', '#2196F3', '#FFC107', '#FF5722']

# Funnel chart
for i, value in enumerate(values):
    if i == 0:
        ax1.add_patch(patches.Rectangle((0, i * 30), value, 20, color=colors[i], label=f'{value}K'))
    else:
        ax1.add_patch(patches.Polygon([
            (0, i * 30), (value, i * 30), 
            (value * 0.8, i * 30 + 20), (0, i * 30 + 20)
        ], color=colors[i], label=f'{value}K'))

    ax1.text(value / 2, i * 30 + 10, f'{value}K', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

ax1.set_title('Conversion Funnel for Sports Event Participation\nin 2023', fontsize=16, fontweight='bold')
ax1.set_xlabel('Number of Individuals (in thousands)', fontsize=12)
ax1.set_ylabel('Stages', fontsize=12)
ax1.set_xlim(0, max(values) * 1.2)
ax1.set_ylim(-10, len(stages) * 30)
ax1.set_yticks(np.arange(len(stages)) * 30)  # Set y-ticks at appropriate positions
ax1.set_yticklabels(stages)  # Set y-tick labels
ax1.xaxis.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', fontsize=10)

# Bar chart for conversion rates
ax2.bar(stages, conversion_rates, color=colors, alpha=0.7)
ax2.set_title('Conversion Rates at Each Stage (%)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Stages', fontsize=12)
ax2.set_ylabel('Conversion Rate (%)', fontsize=12)
ax2.set_ylim(0, 110)  # Since rates are in percentage
ax2.yaxis.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plots
plt.show()