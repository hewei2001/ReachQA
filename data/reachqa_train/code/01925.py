import matplotlib.pyplot as plt
import numpy as np

# Define the cities and the number of vegetarian restaurants over the years
cities = ['New York', 'London', 'Tokyo', 'Berlin', 'Sydney']
years = ['2021', '2022', '2023']

# Number of vegetarian restaurants in each city over the years
data = {
    'New York': [150, 180, 210],
    'London': [130, 165, 200],
    'Tokyo': [90, 120, 150],
    'Berlin': [110, 145, 175],
    'Sydney': [100, 135, 170]
}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Set width of bar
bar_width = 0.15

# Set positions of bars on x-axis
indices = np.arange(len(years))

# Distinct colors for each city
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4']

# Plotting the bars for each city
for i, (city, color) in enumerate(zip(cities, colors)):
    offset = i * bar_width
    ax.bar(indices + offset, data[city], width=bar_width, label=city, color=color)

# Adding labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Vegetarian Restaurants', fontsize=12)
ax.set_title('The Rise of Plant-Based Dining:\nPopularity of Vegetarian Options Across Cities', fontsize=14, weight='bold')
ax.set_xticks(indices + bar_width * 2)  # Centers the tick labels
ax.set_xticklabels(years)
ax.legend(title='Cities', loc='upper left')

# Adding exact data value labels on top of each bar
for i, (city, color) in enumerate(zip(cities, colors)):
    for j, value in enumerate(data[city]):
        ax.text(j + i * bar_width, value + 2, str(value), ha='center', va='bottom', fontsize=10, color=color)

# Adding grid for clarity
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent text from being cut off
plt.tight_layout()

# Display the bar chart
plt.show()