import matplotlib.pyplot as plt
import numpy as np

# Original Data
hyperloop_pods = [12, 15, 14, 16, 10, 13, 11, 14, 15, 13]
autonomous_drones = [7, 6, 5, 9, 10, 8, 7, 5, 6, 7]
maglev_trains = [18, 20, 19, 17, 22, 21, 19, 20, 18, 17]
solar_powered_buses = [25, 28, 30, 27, 26, 29, 31, 25, 27, 28]

data = [hyperloop_pods, autonomous_drones, maglev_trains, solar_powered_buses]

# New Data for the additional subplot
cities = ["City A", "City B", "City C", "City D", "City E"]
average_times = {
    "Hyperloop Pods": [13, 14, 12, 15, 13],
    "Autonomous Drones": [6, 7, 5, 6, 6],
    "Maglev Trains": [19, 18, 20, 19, 21],
    "Solar-Powered Buses": [26, 27, 25, 28, 29],
}

# Set up the figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Box Plot on the left
bp = ax1.boxplot(data, patch_artist=True, notch=True, widths=0.5,
           boxprops=dict(facecolor='#ADD8E6', color='black'),
           whiskerprops=dict(color='black', linestyle='--'),
           capprops=dict(color='black'),
           medianprops=dict(color='red', linewidth=2),
           flierprops=dict(marker='o', color='black', alpha=0.5))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color)

ax1.set_title("The Quantum Leap in Urban Transportation:\nEvaluating the Time Efficiency of Innovative Vehicles", 
              fontsize=14, fontweight='bold')
ax1.set_ylabel("Travel Time (Minutes)", fontsize=12)
ax1.set_xlabel("Transportation Modes", fontsize=12)
ax1.set_xticklabels(["Hyperloop Pods", "Autonomous Drones", "Maglev Trains", "Solar-Powered Buses"], 
                    fontsize=10, rotation=15)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
ax1.annotate('Fastest on average', xy=(2, 7), xytext=(2.5, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='green')

# Bar Plot on the right
x = np.arange(len(cities))  # the label locations
width = 0.2  # the width of the bars

# Plot each transportation mode
for idx, (mode, times) in enumerate(average_times.items()):
    ax2.bar(x + idx*width, times, width, label=mode)

ax2.set_title("Average Travel Times Across Various Cities", fontsize=14, fontweight='bold')
ax2.set_ylabel("Average Travel Time (Minutes)", fontsize=12)
ax2.set_xlabel("Cities", fontsize=12)
ax2.set_xticks(x + width)
ax2.set_xticklabels(cities, fontsize=10)
ax2.legend(title="Transportation Modes", fontsize=9, title_fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()