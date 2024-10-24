import matplotlib.pyplot as plt
import numpy as np

# Define character names and number of fan clubs
characters = ['Starblade', 'Mystifire', 'Voidstrider', 'Floraheart', 'Timeweaver', 'Shadowwhisper']
fan_clubs = [85, 95, 70, 60, 80, 75]

# Construct a related dataset for overlay (e.g., average age of fan club members)
avg_ages = [28, 25, 30, 35, 32, 29]

# Create a bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Primary plot: Bar chart for fan clubs
bars = ax1.bar(characters, fan_clubs, color=['#4682b4', '#ff6347', '#6b8e23', '#da70d6', '#ffb6c1', '#20b2aa'], width=0.6, label='Number of Fan Clubs')

# Annotate each bar with the number of fan clubs
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Set labels and title for primary y-axis
ax1.set_xlabel('Characters', fontsize=12, fontweight='bold')
ax1.set_ylabel('Number of Fan Clubs', fontsize=12, fontweight='bold', color='navy')
ax1.set_title('Character Popularity in Cosmiconia\nFan Clubs and Average Ages', fontsize=14, fontweight='bold')

# Customize the x-axis ticks
plt.xticks(rotation=45, ha='right', fontsize=10)

# Define y-axis ticks for fan clubs
ax1.set_yticks(np.arange(0, 101, 10))
ax1.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)

# Secondary plot: Line plot for average ages
ax2 = ax1.twinx()  # Create a second y-axis
ax2.plot(characters, avg_ages, color='orange', marker='o', linestyle='-', linewidth=2, markersize=8, label='Average Age')
ax2.set_ylabel('Average Age of Fan Club Members', fontsize=12, fontweight='bold', color='orange')
ax2.set_yticks(np.arange(24, 40, 2))

# Add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), bbox_transform=ax1.transAxes)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()