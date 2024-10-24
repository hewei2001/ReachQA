import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define workout duration in minutes for each exercise routine
durations = np.array([10, 20, 30, 40, 50, 60])

# Define calories burned for each routine (Running, Cycling, Swimming)
calories_running = np.array([90, 160, 240, 310, 400, 480])
calories_cycling = np.array([65, 130, 190, 250, 320, 380])
calories_swimming = np.array([75, 140, 210, 280, 360, 440])

# Colors for each exercise routine
colors = ['#FF6347', '#4682B4', '#32CD32']

def smooth_line(x, y):
    x_new = np.linspace(x.min(), x.max(), 300)
    spl = make_interp_spline(x, y, k=3)  # Cubic spline
    y_smooth = spl(x_new)
    return x_new, y_smooth

plt.figure(figsize=(14, 8))

# Plot for Running
plt.scatter(durations, calories_running, color=colors[0], label='Running', marker='o', edgecolor='black', s=100)
x_smooth, y_smooth = smooth_line(durations, calories_running)
plt.plot(x_smooth, y_smooth, color=colors[0], linestyle='-', linewidth=2, alpha=0.9, label='Running Trend')

# Plot for Cycling
plt.scatter(durations, calories_cycling, color=colors[1], label='Cycling', marker='s', edgecolor='black', s=100)
x_smooth, y_smooth = smooth_line(durations, calories_cycling)
plt.plot(x_smooth, y_smooth, color=colors[1], linestyle='-', linewidth=2, alpha=0.9, label='Cycling Trend')

# Plot for Swimming
plt.scatter(durations, calories_swimming, color=colors[2], label='Swimming', marker='^', edgecolor='black', s=100)
x_smooth, y_smooth = smooth_line(durations, calories_swimming)
plt.plot(x_smooth, y_smooth, color=colors[2], linestyle='-', linewidth=2, alpha=0.9, label='Swimming Trend')

# Highlight key points with annotations
for i, txt in enumerate(durations):
    if i % 2 == 0:  # Annotate every other point for readability
        plt.annotate(txt, (durations[i], calories_running[i]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=9)
        plt.annotate(txt, (durations[i], calories_cycling[i]), textcoords="offset points", xytext=(10,10), ha='center', fontsize=9)
        plt.annotate(txt, (durations[i], calories_swimming[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9)

# Title and labels
plt.title('Calories Burned vs. Workout Duration\nfor Different Exercise Routines', fontsize=16, fontweight='bold')
plt.xlabel('Workout Duration (minutes)', fontsize=14)
plt.ylabel('Calories Burned', fontsize=14)

# Grid customization
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
plt.legend(title='Exercise Routine', fontsize=12, loc='upper left', ncol=1, fancybox=True, shadow=True)

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()