import matplotlib.pyplot as plt
import numpy as np

# Define the milestones
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
impacts = [100, 50, 30, 40, 60, 70, 80, 0]
cumulative = np.cumsum(impacts)

# Hypothetical annual budget (in billions) for space exploration
budgets = [18, 19, 20, 21, 24, 26, 29, 30]  # Fictional budget data

# Prepare waterfall steps
step_changes = np.zeros_like(impacts)
step_changes[1:] = cumulative[:-1]

# Set up figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Space Exploration Milestones and Budget Overview (2013-2023)", fontsize=16, fontweight='bold')

# Waterfall Chart
colors = ['#76c7c0' if val > 0 else '#ff6b6b' for val in impacts]
bars = ax1.bar(milestones, impacts, bottom=step_changes, color=colors, edgecolor='black')

# Connecting lines
for i in range(len(milestones) - 1):
    ax1.plot([i, i+1], [cumulative[i], cumulative[i]], 'k-', linewidth=1, alpha=0.7)

# Annotations for cumulative impacts
for bar, value in zip(bars, cumulative):
    ax1.annotate(f'{int(value)}', 
                 xy=(bar.get_x() + bar.get_width() / 2, bar.get_height() + bar.get_y()), 
                 xytext=(0, 3), 
                 textcoords='offset points',
                 ha='center', va='bottom', fontsize=10)

# Title and labels
ax1.set_title("Cumulative Progress Points", fontsize=14)
ax1.set_ylabel("Cumulative Impact")
ax1.set_xlabel("Milestones")
ax1.set_xticks(range(len(milestones)))
ax1.set_xticklabels(milestones, rotation=45, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)

# Budget Trend Line Chart
ax2.plot(milestones, budgets, marker='o', color='#ff5733', linestyle='-')

# Title and labels
ax2.set_title("Hypothetical Budget Trend", fontsize=14)
ax2.set_ylabel("Budget (in Billions)")
ax2.set_xlabel("Milestones")
ax2.set_xticks(range(len(milestones)))
ax2.set_xticklabels(milestones, rotation=45, ha='right')
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_axisbelow(True)

# Annotations for budget values
for i, budget in enumerate(budgets):
    ax2.annotate(f'{budget}', 
                 xy=(i, budget), 
                 xytext=(0, 5), 
                 textcoords='offset points',
                 ha='center', va='bottom', fontsize=10, color='#ff5733')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()