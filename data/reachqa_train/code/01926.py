import matplotlib.pyplot as plt
import numpy as np

# Define the cities and the number of vegetarian restaurants over the years
cities = ['New York', 'London', 'Tokyo', 'Berlin', 'Sydney']
years = ['2021', '2022', '2023']

# Number of vegetarian restaurants in each city over the years
veg_restaurants_data = {
    'New York': [150, 180, 210],
    'London': [130, 165, 200],
    'Tokyo': [90, 120, 150],
    'Berlin': [110, 145, 175],
    'Sydney': [100, 135, 170]
}

# New data for average restaurant ratings over the years in each city
restaurant_ratings_data = {
    'New York': [4.2, 4.3, 4.5],
    'London': [4.1, 4.2, 4.4],
    'Tokyo': [4.0, 4.1, 4.2],
    'Berlin': [3.9, 4.0, 4.2],
    'Sydney': [4.3, 4.4, 4.5]
}

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Set width of bar
bar_width = 0.15

# Set positions of bars on x-axis
indices = np.arange(len(years))

# Distinct colors for each city
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4']

# Plotting the bars for each city
for i, (city, color) in enumerate(zip(cities, colors)):
    offset = i * bar_width
    ax1.bar(indices + offset, veg_restaurants_data[city], width=bar_width, label=f'{city} Veg Restaurants', color=color)

# Adding labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Vegetarian Restaurants', fontsize=12)
ax1.set_title('The Rise of Plant-Based Dining:\nPopularity of Vegetarian Options and Restaurant Ratings Across Cities', fontsize=14, weight='bold')
ax1.set_xticks(indices + bar_width * 2)  # Centers the tick labels
ax1.set_xticklabels(years)

# Creating a twin axis for the line plot
ax2 = ax1.twinx()
ax2.set_ylabel('Average Restaurant Ratings', fontsize=12)

# Plotting the line chart
for city, color in zip(cities, colors):
    ax2.plot(indices, restaurant_ratings_data[city], color=color, linestyle='--', marker='o', label=f'{city} Ratings')

# Adding exact data value labels on top of each bar
for i, (city, color) in enumerate(zip(cities, colors)):
    for j, value in enumerate(veg_restaurants_data[city]):
        ax1.text(j + i * bar_width, value + 2, str(value), ha='center', va='bottom', fontsize=10, color=color)

# Adjusting the legend to avoid overlap
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left', bbox_to_anchor=(1.05, 1), title='Cities & Metrics')

# Adding grid for clarity
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.yaxis.grid(False)

# Automatically adjust the layout to prevent text from being cut off
plt.tight_layout()

# Display the chart
plt.show()