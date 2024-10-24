import matplotlib.pyplot as plt
import numpy as np

# Extend the decades and transportation modes data
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s', '2030s', '2040s']
cars = [120, 170, 150, 140, 120, 100, 60, 40, 25]
buses = [30, 45, 50, 60, 70, 80, 90, 100, 110]
bicycles = [2, 3, 5, 10, 20, 35, 50, 65, 80]
trains = [15, 20, 30, 40, 50, 60, 70, 80, 90]
electric_scooters = [0, 0, 0, 0, 0, 10, 30, 50, 70]
motorcycles = [10, 15, 25, 30, 40, 45, 55, 70, 90]
shared_vehicles = [0, 0, 0, 10, 25, 50, 75, 100, 120]
high_speed_trains = [0, 0, 0, 0, 0, 0, 15, 30, 50]

# Set positions and width for the bars
barWidth = 0.55
r = np.arange(len(decades))

# Set a color palette
colors = ['#FF5733', '#FFC300', '#DAF7A6', '#900C3F', '#1F618D', '#D35400', '#8E44AD', '#16A085']

# Create the stacked bar chart
plt.figure(figsize=(14, 9))

# Plot each bar layer on top of the previous ones
plt.bar(r, cars, color=colors[0], edgecolor='grey', width=barWidth, label='Cars')
plt.bar(r, buses, bottom=np.array(cars), color=colors[1], edgecolor='grey', width=barWidth, label='Buses')
plt.bar(r, bicycles, bottom=np.array(cars) + np.array(buses), color=colors[2], edgecolor='grey', width=barWidth, label='Bicycles')
plt.bar(r, trains, bottom=np.array(cars) + np.array(buses) + np.array(bicycles), color=colors[3], edgecolor='grey', width=barWidth, label='Trains')
plt.bar(r, electric_scooters, bottom=np.array(cars) + np.array(buses) + np.array(bicycles) + np.array(trains), color=colors[4], edgecolor='grey', width=barWidth, label='Electric Scooters')
plt.bar(r, motorcycles, bottom=np.array(cars) + np.array(buses) + np.array(bicycles) + np.array(trains) + np.array(electric_scooters), color=colors[5], edgecolor='grey', width=barWidth, label='Motorcycles')
plt.bar(r, shared_vehicles, bottom=np.array(cars) + np.array(buses) + np.array(bicycles) + np.array(trains) + np.array(electric_scooters) + np.array(motorcycles), color=colors[6], edgecolor='grey', width=barWidth, label='Shared Vehicles')
plt.bar(r, high_speed_trains, bottom=np.array(cars) + np.array(buses) + np.array(bicycles) + np.array(trains) + np.array(electric_scooters) + np.array(motorcycles) + np.array(shared_vehicles), color=colors[7], edgecolor='grey', width=barWidth, label='High Speed Trains')

# Add title and labels with careful line breaks
plt.title('The Evolution of Transportation Modes\nin Transopolis (1960-2040)', fontsize=16, pad=20)
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Number of Trips (Millions)', fontsize=12)
plt.xticks(r, decades, rotation=45)

# Add a legend and adjust its position
plt.legend(loc='upper left', fontsize=10, title='Transport Modes', bbox_to_anchor=(1, 1))

# Enhance readability with gridlines
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.88, 1])

# Display the plot
plt.show()