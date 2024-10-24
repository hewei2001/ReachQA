import matplotlib.pyplot as plt
import numpy as np

# Define the years and milestones data
years = np.array([2060, 2070, 2080, 2090, 2100, 2110, 2120])
milestones = np.array([20, 45, 65, 90, 115, 135, 150])

# Define annotations for each milestone
annotations = [
    "First Manned Mission\nto Mars",
    "Discovery of a New\nElement on a Distant Moon",
    "Launch of the First\nInterstellar Probe",
    "Establishment of\nthe First Lunar Base",
    "Successful Terraforming\nExperiment on Mars",
    "Development of\nFaster-Than-Light Travel",
    "First Human Colony\nBeyond the Solar System"
]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(years, milestones, marker='o', linestyle='-', color='darkblue', linewidth=2.5, markersize=8)

# Annotate each milestone
for i, (year, milestone) in enumerate(zip(years, milestones)):
    ax.annotate(
        annotations[i],
        xy=(year, milestone),
        xytext=(-60, 20 if i % 2 == 0 else -40),  # Alternate annotation positions for readability
        textcoords='offset points',
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='gray'),
        fontsize=9, color='navy', fontweight='bold'
    )

# Set title and axis labels
ax.set_title('Chronicle of Astral Exploration:\nMilestones in Space Travel (2060-2120)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Milestone Impact Index', fontsize=12, labelpad=10)

# Add grid and customize ticks
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 161, 20))

# Set the limits for clarity
ax.set_xlim(2055, 2125)
ax.set_ylim(0, 160)

# Add a legend
ax.legend(['Milestone Impact Index'], loc='upper left', fontsize=11)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()