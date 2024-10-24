import matplotlib.pyplot as plt
import numpy as np

# Data: Percentage allocations of space exploration missions by destination
labels = ['Moon', 'Mars', 'Jupiter', 'Saturn', 'Outer Space']
missions = [25, 35, 10, 10, 20]
costs = [50, 150, 80, 70, 120]  # Hypothetical average annual cost in millions for each destination

# Colors for each segment in the pie chart
colors = ['#FFD700', '#FF6347', '#8A2BE2', '#4682B4', '#32CD32']

# Create the figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 3]})

# Pie Chart
wedges, texts, autotexts = ax[0].pie(
    missions,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=(0.1, 0, 0, 0, 0.1),
    shadow=True
)

for text in texts:
    text.set_fontsize(9)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax[0].set_title("Allocation of Space Exploration Missions\nby Destination (2023-2033)", fontsize=14, fontweight='bold', pad=20)
ax[0].legend(wedges, labels, title="Destinations", loc="upper left", bbox_to_anchor=(0.9, 1))

# Bar Chart
bar_width = 0.5
x_pos = np.arange(len(labels))
ax[1].bar(x_pos, costs, color=colors, width=bar_width, edgecolor='grey')

ax[1].set_title("Average Annual Cost of Missions\nby Destination (in Millions)", fontsize=14, fontweight='bold', pad=20)
ax[1].set_xticks(x_pos)
ax[1].set_xticklabels(labels)
ax[1].set_ylabel('Cost (in Millions)')
ax[1].grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels to bar chart
for i, cost in enumerate(costs):
    ax[1].text(i, cost + 5, f"${cost}", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Display the combined plot
plt.show()