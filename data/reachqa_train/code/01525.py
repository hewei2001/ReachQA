import matplotlib.pyplot as plt
import numpy as np

# Define commute times for each city
commute_data = {
    "New York": [30, 35, 40, 45, 55, 60, 65, 70, 75],
    "London": [20, 25, 30, 35, 40, 45, 50, 55],
    "Tokyo": [40, 42, 45, 47, 50, 52, 55, 58, 60],
    "Paris": [25, 30, 35, 40, 42, 45, 50, 55],
    "Sydney": [15, 20, 25, 30, 35, 40, 45]
}

# Convert data into a list format suitable for plotting
data = [commute_data[city] for city in commute_data]
cities = list(commute_data.keys())

# Compute average commute times for each city
average_commute_times = [np.mean(times) for times in data]

# Create the box plot with scatter overlay
plt.figure(figsize=(14, 8))
box = plt.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.6,
                  boxprops=dict(facecolor='lightblue', color='blue'),
                  whiskerprops=dict(color='darkblue'), capprops=dict(color='darkblue'),
                  medianprops=dict(color='darkred', linewidth=2))

# Colors for the boxes
colors = ['lightgreen', 'lightcoral', 'lightblue', 'lightsalmon', 'lightgoldenrodyellow']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding a scatter plot for individual data points
for i, city_data in enumerate(data, start=1):
    # Jitter x values slightly for clarity
    x_values = np.full(len(city_data), i) + np.random.normal(0, 0.04, size=len(city_data))
    plt.scatter(x_values, city_data, alpha=0.6, color='gray', edgecolor='k', label='Individual Data Points' if i == 1 else "")

# Adding a line plot for average commute times
plt.plot(range(1, len(cities) + 1), average_commute_times, color='darkgreen', marker='o', linestyle='-', linewidth=2, markersize=8, label='Average Commute Time')

# Customizing the plot
plt.title('Urban Commuter Insights:\nVariability and Distribution of Commute Times Across Major Cities', fontsize=16, weight='bold', pad=20)
plt.xlabel('Cities', fontsize=12)
plt.ylabel('Commute Time (Minutes)', fontsize=12)
plt.xticks(ticks=np.arange(1, len(commute_data) + 1), labels=cities, rotation=30)
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend
plt.legend(loc='upper left')

# Use tight_layout to automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()