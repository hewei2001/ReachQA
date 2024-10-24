import matplotlib.pyplot as plt
import numpy as np

# Data for the line chart
years = np.array(range(2013, 2023))
spring_temps = [7.0, 9.5, 9.0, 8.2, 10.5, 11.0, 12.3, 13.1, 12.8, 13.2]  # Spring
summer_temps = [25.0, 27.5, 26.8, 25.7, 28.3, 28.8, 30.1, 30.8, 31.2, 32.0]  # Summer
fall_temps = [12.0, 11.5, 13.0, 13.2, 14.5, 14.8, 15.1, 16.1, 16.3, 16.5]  # Fall
winter_temps = [-1.5, -1.0, -0.5, -1.2, -0.3, -0.2, 0.1, 1.0, 1.2, 1.8]  # Winter

# Create a figure and specify the background color
plt.figure(figsize=(14, 8), facecolor='aliceblue')

# Define a color map for the seasons
colors = plt.cm.tab10(np.linspace(0, 1, 4))

# Plotting with season colors and markers
plt.plot(years, spring_temps, color=colors[0], marker='o', label='Spring (March)', linewidth=2, markersize=6)
plt.plot(years, summer_temps, color=colors[1], marker='s', label='Summer (June)', linewidth=2, markersize=6)
plt.plot(years, fall_temps, color=colors[2], marker='^', label='Fall (September)', linewidth=2, markersize=6)
plt.plot(years, winter_temps, color=colors[3], marker='v', label='Winter (December)', linewidth=2, markersize=6)

# Annotate data points for each season, adjusted for readability
for i, year in enumerate(years):
    plt.annotate(f'{spring_temps[i]:.1f}°C', (year, spring_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', va='bottom', color=colors[0])
    plt.annotate(f'{summer_temps[i]:.1f}°C', (year, summer_temps[i]), textcoords="offset points", xytext=(0,-15), ha='center', va='top', color=colors[1])
    plt.annotate(f'{fall_temps[i]:.1f}°C', (year, fall_temps[i]), textcoords="offset points", xytext=(0,-10), ha='center', va='top', color=colors[2])
    plt.annotate(f'{winter_temps[i]:.1f}°C', (year, winter_temps[i]), textcoords="offset points", xytext=(0,15), ha='center', va='bottom', color=colors[3])

# Customize the plot with a multi-line title
plt.title('Temperature Trends\nand Seasonal Variations in Minneapolis\n(2013-2022)', fontsize=16, linespacing=1.5)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

# Adjust legend
plt.legend(loc='upper left', fontsize=12)

# Adjust grid and layout
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()

# Show the plot with annotations, markers, and a grid for readability and functionality
plt.show()