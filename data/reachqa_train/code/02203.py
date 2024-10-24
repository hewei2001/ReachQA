import matplotlib.pyplot as plt
import numpy as np

# Define data for the number of successful space missions
entities = ['NASA', 'ESA', 'CNSA', 'SpaceX', 'ISRO']
years = ['2060', '2065', '2070', '2075', '2080']
missions_data = np.array([
    [15, 20, 25, 22, 30],  # NASA
    [10, 15, 18, 16, 20],  # ESA
    [12, 17, 22, 25, 28],  # CNSA
    [8, 14, 20, 24, 30],   # SpaceX
    [6, 12, 18, 20, 23]    # ISRO
])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Bar width and index for x-axis
bar_width = 0.15
index = np.arange(len(years))

# Colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each entity's data
for i, (entity, color) in enumerate(zip(entities, colors)):
    ax.bar(index + i * bar_width, missions_data[i], bar_width, label=entity, color=color)

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Successful Missions', fontsize=12)
ax.set_title('Race to the Stars:\nSuccessful Space Missions (2060-2080)', fontsize=16, fontweight='bold')
ax.set_xticks(index + bar_width * 2)
ax.set_xticklabels(years)
ax.legend(title='Organizations', fontsize=10)

# Add value labels on top of the bars
for i in range(len(entities)):
    for j in range(len(years)):
        ax.text(index[j] + i * bar_width, missions_data[i][j] + 0.5, 
                str(missions_data[i][j]), ha='center', va='bottom', fontsize=10)

# Improve layout and visibility
plt.tight_layout()

# Display the plot
plt.show()