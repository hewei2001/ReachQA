import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patheffects import withStroke

# Define expanded phases of the project
phases = [
    'Initial Capital', 'Phase 1\nPlanning', 'Phase 2\nDigital Infrastructure', 
    'Phase 3\nStaff Hiring', 'Phase 4\nPilot Program', 'Phase 5\nCommunity Engagement', 
    'Phase 6\nFull-Scale Operation', 'Phase 7\nExpansion', 'Phase 8\nSustainability', 
    'Phase 9\nReview and Feedback', 'Phase 10\nInnovation Implementation'
]

# Define funding changes in million dollars with some additional complexity
funding_changes = np.array([50, 20, 30, -15, 25, -10, 40, 15, -5, 10, 35])

# Calculate cumulative values
cumulative_funds = np.cumsum(funding_changes)
initial_value = 0
cumulative_funds = np.insert(cumulative_funds, 0, initial_value)

# Define colors for the waterfall bars
colors = ['#2196F3'] + ['#4CAF50' if change >= 0 else '#FF5722' for change in funding_changes]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each phase as a bar in the waterfall
for i in range(1, len(cumulative_funds)):
    ax.bar(phases[i-1], cumulative_funds[i] - cumulative_funds[i-1], bottom=cumulative_funds[i-1],
           color=colors[i-1], edgecolor='black', width=0.5, zorder=3)
    ax.plot([i-1, i-1], [cumulative_funds[i-1], cumulative_funds[i]], color='black', linewidth=1.5, zorder=2)

# Annotate bars with their respective funding changes and cumulative values
for i, change in enumerate(funding_changes, 1):
    change_label = f'{change:+}M'
    ax.text(i-1, cumulative_funds[i-1] + change/2, change_label, ha='center', va='center', 
            color='white', fontsize=9, weight='bold', zorder=5)

# Add final cumulative value on top of the last bar
final_value_label = f'{cumulative_funds[-1]}M Total'
ax.text(len(phases) - 1, cumulative_funds[-1], final_value_label, ha='center', va='bottom', 
        color='black', fontsize=10, weight='bold')

# Add a baseline to denote the starting point
ax.axhline(y=initial_value, color='grey', linewidth=1.2, linestyle='--', zorder=1)

# Set titles and labels
plt.title("Comprehensive Analysis of Funding Evolution for the\nGreat Library Initiative", fontsize=16, weight='bold')
ax.set_ylabel('Cumulative Funding (Million $)', fontsize=12)

# Set x-ticks and rotate for better visibility
ax.set_xticks(range(len(phases)))
ax.set_xticklabels(phases, rotation=45, ha='right')

# Add gridlines for y-axis
ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, alpha=0.7, zorder=0)

# Enhance visual appeal with slight transparency for bars and shadow effects
for bar in ax.patches:
    bar.set_alpha(0.9)
    bar.set_path_effects([withStroke(linewidth=1, foreground='black')])

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()