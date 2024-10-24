import matplotlib.pyplot as plt
import numpy as np

# Data for mythical creatures and their abilities
creatures = ['Dragon', 'Phoenix', 'Unicorn', 'Griffin', 'Mermaid']
strength = [95, 70, 60, 85, 50]
speed = [80, 90, 65, 75, 60]
intelligence = [90, 85, 80, 70, 95]
magic = [100, 85, 75, 80, 90]

# Calculate total power levels for each creature
total_power = np.array(strength) + np.array(speed) + np.array(intelligence) + np.array(magic)

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars for each creature
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231']
bars = ax.barh(creatures, total_power, color=colors, edgecolor='black', height=0.5)

# Annotate each bar with the total power level
for bar in bars:
    ax.annotate(f'{bar.get_width()}',
                xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # offset text slightly for better visibility
                textcoords='offset points',
                ha='left', va='center',
                fontsize=12)

# Set title and axis labels
ax.set_title('Power Levels of Mythical Creatures\nin the Realm of Eldoria', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Total Power Level', fontsize=12)
ax.set_ylabel('Mythical Creature', fontsize=12)

# Add grid lines for improved readability
ax.xaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Improve layout and visibility
plt.tight_layout()

# Display the plot
plt.show()