import matplotlib.pyplot as plt
import numpy as np

# Extended data for 15 years (2008 to 2023)
years = np.arange(2008, 2023)

# Hypothetical data (in thousands of trips per year)
bicycles = [20, 25, 30, 35, 40, 50, 60, 70, 85, 100, 120, 150, 185, 225, 270]
electric_scooters = [0, 0, 0, 5, 10, 15, 30, 45, 60, 80, 105, 135, 170, 210, 250]
electric_buses = [60, 65, 70, 75, 80, 85, 90, 100, 110, 125, 145, 170, 200, 235, 270]
pedestrian_pathways = [25, 27, 30, 32, 35, 40, 50, 60, 75, 90, 110, 135, 160, 190, 220]
electric_cars = [0, 0, 10, 20, 30, 40, 50, 60, 75, 95, 115, 140, 170, 205, 245]
autonomous_shuttles = [0, 0, 0, 0, 0, 10, 20, 30, 50, 70, 95, 120, 150, 185, 220]

# Stack the data for the stacked bar chart
transport_data = np.vstack([bicycles, electric_scooters, electric_buses, pedestrian_pathways, electric_cars, autonomous_shuttles])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.5
indices = np.arange(len(years))

# Plot each stack with unique colors
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']
labels = ['Bicycles', 'Electric Scooters', 'Electric Buses', 'Pedestrian Pathways', 'Electric Cars', 'Autonomous Shuttles']

bottom_stack = np.zeros(len(years))

for i, (data, color, label) in enumerate(zip(transport_data, colors, labels)):
    ax.bar(indices, data, bar_width, bottom=bottom_stack, label=label, color=color, edgecolor='black', alpha=0.85)
    bottom_stack += data

# Add titles and labels
ax.set_title("Evolution of Eco-Friendly Transportation Modes\nin Urban Areas (2008-2023): A Comprehensive Analysis", fontsize=14, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Trips (in thousands)", fontsize=12)

# Customize the x-axis and y-axis
ax.set_xticks(indices)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(0, 1001, 100))

# Add a legend
ax.legend(loc='upper left', frameon=False, fontsize=10)

# Add gridlines for better readability
ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate key points
ax.annotate('Electric Scooters Growth', xy=(7, 120), xytext=(9, 300),
            arrowprops=dict(facecolor='grey', arrowstyle='->', linewidth=1.5),
            fontsize=9, color='black')

ax.annotate('Emergence of Autonomous\nShuttles', xy=(11, 410), xytext=(13, 650),
            arrowprops=dict(facecolor='grey', arrowstyle='->', linewidth=1.5),
            fontsize=9, color='black')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()