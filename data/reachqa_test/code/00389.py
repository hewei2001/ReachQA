import matplotlib.pyplot as plt
import numpy as np

# Define the cities
cities = ['Tokyo', 'New York City', 'London', 'Paris', 'Beijing']

# Define the years
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

# Define the electric vehicle registration data (in thousands) for each city and year
ev_data = np.array([
    [5, 8, 12, 18, 25, 35, 45, 60],  # Tokyo
    [2, 4, 6, 10, 15, 20, 28, 40],  # New York City
    [3, 5, 8, 12, 18, 25, 35, 50],  # London
    [2, 4, 6, 10, 15, 20, 25, 35],  # Paris
    [5, 8, 12, 20, 30, 40, 55, 70]   # Beijing
])

# Calculate the total electric vehicle registrations for each city
total_ev_data = np.sum(ev_data, axis=1)

# Create a figure and axes
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# Define distinct colors and line styles for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
linestyles = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]

# Plot the electric vehicle registration data (line plot)
ax = axs[0]
for i, (city, color, linestyle) in enumerate(zip(cities, colors, linestyles)):
    ax.plot(years, ev_data[i], label=city, color=color, linestyle=linestyle, linewidth=2, marker='o')

# Set the title and labels for the line plot
ax.set_title("Electric Vehicle Adoption in Major Cities Around the World\n"
            "(Number of Registered Electric Vehicles in Thousands)")
ax.set_xlabel('Year')
ax.set_ylabel('Number of Registered Electric Vehicles (Thousands)')

# Add a grid to facilitate the estimation of values
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend to identify different lines
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Label each data point on the line
for i, (city, data) in enumerate(zip(cities, ev_data)):
    for j, (year, value) in enumerate(zip(years, data)):
        ax.annotate(str(value), xy=(year, value), xytext=(0, 5), textcoords='offset points', ha='center')

# Plot the total electric vehicle registrations for each city (bar chart)
ax = axs[1]
ax.bar(cities, total_ev_data, color=colors)

# Set the title and labels for the bar chart
ax.set_title("Total Electric Vehicle Registrations by City")
ax.set_xlabel('City')
ax.set_ylabel('Total Number of Registered Electric Vehicles (Thousands)')

# Rotate the x-axis labels for better readability
ax.tick_params(axis='x', labelrotation=45)

# Add a grid to facilitate the estimation of values
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the layout to avoid occlusion
plt.tight_layout(rect=[0, 0, 1, 1])

# Show the plot
plt.show()