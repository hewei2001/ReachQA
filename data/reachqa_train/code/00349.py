import matplotlib.pyplot as plt
import numpy as np

# Celestial bodies and their budget allocations
destinations = ['Mars', 'Europa', 'Titan', 'Asteroid Belt', 'Venus', 'Enceladus', 'Moon']
budget_allocation = [35, 20, 15, 10, 10, 5, 5]  # in percentage

# Estimated number of missions planned
missions = [10, 7, 5, 3, 3, 2, 1]

# Colors inspired by celestial body characteristics
colors = ['#FF5733', '#3498DB', '#9B59B6', '#E67E22', '#F39C12', '#85C1E9', '#F7DC6F']

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# ----- Pie Chart -----
# Explode the largest slice (Mars) to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0)
wedges, texts, autotexts = ax1.pie(
    budget_allocation,
    explode=explode,
    labels=destinations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    wedgeprops=dict(edgecolor='w')
)

# Style the autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Ensure pie chart is a circle
ax1.axis('equal')
ax1.set_title("Budget Distribution for\nGalactic Exploration Missions (2030-2040)", fontsize=14, fontweight='bold')

# ----- Bar Chart -----
x_pos = np.arange(len(destinations))
ax2.bar(x_pos, missions, color=colors, edgecolor='w')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(destinations, rotation=45, ha='right')
ax2.set_ylabel('Number of Planned Missions')
ax2.set_title('Projected Mission Count by Destination (2030-2040)', fontsize=12)

# Annotate bar chart with mission numbers
for i, v in enumerate(missions):
    ax2.text(x_pos[i], v + 0.3, str(v), color='black', ha='center', fontweight='bold')

# ----- Legend Configuration -----
legend_labels = [f"{destination}: {allocation}%" for destination, allocation in zip(destinations, budget_allocation)]
ax1.legend(legend_labels, title="Mission Budget Allocation", loc="center left", bbox_to_anchor=(0.9, -0.1), fontsize=10)

# Tight layout for better spacing and preventing overlap
plt.tight_layout()

# Display the plot
plt.show()