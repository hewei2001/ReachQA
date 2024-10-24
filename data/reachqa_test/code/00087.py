import matplotlib.pyplot as plt
import numpy as np

# Original milestone data
years = np.array([1957, 1961, 1969, 1981, 1998, 2012, 2021])
milestones_score = np.array([10, 20, 40, 25, 30, 35, 45])

# Related but different data: hypothetical funding in billion USD
funding = np.array([1.2, 1.5, 2.1, 3.8, 4.5, 6.3, 8.0])

# Annotations for milestones
annotations = [
    "Sputnik 1: First artificial satellite",
    "Yuri Gagarin: First human in space",
    "Apollo 11: First Moon landing",
    "Columbia: First Space Shuttle flight",
    "ISS: Start of International Space Station",
    "Curiosity: Rover lands on Mars",
    "James Webb: Space telescope launched"
]

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the milestone significance as a line plot
ax1.plot(years, milestones_score, marker='o', linestyle='-', color='blue', markersize=8, linewidth=2, label='Significance Score')

# Overlay a bar chart for the funding data
ax2 = ax1.twinx()
ax2.bar(years, funding, width=0.5, alpha=0.4, color='orange', label='Funding (in billion USD)')

# Annotate each milestone
for (x, y, label) in zip(years, milestones_score, annotations):
    ax1.annotate(label, (x, y), textcoords="offset points", xytext=(-85, 10 if y % 20 == 0 else -20), ha='center', fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='gray', lw=1.5), bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white', alpha=0.8))

# Titles and labels
ax1.set_title("The Evolution of Space Exploration Milestones and Funding\n(1957 - 2021)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Significance Score", fontsize=12)
ax2.set_ylabel("Funding (in billion USD)", fontsize=12)

# Setting ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(range(0, 51, 10))
ax2.set_yticks(np.arange(0, 9, 1))

# Grid and legends
ax1.grid(visible=True, linestyle='--', alpha=0.7)
fig.tight_layout()

# Add legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left')

# Display the plot
plt.show()