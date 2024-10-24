import matplotlib.pyplot as plt
import numpy as np

# Define cities and years
cities = ['Amsterdam', 'San Francisco', 'Tokyo', 'Copenhagen', 'Vancouver']
years = ['2020', '2021', '2022', '2023']

# Number of new EV charging stations each year for each city
amsterdam_stations = [150, 200, 250, 300]
san_francisco_stations = [180, 220, 260, 310]
tokyo_stations = [160, 210, 240, 290]
copenhagen_stations = [140, 190, 230, 280]
vancouver_stations = [170, 200, 250, 320]

# Aggregate data for plotting
data = [amsterdam_stations, san_francisco_stations, tokyo_stations, copenhagen_stations, vancouver_stations]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting details
width = 0.15  # width of the bars
x = np.arange(len(years))  # the label locations

# Colors for each city
colors = ['#76b852', '#ff7f50', '#4c8c2a', '#468499', '#d4b930']

# Plot each city's data as a separate set of bars
for i, (city_data, color) in enumerate(zip(data, colors)):
    rects = ax.bar(x + i * width, city_data, width, label=cities[i], color=color)
    # Annotate each bar with its value
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

# Customizing the plot
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('New EV Charging Stations', fontsize=12)
ax.set_title('Growth of EV Charging Stations\nEco-Friendly Cities Initiative', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x + width * 2)
ax.set_xticklabels(years, fontsize=11)
ax.legend(title="Cities", fontsize=10, loc='upper left')

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()