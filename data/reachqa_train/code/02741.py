import matplotlib.pyplot as plt
import numpy as np

# Define character names and number of fan clubs
characters = ['Starblade', 'Mystifire', 'Voidstrider', 'Floraheart', 'Timeweaver', 'Shadowwhisper']
fan_clubs = [85, 95, 70, 60, 80, 75]

# Create a bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(characters, fan_clubs, color=['#4682b4', '#ff6347', '#6b8e23', '#da70d6', '#ffb6c1', '#20b2aa'], width=0.6)

# Annotate each bar with the number of fan clubs
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the axes
ax.set_xlabel('Characters', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Fan Clubs', fontsize=12, fontweight='bold')
ax.set_title('Character Popularity in Cosmiconia\nNumber of Fan Clubs per Character', fontsize=14, fontweight='bold')

# Customize the x-axis ticks
plt.xticks(rotation=45, ha='right', fontsize=10)

# Define y-axis ticks
plt.yticks(np.arange(0, 101, 10))

# Add grid lines for y-axis
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()