import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the data
wonders = [
    "Great Pyramid\nof Giza",
    "Hanging Gardens\nof Babylon",
    "Statue of Zeus\nat Olympia",
    "Temple of Artemis\nat Ephesus",
    "Mausoleum\nat Halicarnassus",
    "Colossus\nof Rhodes"
]

periods = ["Early", "Mid", "Recent"]
excavation_heights = [
    [18, 35, 52],
    [8, 28, 39],
    [13, 32, 46],
    [19, 31, 47],
    [10, 26, 44],
    [15, 27, 43]
]

# Compute the average excavation height for each period
average_heights_by_period = np.mean(excavation_heights, axis=0)

# Coordinates for 3D bar plot
wonders_pos = np.arange(len(wonders))
periods_pos = np.arange(len(periods))
wonders_pos, periods_pos = np.meshgrid(wonders_pos, periods_pos)

# Flatten the coordinates for the bar plot
wonders_pos_flat = wonders_pos.flatten()
periods_pos_flat = periods_pos.flatten()
heights_flat = np.array(excavation_heights).flatten()

# Set colors for periods
colors = ['skyblue', 'lightgreen', 'lightcoral']

# Create a figure with two subplots
fig = plt.figure(figsize=(18, 8))

# First subplot: 3D bar plot
ax1 = fig.add_subplot(121, projection='3d')

# Plot each period separately for clarity in the first subplot
for period_idx in range(len(periods)):
    heights_for_period = np.array(excavation_heights)[:, period_idx]
    ax1.bar3d(
        wonders_pos_flat[periods_pos_flat == period_idx],
        periods_pos_flat[periods_pos_flat == period_idx],
        np.zeros_like(heights_for_period),
        0.8, 0.8, heights_for_period,
        color=colors[period_idx],
        alpha=0.7,
        label=periods[period_idx]
    )

# Set the axes labels and title for the first subplot
ax1.set_xlabel('Wonder', fontsize=10, labelpad=10)
ax1.set_ylabel('Excavation Period', fontsize=10, labelpad=10)
ax1.set_zlabel('Excavation Height (m)', fontsize=10, labelpad=10)
ax1.set_title("Excavation Heights of Ancient Wonders\nSpanning the 20th and 21st Century", fontsize=14, fontweight='bold', pad=20)

# Set the ticks and labels for the axes of the first subplot
ax1.set_xticks(np.arange(len(wonders)) + 0.4)
ax1.set_xticklabels(wonders, rotation=45, ha='right', fontsize=9)
ax1.set_yticks(np.arange(len(periods)) + 0.4)
ax1.set_yticklabels(periods, fontsize=9)
ax1.set_zlim(0, 60)

# Adjust the viewing angle for better visibility
ax1.view_init(elev=20, azim=145)

# Add a legend to the first subplot
ax1.legend(loc='upper right', fontsize=10)

# Second subplot: line plot
ax2 = fig.add_subplot(122)

# Plot the average excavation height over periods for each wonder in the second subplot
wonders_pos_line = np.arange(len(wonders))
for wonder_idx, wonder in enumerate(wonders):
    heights_by_wonder = np.array(excavation_heights)[wonder_idx]
    ax2.plot(
        periods, heights_by_wonder, marker='o', label=wonder.replace('\n', ' '), linewidth=2
    )

# Set the axes labels and title for the second subplot
ax2.set_xlabel('Excavation Period', fontsize=10, labelpad=10)
ax2.set_ylabel('Excavation Height (m)', fontsize=10, labelpad=10)
ax2.set_title("Trends in Excavation Heights Across Wonders", fontsize=14, fontweight='bold')

# Add a legend to the second subplot
ax2.legend(loc='upper left', fontsize=8)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()