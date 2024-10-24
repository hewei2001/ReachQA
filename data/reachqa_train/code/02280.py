import matplotlib.pyplot as plt
import numpy as np

# Define the districts
districts = ['Residential', 'Commercial', 'Industrial', 'Cultural']

# Create and refine artificial energy consumption data for each district (in kWh)
data_residential = [320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520]
data_commercial = [510, 530, 550, 590, 610, 640, 670, 690, 730, 760, 790, 810]
data_industrial = [820, 850, 880, 900, 940, 980, 1020, 1050, 1100, 1150, 1180, 1200]
data_cultural = [200, 210, 230, 250, 270, 290, 310, 320, 330, 340, 350, 360]

# Combine the data into a list for the box plot
data = [data_residential, data_commercial, data_industrial, data_cultural]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))

# Customize the boxplot
box = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightgrey', color='darkblue', linewidth=1.5),
                 whiskerprops=dict(color='darkblue', linewidth=1.5),
                 capprops=dict(color='darkblue', linewidth=1.5),
                 medianprops=dict(color='red', linewidth=2),
                 flierprops=dict(marker='o', markerfacecolor='orange', markersize=5, linestyle='none'))

# Add color to the boxes for differentiation
colors = ['skyblue', 'lightgreen', 'salmon', 'gold']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set labels and title
ax.set_yticklabels(districts, fontsize=12, fontweight='bold')
ax.set_xlabel('Energy Consumption (kWh)', fontsize=12)
ax.set_title("The Symphony of Urban Life:\nEnergy Consumption Patterns in City Districts", 
             fontsize=16, fontweight='bold', loc='center', pad=20)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure no occlusion of text and labels
plt.tight_layout()

# Display the plot
plt.show()