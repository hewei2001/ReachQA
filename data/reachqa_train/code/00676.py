import matplotlib.pyplot as plt
import numpy as np

# Define weight data for different types of medieval armor
chain_mail_weights = [10, 12, 11, 13, 14, 15, 13, 12, 11, 14]
plate_armor_weights = [25, 28, 27, 30, 29, 31, 32, 33, 30, 28]
scale_armor_weights = [20, 22, 21, 23, 24, 22, 20, 21, 23, 25]
brigandine_weights = [15, 17, 16, 18, 19, 18, 17, 16, 19, 20]

# Combine the data into a list for the boxplot
armor_data = [chain_mail_weights, plate_armor_weights, scale_armor_weights, brigandine_weights]

# Define armor types for labeling
armor_types = ["Chain Mail", "Plate Armor", "Scale Armor", "Brigandine Armor"]

# Create a horizontal boxplot
fig, ax = plt.subplots(figsize=(12, 7))

# Customize colors for each boxplot
colors = ['#D4A017', '#C0C0C0', '#8C7853', '#654321']

# Create the boxplot
bplot = ax.boxplot(armor_data, vert=False, patch_artist=True, 
                   notch=True, showmeans=True,
                   boxprops=dict(facecolor=colors[0], color='black'),
                   whiskerprops=dict(color='black'),
                   capprops=dict(color='black'),
                   medianprops=dict(color='red'),
                   meanprops=dict(marker='o', markerfacecolor='green', markeredgecolor='black', markersize=10),
                   flierprops=dict(marker='s', color='black', alpha=0.5))

# Set distinct colors for each category
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Add labels, title, and legend
ax.set_yticklabels(armor_types)
ax.set_xlabel('Weight (kg)', fontsize=12)
ax.set_title('Medieval Armor Weight Distribution\nA Study of Historical Warfare Gear', fontsize=16, fontweight='bold')

# Add grid lines for readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Annotations for additional insights
ax.annotate('Typical Weight Range', xy=(30, 2.5), xytext=(33, 3),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='blue')

# Adjust layout to avoid any overlap or cut-off
plt.tight_layout()

# Display the plot
plt.show()