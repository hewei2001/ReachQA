import matplotlib.pyplot as plt
import numpy as np

# Define the milestones and their impacts on space exploration
milestones = [
    "Baseline 2013",
    "NASA's Mars Rover 2014",
    "ESA Rosetta 2015",
    "CNSA Lunar 2016",
    "Private Crew Launch 2020",
    "Perseverance Mars 2021",
    "James Webb Telescope 2021",
    "Current Status 2023"
]

# Impacts of each milestone
impacts = [
    100,  # Initial baseline
    50,   # Mars Rover
    30,   # Rosetta
    40,   # Lunar success
    60,   # Private crew launch
    70,   # Perseverance rover
    80,   # James Webb Telescope
    0     # Final status in 2023
]

# Calculate cumulative impacts
cumulative = np.cumsum(impacts)

# Prepare waterfall steps
step_changes = np.zeros_like(impacts)
step_changes[1:] = cumulative[:-1]

# Determine bar colors
colors = ['#76c7c0' if val > 0 else '#ff6b6b' for val in impacts]

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the waterfall chart
bars = ax.bar(milestones, impacts, bottom=step_changes, color=colors, edgecolor='black')

# Draw connecting lines
for i in range(len(milestones) - 1):
    ax.plot([i, i+1], [cumulative[i], cumulative[i]], 'k-', linewidth=1, alpha=0.7)

# Title and axis labels
ax.set_title("Key Achievements in Space Exploration (2013-2023)", fontsize=16, fontweight='bold')
ax.set_ylabel("Cumulative Progress Points", fontsize=12)
ax.set_xlabel("Milestones", fontsize=12)

# Annotate bars with impact values
for bar, value in zip(bars, cumulative):
    ax.annotate(f'{int(value)}', 
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_height() + bar.get_y()), 
                xytext=(0, 3), 
                textcoords='offset points',
                ha='center', 
                va='bottom',
                fontsize=10)

# Adjust layout
plt.xticks(rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)
plt.tight_layout()

# Display the plot
plt.show()