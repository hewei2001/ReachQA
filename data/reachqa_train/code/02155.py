import matplotlib.pyplot as plt
import numpy as np

# Original Data Setup
years = np.arange(2015, 2021)
cities = ['New York', 'London', 'Tokyo', 'Berlin', 'Sydney']

# Participation data (Original)
community_gardens = [
    [250, 270, 290, 310, 330, 350],
    [200, 220, 240, 260, 280, 300],
    [300, 320, 340, 360, 380, 400],
    [180, 200, 220, 240, 260, 280],
    [210, 230, 250, 270, 290, 310]
]
school_gardens = [
    [100, 110, 120, 130, 140, 150],
    [90, 100, 110, 120, 130, 140],
    [120, 130, 140, 150, 160, 170],
    [80, 90, 100, 110, 120, 130],
    [110, 120, 130, 140, 150, 160]
]
rooftop_gardens = [
    [50, 60, 70, 80, 90, 100],
    [40, 50, 60, 70, 80, 90],
    [70, 80, 90, 100, 110, 120],
    [30, 40, 50, 60, 70, 80],
    [60, 70, 80, 90, 100, 110]
]
vertical_farms = [
    [20, 30, 40, 50, 60, 70],
    [30, 40, 50, 60, 70, 80],
    [40, 50, 60, 70, 80, 90],
    [25, 35, 45, 55, 65, 75],
    [35, 45, 55, 65, 75, 85]
]

# New Hypothetical Dataset: Number of New Gardens Developed
new_gardens = [
    [10, 12, 14, 16, 18, 20],
    [8, 10, 12, 14, 16, 18],
    [15, 16, 17, 18, 19, 20],
    [7, 8, 9, 10, 11, 12],
    [9, 10, 11, 12, 13, 14]
]

# Stacking the data
data = np.array([community_gardens, school_gardens, rooftop_gardens, vertical_farms])

colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728']

# Create the main figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# Plotting the stacked bar chart on ax1
bar_width = 0.15
for i, (city, city_data) in enumerate(zip(cities, data.transpose(1, 0, 2))):
    bottom = np.zeros(len(years))
    for category_data, color in zip(city_data, colors):
        ax1.bar(years + i * bar_width, category_data, width=bar_width, bottom=bottom, color=color, edgecolor='w')
        bottom += category_data

# Set title and labels for the bar chart
ax1.set_title('Urban Gardening Participation Trends\n(2015-2020)', fontsize=14, fontweight='bold', loc='left')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Participants', fontsize=12)
ax1.set_xticks(years + bar_width * 2)
ax1.set_xticklabels(years)
ax1.set_xlim(2014.5, 2021)
ax1.set_ylim(0, 700)
ax1.legend(['Community Gardens', 'School Gardens', 'Rooftop Gardens', 'Vertical Farms'],
           loc='upper left', fontsize=10, title="Gardening Types", bbox_to_anchor=(1.05, 1))

# Plotting the line chart on ax2 for new gardens developed
for i, city in enumerate(cities):
    ax2.plot(years, new_gardens[i], marker='o', linestyle='-', label=city)

# Set title and labels for the line chart
ax2.set_title('Growth of New Urban Gardens\n(2015-2020)', fontsize=14, fontweight='bold', loc='left')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Number of New Gardens', fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years)
ax2.set_xlim(2015, 2020)
ax2.set_ylim(0, 25)
ax2.legend(loc='upper left', fontsize=10, title="Cities")

# Rotate x-axis labels for better readability
ax1.tick_params(axis='x', rotation=45)
ax2.tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()