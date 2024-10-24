import matplotlib.pyplot as plt
import numpy as np

# Data: Communication style preferences by cultural group
cultural_groups = ['American', 'British', 'Japanese', 'Indian', 'Brazilian']
communication_styles = ['Formal', 'Casual', 'Direct', 'Indirect', 'Humorous']

# Preferences percentages
preferences = np.array([
    [30, 25, 15, 20, 10],  # American
    [35, 20, 10, 25, 10],  # British
    [40, 15, 10, 30, 5],   # Japanese
    [25, 30, 15, 20, 10],  # Indian
    [20, 25, 20, 15, 20]   # Brazilian
])

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))

# Set a color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Accumulating bottom positions for stacked bars
bottoms = np.zeros(len(cultural_groups))

# Create stacked bar chart
for i, style in enumerate(communication_styles):
    ax.bar(cultural_groups, preferences[:, i], bottom=bottoms, color=colors[i], label=style)
    bottoms += preferences[:, i]

# Title and labels
ax.set_title("Cultural Language Preferences in Communication\nAmong College Students", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Percentage (%)", fontsize=14)
ax.set_xlabel("Cultural Group", fontsize=14)

# Add a legend
ax.legend(title="Communication Style", fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))

# Ensure y-axis is percentage based
ax.set_ylim(0, 100)

# Display percentage value on each segment
for i in range(len(cultural_groups)):
    for j in range(len(communication_styles)):
        plt.text(x=i, 
                 y=sum(preferences[i][:j]) + preferences[i][j] / 2, 
                 s=f'{preferences[i][j]}%', 
                 ha='center', 
                 va='center', 
                 color='white', 
                 fontweight='bold',
                 fontsize=10)

# Customize grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()