import matplotlib.pyplot as plt
import numpy as np

# Data for travel times (in minutes) for each transport mode in the futuristic city of Tomorrowville
# This fictional data is designed to represent daily travel times and their variability across various transport modes.
hyperloop_times = [30, 32, 29, 28, 34, 27, 31, 30, 28, 33, 29, 32, 31, 30]
flying_taxi_times = [20, 22, 19, 25, 23, 21, 24, 20, 22, 23, 21, 25, 24, 20]
autonomous_drone_times = [10, 12, 8, 15, 11, 9, 10, 12, 14, 13, 11, 10, 9, 12]
smart_train_times = [45, 47, 50, 43, 48, 46, 49, 45, 47, 44, 46, 50, 48, 45]

# Combine the data into a list
data = [hyperloop_times, flying_taxi_times, autonomous_drone_times, smart_train_times]

# Labels for the transport modes
transport_modes = ['Hyperloop', 'Flying Taxi', 'Autonomous Drone', 'Smart Train']

# Create the figure and the axis
fig, ax = plt.subplots(figsize=(12, 7))

# Create horizontal box plot
boxplots = ax.boxplot(data, vert=False, patch_artist=True, showmeans=True, notch=True)

# Customize colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Customize the means, medians, and whiskers
for whisker in boxplots['whiskers']:
    whisker.set(color='#7570b3', linewidth=2, linestyle='--')
for cap in boxplots['caps']:
    cap.set(color='#7570b3', linewidth=2)
for median in boxplots['medians']:
    median.set(color='orange', linewidth=2)
for mean in boxplots['means']:
    mean.set(marker='o', color='red', markersize=5)

# Add title and labels
ax.set_title('Efficiency of Futuristic Transport Modes in Tomorrowville', fontsize=16, pad=15)
ax.set_xlabel('Daily Travel Time (minutes)', fontsize=12)
ax.set_yticklabels(transport_modes, fontsize=12)

# Adding grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()