import matplotlib.pyplot as plt
import numpy as np

# Seasons and gardening activities
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
activities = ['Planting', 'Watering', 'Weeding', 'Pruning', 'Harvesting']

# Hours spent on each activity per season
activity_hours = np.array([
    [8, 18, 20, 10],    # Planting
    [6, 22, 34, 14],    # Watering
    [12, 18, 25, 28],   # Weeding
    [10, 8, 12, 24],    # Pruning
    [0, 12, 22, 32],    # Harvesting
])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors
colors = ['#8c564b', '#1f77b4', '#2ca02c', '#d62728', '#ff7f0e']

# Plot the stackplot
ax.stackplot(seasons, activity_hours, labels=activities, colors=colors, alpha=0.8)

# Adding title and labels
ax.set_title('Garden Landscaping Through the Seasons', fontsize=16, fontweight='bold', pad=10)
ax.set_xlabel('Seasons', fontsize=12)
ax.set_ylabel('Hours Spent', fontsize=12)

# Adding a legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Gardening Activities", fontsize='small', title_fontsize='medium')

# Adding gridlines for clarity
ax.grid(linestyle='--', alpha=0.7)

# Ensuring that the layout is optimized and readable
plt.tight_layout()

# Show the plot
plt.show()