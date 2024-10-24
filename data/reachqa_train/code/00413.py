import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Adventure sports and their associated average adrenaline levels
sports = ["Skydiving", "Bungee Jumping", "White Water Rafting", 
          "Rock Climbing", "Mountain Biking", "Paragliding"]
adrenaline_levels = [95, 90, 85, 80, 75, 70]

# Create a figure with customized size
plt.figure(figsize=(14, 8))

# Create a gradient color map
colors = plt.cm.viridis(np.linspace(0, 1, len(sports)))

# Custom pattern styles
patterns = ['/', '\\', '|', '-', '+', 'x']

# Create horizontal bars with gradients
bars = plt.barh(sports, adrenaline_levels, color=colors, edgecolor='black', hatch='/', height=0.6)

# Add a gradient background
plt.gca().set_facecolor('#f0f0f0')
plt.gca().set_axisbelow(True)

# Add labels, title, and grid
plt.xlabel('Adrenaline Level (1-100)', fontsize=12, weight='bold')
plt.title('Thrill Factor: Adventure Sports Adrenaline Levels\nSurvey in Thrillville', 
          fontsize=16, fontweight='bold', loc='left')
plt.grid(axis='x', linestyle='--', alpha=0.5, color='gray')

# Annotate each bar with the corresponding adrenaline level and an emoji
for bar, pattern in zip(bars, patterns):
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width()} ⚡', va='center', ha='left', color='black', fontsize=11)
    bar.set_hatch(pattern)  # Apply unique pattern to each bar

# Invert y-axis for ranking purposes
plt.gca().invert_yaxis()
plt.yticks(fontsize=11)

# Pie chart as an inset to show distribution
ax_inset = plt.gcf().add_axes([0.75, 0.15, 0.2, 0.2])
ax_inset.pie(adrenaline_levels, labels=sports, colors=colors, startangle=140, autopct='%1.1f%%')
ax_inset.set_title('Adrenaline Distribution', fontsize=10, weight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()