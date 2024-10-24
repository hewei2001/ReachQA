import matplotlib.pyplot as plt
import numpy as np

# Data
cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney', 'Beijing', 'Chicago', 'Mumbai', 'Seoul', 'Rio de Janeiro', 'Cairo']
modes = ['Public Transport', 'Private Cars', 'Cycling', 'Walking', 'Other']

# Data Values
data = [
    [32, 40, 8, 15, 5],
    [35, 28, 10, 17, 10],
    [50, 18, 6, 14, 12],
    [38, 27, 12, 13, 10],
    [22, 44, 12, 11, 11],
    [31, 32, 11, 15, 11],
    [27, 29, 13, 19, 12],
    [21, 33, 9, 15, 22],
    [36, 21, 8, 16, 19],
    [26, 31, 11, 19, 13],
    [29, 31, 10, 16, 14]
]

# Travel Times (in minutes)
travel_times = [
    [36, 21, 14, 31, 27],
    [26, 19, 11, 21, 19],
    [31, 26, 13, 26, 23],
    [21, 16, 11, 19, 16],
    [26, 21, 13, 23, 21],
    [31, 26, 14, 29, 26],
    [26, 21, 13, 23, 21],
    [21, 16, 11, 21, 19],
    [26, 19, 11, 23, 21],
    [31, 26, 14, 29, 26],
    [36, 21, 13, 26, 23]
]

# Colors
colors = ['#6495ED', '#FFC107', '#8BC34A', '#2196F3', '#FF9800']

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Stacked Bar Chart
bottom = np.zeros(len(cities))
for i, mode in enumerate(modes):
    ax1.bar(cities, [d[i] for d in data], bottom=bottom, label=mode, color=colors[i])
    bottom += np.array([d[i] for d in data])

# Set title, labels, and ticks for the first subplot
ax1.set_title("Transportation Mode Distribution in Major Cities", fontsize=14, y=1.05)
ax1.set_xlabel('City', fontsize=12)
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.set_xticks(np.arange(len(cities)))
ax1.set_xticklabels(cities, rotation=45, ha="right", fontsize=10)
ax1.set_ylim([0, 110])

# Add grid lines
ax1.yaxis.grid(True, linestyle='--', which='both', color='lightgrey', alpha=0.7)

# Add legend
ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=10, title='Transportation Mode')

# Add percentage labels
for i, city in enumerate(cities):
    cumulative = 0
    for j, mode in enumerate(modes):
        value = data[i][j]
        cumulative += value
        if value > 5:  # Only label segments with a significant size
            ax1.text(i, cumulative - value/2, f'{value}%', ha='center', va='center', fontsize=9, color='white' if value > 15 else 'black')

# Line Plot for Average Travel Times
avg_travel_times = [np.mean(t) for t in travel_times]
ax2.plot(cities, avg_travel_times, marker='o', color='blue', label='Average Travel Time')

# Set title, labels, and ticks for the second subplot
ax2.set_title('Average Travel Time by City', fontsize=14)
ax2.set_xlabel('City', fontsize=12)
ax2.set_ylabel('Travel Time (minutes)', fontsize=12)
ax2.set_xticks(np.arange(len(cities)))
ax2.set_xticklabels(cities, rotation=45, ha="right", fontsize=10)

# Add grid lines
ax2.yaxis.grid(True, linestyle='--', which='both', color='lightgrey', alpha=0.7)

# Add legend
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout
fig.tight_layout(rect=[0, 0, 1, 0.95])

# Show plot
plt.show()
