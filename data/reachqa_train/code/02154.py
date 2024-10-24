import matplotlib.pyplot as plt
import numpy as np

# Define the years and cities
years = np.arange(2015, 2021)
cities = ['New York', 'London', 'Tokyo', 'Berlin', 'Sydney']

# Participation data for different types of gardens (number of participants)
# Each sublist represents data for a specific city in order of the years
community_gardens = [
    [250, 270, 290, 310, 330, 350],  # New York
    [200, 220, 240, 260, 280, 300],  # London
    [300, 320, 340, 360, 380, 400],  # Tokyo
    [180, 200, 220, 240, 260, 280],  # Berlin
    [210, 230, 250, 270, 290, 310]   # Sydney
]

school_gardens = [
    [100, 110, 120, 130, 140, 150],  # New York
    [90, 100, 110, 120, 130, 140],   # London
    [120, 130, 140, 150, 160, 170],  # Tokyo
    [80, 90, 100, 110, 120, 130],    # Berlin
    [110, 120, 130, 140, 150, 160]   # Sydney
]

rooftop_gardens = [
    [50, 60, 70, 80, 90, 100],       # New York
    [40, 50, 60, 70, 80, 90],        # London
    [70, 80, 90, 100, 110, 120],     # Tokyo
    [30, 40, 50, 60, 70, 80],        # Berlin
    [60, 70, 80, 90, 100, 110]       # Sydney
]

vertical_farms = [
    [20, 30, 40, 50, 60, 70],        # New York
    [30, 40, 50, 60, 70, 80],        # London
    [40, 50, 60, 70, 80, 90],        # Tokyo
    [25, 35, 45, 55, 65, 75],        # Berlin
    [35, 45, 55, 65, 75, 85]         # Sydney
]

# Stack the data
data = np.array([community_gardens, school_gardens, rooftop_gardens, vertical_farms])

# Define colors for each type of garden
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728']

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width for each city's data
bar_width = 0.15  

# Create a stacked bar chart for each city
for i, (city, city_data) in enumerate(zip(cities, data.transpose(1, 0, 2))):
    bottom = np.zeros(len(years))
    for category_data, color in zip(city_data, colors):
        ax.bar(years + i * bar_width, category_data, width=bar_width, bottom=bottom, color=color, edgecolor='w', label=city)
        bottom += category_data

# Set the chart title and labels
ax.set_title('Growing Green: Urban Gardening Participation\nfrom 2015 to 2020', fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Participants', fontsize=12)
ax.set_xticks(years + bar_width * 2)  # Center x-ticks on each group of bars
ax.set_xticklabels(years)
ax.set_xlim(2014.5, 2021)
ax.set_ylim(0, 700)

# Add the legend outside the plot
ax.legend(['Community Gardens', 'School Gardens', 'Rooftop Gardens', 'Vertical Farms'],
          loc='upper left', fontsize=10, title="Gardening Types", bbox_to_anchor=(1.05, 1))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()