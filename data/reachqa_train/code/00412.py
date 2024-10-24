import matplotlib.pyplot as plt
import numpy as np

# Adventure sports and their associated average adrenaline levels
sports = ["Skydiving", "Bungee Jumping", "White Water Rafting", 
          "Rock Climbing", "Mountain Biking", "Paragliding"]
adrenaline_levels = [95, 90, 85, 80, 75, 70]

# Create a horizontal bar chart
plt.figure(figsize=(12, 7))
colors = plt.cm.viridis(np.linspace(0, 1, len(sports)))
bars = plt.barh(sports, adrenaline_levels, color=colors, edgecolor='black')

# Add labels, title, and grid
plt.xlabel('Adrenaline Level (1-100)', fontsize=12)
plt.title('Thrill Factor: Adventure Sports Adrenaline Levels\nSurvey in Thrillville', 
          fontsize=16, fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Annotate each bar with the corresponding adrenaline level
for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width()}', va='center', ha='left', color='black', fontsize=10)

# Ensure category labels are centered with bars
plt.gca().invert_yaxis()  # Reverse the y-axis to have the highest adrenaline sports at the top
plt.yticks(fontsize=11)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()