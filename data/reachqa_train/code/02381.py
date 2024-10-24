import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data representing charging times (in minutes) at different stations
charging_times = [
    [20, 22, 25, 23, 27, 50, 21, 22, 24, 29, 30],  # Station A
    [35, 45, 42, 37, 80, 33, 40, 39, 38, 90, 36],  # Station B
    [15, 16, 18, 14, 17, 19, 15, 16, 18, 17, 16],  # Station C
    [55, 56, 54, 55, 55, 55, 56, 54, 55, 54, 56],  # Station D
    [20, 25, 30, 35, 40, 50, 60, 70, 80, 30, 40],  # Station E
]

# Station labels
stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('#f0f0f0')  # Setting a light background color

# Create a horizontal boxplot with a notch and different colors
colors = sns.color_palette("pastel", len(stations))
bp = ax.boxplot(charging_times, vert=False, patch_artist=True, notch=True,
                boxprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='darkblue', linewidth=2),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', color='red', alpha=0.7))

# Setting facecolor for each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding annotations for means
for i, times in enumerate(charging_times):
    mean = np.mean(times)
    ax.annotate(f'Mean: {mean:.1f}', xy=(mean, i+1), xytext=(mean + 5, i+1),
                textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, ha='center', va='bottom', color='darkred')

# Customize the plot with titles and labels
ax.set_title("Distribution of Electric Vehicle (EV) Charging Times\nAcross Metropolitan Charging Stations", 
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Charging Time (Minutes)", fontsize=12, labelpad=10)
ax.set_yticklabels(stations, fontsize=12)

# Enhance readability with grid
ax.grid(True, linestyle='--', alpha=0.6)

# Adding a subtle background
ax.set_facecolor('#ffffff')

# Add a legend that corresponds to the color coding for each station
for i, color in enumerate(colors):
    ax.scatter([], [], color=color, label=stations[i])
ax.legend(loc='upper right', fontsize=10, frameon=True, framealpha=1, edgecolor='black')

# Automatically adjust layout for optimal display
plt.tight_layout()

# Show the plot
plt.show()