import matplotlib.pyplot as plt
import numpy as np

# Original mission duration data (in months)
nasa_durations = [6, 18, 12, 9, 15, 24, 2, 10, 30, 3]
esa_durations = [4, 12, 20, 25, 8, 13, 5, 7, 22, 15]
roscosmos_durations = [7, 19, 14, 10, 11, 20, 8, 4, 17, 6]
cnsa_durations = [5, 15, 10, 18, 22, 7, 3, 6, 16, 12]
isro_durations = [3, 8, 14, 10, 9, 12, 5, 2, 13, 11]

# Compile data for boxplot
data = [nasa_durations, esa_durations, roscosmos_durations, cnsa_durations, isro_durations]

# Define the names of the space agencies
agencies = ['NASA', 'ESA', 'Roscosmos', 'CNSA', 'ISRO']

# Constructing average mission durations for a line plot
# These values are related but differ from the box plot data
average_durations = [np.mean(nasa_durations),
                     np.mean(esa_durations),
                     np.mean(roscosmos_durations),
                     np.mean(cnsa_durations),
                     np.mean(isro_durations)]

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Create the box plot
box = ax.boxplot(data, vert=True, patch_artist=True, labels=agencies, notch=True)

# Customize the box plot
colors = ['#FF6347', '#8B0000', '#4682B4', '#32CD32', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set(facecolor=color, alpha=0.7)
plt.setp(box['whiskers'], color='gray', linestyle='--')
plt.setp(box['caps'], color='black')
plt.setp(box['medians'], color='yellow', linewidth=2)

# Overlay line plot for average mission durations
ax.plot(agencies, average_durations, color='black', marker='o', linestyle='-', linewidth=2, label='Average Duration')

# Set titles and labels
ax.set_title('Space Exploration Mission Durations (2010-2020)\nBox Plot and Average Duration Line', fontsize=14, fontweight='bold')
ax.set_ylabel('Mission Duration (Months)')
ax.set_xlabel('Space Agency')

# Add grid
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Legend handling
color_lines = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(color_lines + [plt.Line2D([0], [0], color='black', lw=2, marker='o')],
          agencies + ['Average Duration'], title='Legend', loc='upper right', fontsize=10, frameon=False)

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()