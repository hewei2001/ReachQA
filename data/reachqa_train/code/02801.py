import matplotlib.pyplot as plt
import numpy as np

# Define cities and the number of AI-driven food delivery robots deployed in each city for 2030
cities = ['Tokyo', 'New York', 'London', 'Shanghai', 'Berlin', 'Sydney', 'Mumbai']
robots_deployed = [1200, 950, 850, 1100, 700, 600, 750]
population_millions = [14, 8, 9, 25, 3.5, 5, 20]  # Example population data for secondary axis

# Define bar positions and width
x_positions = np.arange(len(cities))
bar_width = 0.4

# Create the plot with a secondary y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Plot the bars for the number of robots
colors = ['#FFB6C1', '#87CEFA', '#FFD700', '#8A2BE2', '#7FFF00', '#FF4500', '#00CED1']
bars = ax1.bar(x_positions, robots_deployed, color=colors, width=bar_width, label='Robots Deployed')

# Overlay a line plot for population
ax2.plot(x_positions, population_millions, color='grey', marker='o', linestyle='-', linewidth=2,
         markersize=8, label='Population (millions)')

# Annotate each bar with the number of robots
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 25, f'{yval}', ha='center', va='bottom',
             fontsize=10, fontweight='bold')

# Customize the x-axis
ax1.set_xticks(x_positions)
ax1.set_xticklabels(cities, rotation=45, ha='right', fontsize=11)

# Set titles and labels
ax1.set_title("AI-driven Food Delivery Robots and Population (2030)\nAcross Major Global Cities",
              fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel("Number of Robots Deployed", fontsize=12)
ax2.set_ylabel("Population (millions)", fontsize=12)

# Add grid lines for the y-axis
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legends for both plots
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 1.15), fontsize=10)
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 1.15), fontsize=10)

# Highlight max robot deployment city
max_robots = max(robots_deployed)
max_city_index = robots_deployed.index(max_robots)
ax1.text(x_positions[max_city_index], max_robots + 100, f'Max: {cities[max_city_index]}', 
         ha='center', fontsize=11, color='red', fontweight='bold', bbox=dict(facecolor='white', alpha=0.6))

# Automatically adjust layout to fit all elements
plt.tight_layout()

# Show the plot
plt.show()