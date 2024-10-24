import matplotlib.pyplot as plt
import numpy as np

# Duration of missions in days for each space agency
nasa_missions = [15, 330, 12, 412, 22, 1000, 90, 7, 710, 73]
esa_missions = [7, 28, 60, 400, 450, 100, 500, 23, 730, 150]
roscosmos_missions = [6, 168, 1, 365, 720, 110, 180, 45, 15, 9]
cnsa_missions = [30, 90, 300, 14, 75, 40, 150, 110, 270, 365]
isro_missions = [2, 10, 4, 30, 365, 45, 180, 150, 14, 100]

# Compile data into a list
data = [nasa_missions, esa_missions, roscosmos_missions, cnsa_missions, isro_missions]
agency_names = ['NASA', 'ESA', 'Roscosmos', 'CNSA', 'ISRO']

# Create the box plot
plt.figure(figsize=(12, 8))
box_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
bp = plt.boxplot(data, patch_artist=True, notch=True, vert=True, whis=1.5)

# Set colors for each box
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

# Customize each component of the boxplot
plt.setp(bp['whiskers'], color='black', linestyle='--', linewidth=1.5)
plt.setp(bp['caps'], color='black', linewidth=1.5)
plt.setp(bp['medians'], color='darkred', linewidth=2)

# Customize plot
plt.xticks(np.arange(1, len(agency_names) + 1), agency_names, fontsize=11)
plt.ylabel('Mission Duration (Days)', fontsize=12)
plt.title('Exploring the Cosmos:\nMission Durations of Leading Space Agencies', fontsize=14, pad=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend manually using Line2D from matplotlib
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='w', markerfacecolor=box_colors[i], marker='s', markersize=10, label=agency_names[i])
                   for i in range(len(agency_names))]
plt.legend(handles=legend_elements, loc='upper right', title='Space Agencies', title_fontsize='11', fontsize=10)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Show the plot
plt.show()