import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
activities = ['Painting', 'Sculpture', 'Digital Art', 'Sketching', 'Photography']
time_spent = [240, 180, 150, 120, 90]

# Positions for each activity on the x-axis
x_positions = np.arange(len(activities))

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(x_positions, time_spent, color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#B3B3B3'])

# Annotate each bar with the time spent
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval} min', ha='center', va='bottom', fontsize=10, weight='bold')

# Customize the plot
ax.set_xlabel('Art Activities', fontsize=12, weight='bold')
ax.set_ylabel('Average Time Spent (minutes)', fontsize=12, weight='bold')
ax.set_title('Time Allocation in Art Workshop Activities\nat The Creative Canvas Academy', fontsize=14, weight='bold')

# Setting the x-ticks to match the activities and adjusting rotation
ax.set_xticks(x_positions)
ax.set_xticklabels(activities, rotation=15, ha='right', fontsize=11)

# Adding grid lines for better estimation of values
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()