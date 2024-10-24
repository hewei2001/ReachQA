import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data for leisure activities and hours spent per week
activities = [
    "Socializing with Friends/Family",
    "Exercising",
    "Watching TV/Streaming",
    "Reading",
    "Hobbies (e.g., Cooking, Art)",
    "Online Gaming",
    "Traveling (Short Trips)"
]
hours_spent = [8, 5, 10, 3, 6, 4, 2]

# Calculate percentages
total_hours = sum(hours_spent)
percentages = [h / total_hours * 100 for h in hours_spent]

# Create a color palette and gradient
colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(activities)))

# Creating the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal bars
bars = ax.barh(activities, hours_spent, color=colors, edgecolor='black', height=0.6)

# Set x-axis label and chart title with multi-line title
ax.set_xlabel("Average Hours per Week", fontsize=12)
ax.set_title("Balancing Acts:\nLeisure Time Distribution\nin a Modern Week", fontsize=16, pad=20)

# Add grid lines for readability with adjusted style
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Invert y-axis for top-to-bottom ordering
ax.invert_yaxis()

# Annotate the bars with the corresponding hours and percentages
for bar, hours, percentage in zip(bars, hours_spent, percentages):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
            f'{hours} hrs\n({percentage:.1f}%)', va='center', ha='left', fontsize=10, color='black')

# Add icons or patterns (representative symbols) - pseudo-representations via custom legend patches
patterns = ['/', '\\', '|', '-', '+', 'x', 'o']
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

# Create a custom legend for hatch patterns
legend_handles = [Patch(facecolor='grey', edgecolor='black', hatch=p, label=act) 
                  for act, p in zip(activities, patterns)]
ax.legend(handles=legend_handles, title='Activity Patterns', fontsize=10, title_fontsize=12)

# Enhance the font style of the y-tick labels
ax.set_yticklabels(activities, ha='right', fontsize=12, style='italic')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()