import matplotlib.pyplot as plt
import numpy as np

# Data and labels for the donut pie chart
tasks = [
    'Data Cleaning', 
    'Modeling', 
    'Meetings', 
    'Research & Development', 
    'Visualization', 
    'Documentation', 
    'Personal Development'
]
hours = [10, 8, 6, 5, 4, 3, 4]

# Define a gradient color scheme
colors = ['#ff9999', '#ff8080', '#ff6666', '#ff4d4d', '#ff3333', '#ff1a1a', '#ff0000']

# Plotting the donut pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    hours, 
    labels=tasks, 
    autopct=lambda pct: f'{pct:.1f}%' if pct > 0 else '', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.1 if i == 0 else 0.05 for i in range(len(tasks))]  # Highlight segments with different explosions
)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

# Adding total hours in the center of the donut
total_hours = sum(hours)
ax.text(0, 0, f'{total_hours}\nHours Total', ha='center', va='center', fontsize=12, weight='bold')

# Title and styling with multiline break for long titles
plt.title("Time Allocation of a Modern Data Scientist's Week\n(Based on a Hypothetical Work Schedule)", fontsize=14, y=1.05)
plt.setp(autotexts, size=10, weight="bold", color="black")

# Add a legend outside the chart
ax.legend(wedges, tasks,
          title="Tasks",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()