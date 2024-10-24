import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
activities = ['Painting', 'Sculpture', 'Digital Art', 'Sketching', 'Photography']
time_spent = [240, 180, 150, 120, 90]

# Calculate percentages of total time
total_time = sum(time_spent)
percentages = [t / total_time * 100 for t in time_spent]

# Positions for each activity on the x-axis
x_positions = np.arange(len(activities))

# Create the bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create bars with gradient colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#B3B3B3']
bars = ax1.bar(x_positions, time_spent, color=colors, edgecolor='darkgrey', linewidth=1.5, zorder=3)

# Annotate each bar with the time spent and percentage
for bar, percentage in zip(bars, percentages):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval} min\n({percentage:.1f}%)', 
             ha='center', va='bottom', fontsize=10, weight='bold', color='darkred', zorder=4)

# Add secondary y-axis for percentage
ax2 = ax1.twinx()
ax2.set_ylim(ax1.get_ylim())
ax2.set_yticks(ax1.get_yticks())
ax2.set_yticklabels([f'{int(y / total_time * 100)}%' for y in ax1.get_yticks()])
ax2.set_ylabel('Percentage of Total Time (%)', fontsize=12, weight='bold')

# Customize the plot
ax1.set_xlabel('Art Activities', fontsize=12, weight='bold')
ax1.set_ylabel('Average Time Spent (minutes)', fontsize=12, weight='bold')
ax1.set_title('Time Allocation in Art Workshop Activities\nat The Creative Canvas Academy', 
              fontsize=14, weight='bold', pad=20)

# Setting the x-ticks to match the activities and adjusting rotation
ax1.set_xticks(x_positions)
ax1.set_xticklabels(activities, rotation=15, ha='right', fontsize=11)

# Adding grid lines for better estimation of values
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7, zorder=0)

# Add a subtle background gradient to enhance the visual appearance
fig.patch.set_facecolor('#f5f5f5')
ax1.set_facecolor('#ffffff')

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()