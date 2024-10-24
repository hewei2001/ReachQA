import matplotlib.pyplot as plt
import numpy as np

# Define sample reaction time data in milliseconds for each sport
basketball_times = [320, 315, 310, 325, 300, 330, 310, 340, 315, 320]
soccer_times = [290, 295, 280, 275, 300, 310, 295, 285, 290, 280]
tennis_times = [250, 255, 245, 260, 240, 265, 255, 250, 245, 255]
swimming_times = [310, 305, 300, 315, 310, 320, 305, 310, 300, 315]
archery_times = [280, 275, 270, 285, 265, 290, 275, 280, 275, 270]

# Assemble the data into a list
data = [basketball_times, soccer_times, tennis_times, swimming_times, archery_times]

# Define sports names
sports = ['Basketball', 'Soccer', 'Tennis', 'Swimming', 'Archery']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Create a custom color palette
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Plot the horizontal boxplot
box = ax.boxplot(data, vert=False, patch_artist=True, labels=sports, notch=True, whis=1.5)

# Customize each box with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, medians, and outliers
plt.setp(box['whiskers'], color='black', linewidth=1.5)
plt.setp(box['caps'], color='black', linewidth=1.5)
plt.setp(box['medians'], color='darkblue', linewidth=2)
plt.setp(box['fliers'], marker='o', color='red', alpha=0.5)

# Title and labels
ax.set_title("Cognitive Reaction Times Across Various Sports\nA Comparative Study", fontsize=14, weight='bold', color='darkred', pad=20)
ax.set_xlabel('Reaction Time (milliseconds)', fontsize=12, labelpad=15)
ax.set_ylabel('Sports', fontsize=12)

# Add gridlines
ax.grid(True, axis='x', linestyle='--', linewidth=0.7, color='gray', alpha=0.7)

# Add a legend for clarity
legend_handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(legend_handles, sports, title="Sports", loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, frameon=False)

# Automatically adjust layout to fit elements without overlap
plt.tight_layout()

# Display the plot
plt.show()