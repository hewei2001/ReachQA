import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year
months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

# Hypothetical average daily exercise in minutes
daily_exercise_minutes = np.array([25, 30, 35, 50, 55, 60, 65, 60, 50, 40, 35, 30])

# Hypothetical mental health index levels (0-100 scale)
mental_health_index = np.array([65, 68, 70, 76, 78, 81, 85, 83, 78, 72, 70, 68])

# Create the line chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the first line for daily exercise
line1 = ax1.plot(months, daily_exercise_minutes, color='teal', linestyle='-', marker='o', linewidth=2, markersize=8, label='Average Daily Exercise (mins)')

# Create a secondary y-axis for the mental health index
ax2 = ax1.twinx()
line2 = ax2.plot(months, mental_health_index, color='indigo', linestyle='--', marker='s', linewidth=2, markersize=8, label='Mental Health Index')

# Annotate significant points
annotations = {
    'April': ('New programs', (0, 50)),
    'July': ('Heatwave impact', (0, -50)),
    'October': ('Awareness campaign', (0, 50))
}

for month, (text, offset) in annotations.items():
    index = np.where(months == month)[0][0]
    ax1.annotate(
        text, 
        (months[index], daily_exercise_minutes[index]), 
        xytext=offset, 
        textcoords='offset points', 
        arrowprops=dict(arrowstyle='->', color='grey'),
        ha='center', fontsize=10, color='darkred'
    )

# Titles and labels
ax1.set_title("Impact of Daily Exercise on Mental Health Levels\nin CityX (2022)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14)
ax1.set_ylabel("Average Daily Exercise (mins)", fontsize=14, color='teal')
ax2.set_ylabel("Mental Health Index", fontsize=14, color='indigo')

# Combine legends from both lines
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=12)

# Styling
ax1.xaxis.set_tick_params(rotation=45)
ax1.yaxis.set_tick_params(labelcolor='teal')
ax2.yaxis.set_tick_params(labelcolor='indigo')

# Grid and layout adjustments
ax1.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()