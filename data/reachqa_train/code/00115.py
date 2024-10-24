import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest
years = np.arange(2010, 2020)

# Simulated restoration data for each site
pyramid_restorations = [2, 4, 5, 7, 9, 12, 14, 17, 19, 22]
colosseum_restorations = [1, 2, 3, 5, 7, 10, 12, 14, 16, 20]
machu_picchu_restorations = [0, 1, 3, 4, 6, 8, 10, 12, 15, 18]
taj_mahal_restorations = [0, 2, 3, 5, 6, 8, 10, 11, 13, 15]
great_wall_restorations = [1, 3, 4, 6, 8, 11, 13, 15, 17, 21]

# Plot the line chart
fig, ax = plt.subplots(figsize=(14, 8))

# Define a color scheme and markers
colors = ['gold', 'red', 'green', 'blue', 'brown']
markers = ['o', '^', 's', 'd', 'x']
sites = ['Great Pyramid of Giza', 'The Colosseum', 'Machu Picchu', 'The Taj Mahal', 'Great Wall of China']
restoration_data = [pyramid_restorations, colosseum_restorations, machu_picchu_restorations, taj_mahal_restorations, great_wall_restorations]

# Plot data with annotations
for i, data in enumerate(restoration_data):
    ax.plot(years, data, label=sites[i], color=colors[i], marker=markers[i], linewidth=2)
    for j, y in enumerate(data):
        ax.annotate(f'{y}', (years[j], y), textcoords="offset points", xytext=(0, 10), ha='center',
                    fontsize=9, color=colors[i])

# Annotate major milestones
milestones = {
    2013: 'Colosseum: Facade restoration',
    2015: 'Machu Picchu: Tourist center',
    2017: 'Taj Mahal: Marble cleaning',
    2019: 'Great Wall: Section rebuilt'
}

for year, text in milestones.items():
    x, y_values = year, [data[year - 2010] for data in restoration_data]
    max_y_index = np.argmax(y_values)
    ax.annotate(text, (x, y_values[max_y_index]), textcoords="offset points", xytext=(30, -15), ha='center',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color=colors[max_y_index], lw=1.5),
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor=colors[max_y_index], facecolor='white'))

# Title and labels
ax.set_title('The Renaissance of Ancient Wonders:\nTimeline of World Heritage Site Restorations', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Completed Restorations', fontsize=12)

# Legend and grid
ax.legend(title='World Heritage Sites', loc='upper left', fontsize=10, title_fontsize='12', frameon=True)
ax.grid(True, linestyle='--', alpha=0.5)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()