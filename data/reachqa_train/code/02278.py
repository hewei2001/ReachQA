import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the years and milestones data
years = np.array([2060, 2070, 2080, 2090, 2100, 2110, 2120])
milestones = np.array([20, 45, 65, 90, 115, 135, 150])

# Construct additional data for projected budget
projected_budget = np.array([30, 60, 80, 95, 120, 140, 170])

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

# Plot the milestones with a color gradient
colors = plt.cm.viridis(np.linspace(0, 1, len(years)))
for i in range(len(years) - 1):
    ax.plot(years[i:i+2], milestones[i:i+2], color=colors[i], linewidth=3, marker='o', markersize=8)
    
# Plot the projected budget
ax.plot(years, projected_budget, linestyle='--', color='orange', linewidth=2, marker='s', markersize=6, alpha=0.8)

# Annotate each milestone
for i, (year, milestone) in enumerate(zip(years, milestones)):
    ax.annotate(
        annotations[i],
        xy=(year, milestone),
        xytext=(-70, 25 if i % 2 == 0 else -45),
        textcoords='offset points',
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='gray'),
        fontsize=9, color='navy', fontweight='bold'
    )

# Set title and axis labels with a multi-line title
ax.set_title('Chronicle of Astral Exploration:\nMilestones in Space Travel (2060-2120)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Milestone/Budget Index', fontsize=12, labelpad=10)

# Add background shading for eras
ax.axvspan(2060, 2080, color='lavender', alpha=0.3, label='Era of Initial Expansion')
ax.axvspan(2080, 2100, color='lightcyan', alpha=0.3, label='Era of Technological Breakthrough')

# Add grid
ax.grid(True, linestyle='--', alpha=0.6)

# Set ticks with rotation for visibility
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 181, 20))

# Set the limits for clarity
ax.set_xlim(2055, 2125)
ax.set_ylim(0, 180)

# Create a legend
milestone_legend = mpatches.Patch(color='blue', label='Milestone Impact Index')
budget_legend = mpatches.Patch(color='orange', label='Projected Budget')
ax.legend(handles=[milestone_legend, budget_legend], loc='upper left', fontsize=11)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()