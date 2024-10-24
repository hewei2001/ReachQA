import numpy as np
import matplotlib.pyplot as plt

# Extended time range with fictional data
decades = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s', '2030s']

# Number of missions (fictional) for each category per decade
manned_missions = np.array([1, 2, 10, 15, 20, 30, 40, 35, 40])
unmanned_missions = np.array([5, 10, 25, 30, 25, 40, 60, 55, 60])
deep_space_missions = np.array([0, 1, 2, 5, 8, 15, 25, 30, 35])
orbital_missions = np.array([3, 5, 15, 20, 30, 50, 70, 65, 80])
interplanetary_missions = np.array([0, 0, 1, 2, 5, 10, 15, 25, 40])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each category of missions with distinct styles and stacked lines
ax.plot(decades, manned_missions, label='Manned Missions', color='blue', marker='o', linestyle='-', linewidth=2)
ax.plot(decades, unmanned_missions, label='Unmanned Missions', color='green', marker='s', linestyle='--', linewidth=2)
ax.plot(decades, deep_space_missions, label='Deep Space Missions', color='purple', marker='^', linestyle='-.', linewidth=2)
ax.plot(decades, orbital_missions, label='Orbital Missions', color='orange', marker='x', linestyle='-', linewidth=2)
ax.plot(decades, interplanetary_missions, label='Interplanetary Missions', color='red', marker='D', linestyle=':', linewidth=2)

# Annotate significant milestones
ax.annotate('First Moon Landing', xy=('1960s', 2), xytext=('1970s', 12),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkred')
ax.annotate('Mars Rover Launch', xy=('2010s', 25), xytext=('2000s', 18),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkgreen')
ax.annotate('Exponential Growth', xy=('2020s', 30), xytext=('1990s', 50),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkblue')

# Add titles and labels
ax.set_title('Evolution of Space Exploration Missions:\nA Journey Across Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Number of Space Missions (Log Scale)', fontsize=12)
ax.set_yscale('log')
ax.legend(loc='upper left', fontsize=10, title='Mission Categories', frameon=False)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Customize x-ticks and y-ticks
plt.xticks(rotation=45)
plt.yticks([1, 10, 100], ['1', '10', '100'])

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the line chart
plt.show()