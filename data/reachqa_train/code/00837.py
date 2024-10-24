import numpy as np
import matplotlib.pyplot as plt

# Decades for the timeline
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Number of missions (fictional) for each category per decade
manned_missions = np.array([2, 10, 15, 20, 30, 40, 35])
unmanned_missions = np.array([10, 25, 30, 25, 40, 60, 55])
deep_space_missions = np.array([1, 2, 5, 8, 15, 25, 30])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot each category of missions with distinct styles
ax.plot(decades, manned_missions, label='Manned Missions', color='blue', marker='o', linestyle='-', linewidth=2)
ax.plot(decades, unmanned_missions, label='Unmanned Missions', color='green', marker='s', linestyle='--', linewidth=2)
ax.plot(decades, deep_space_missions, label='Deep Space Missions', color='purple', marker='^', linestyle='-.', linewidth=2)

# Annotate significant milestones
ax.annotate('First Moon Landing', xy=('1960s', 2), xytext=('1970s', 10),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkred')
ax.annotate('Mars Rover Launch', xy=('2010s', 25), xytext=('2000s', 20),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkgreen')

# Adding titles and labels
ax.set_title('Space Exploration Milestones:\nHumanity\'s Reach Beyond Earth', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Number of Space Missions', fontsize=12)
ax.legend(loc='upper left', fontsize=10, title='Mission Categories', frameon=False)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Customize x-ticks and y-ticks for better appearance
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 71, 10))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the line chart
plt.show()