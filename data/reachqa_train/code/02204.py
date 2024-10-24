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

# Calculate cumulative missions over years
cumulative_missions = np.sum(missions_data, axis=0)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar width and index for x-axis
bar_width = 0.15
index = np.arange(len(years))

# Colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each entity's data
for i, (entity, color) in enumerate(zip(entities, colors)):
    ax1.bar(index + i * bar_width, missions_data[i], bar_width, label=entity, color=color)

# Create a secondary y-axis for the line plot
ax2 = ax1.twinx()

# Plot cumulative successful missions as a line plot
ax2.plot(index + bar_width * 2, cumulative_missions, color='black', linestyle='--', marker='o', label='Cumulative Missions', linewidth=2)

# Set labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Successful Missions', fontsize=12)
ax2.set_ylabel('Cumulative Missions', fontsize=12)
ax1.set_title('Race to the Stars:\nSuccessful and Cumulative Space Missions (2060-2080)', fontsize=16, fontweight='bold')
ax1.set_xticks(index + bar_width * 2)
ax1.set_xticklabels(years)

# Add value labels on top of the bars
for i in range(len(entities)):
    for j in range(len(years)):
        ax1.text(index[j] + i * bar_width, missions_data[i][j] + 0.5, 
                 str(missions_data[i][j]), ha='center', va='bottom', fontsize=10)

# Add markers for cumulative data points
for i, cum_val in enumerate(cumulative_missions):
    ax2.text(index[i] + bar_width * 2, cum_val + 0.5, str(cum_val), ha='center', va='bottom', fontsize=10, color='black')

# Combine legends from both plots
bars_legend = ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Organizations', fontsize=10)
line_legend = ax2.legend(loc='upper left', bbox_to_anchor=(1, 0.9), fontsize=10)
ax1.add_artist(bars_legend)

# Improve layout and visibility
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()