import matplotlib.pyplot as plt
import numpy as np

# Define the cities and their sustainability metrics
cities = ['EcoVille', 'GreenTown', 'SustainCity', 'CleanBurg', 'EcoHaven']
metrics = ['Air Quality', 'Green Spaces', 'Renewable Energy', 
           'Waste Management', 'Public Transport', 'Community Engagement']

# Data for each city as percentage achievements
data = {
    'EcoVille': [85, 78, 90, 88, 95, 70],
    'GreenTown': [80, 85, 75, 92, 88, 75],
    'SustainCity': [75, 80, 70, 85, 80, 80],
    'CleanBurg': [90, 72, 80, 78, 85, 77],
    'EcoHaven': [88, 95, 82, 80, 75, 85]
}

# Calculate average performance for each city
averages = {city: np.mean(values) for city, values in data.items()}

# Convert data to the appropriate radar chart format
labels = np.array(metrics)
num_vars = len(labels)

# Function to draw radar charts
def radar_chart(ax, values, city_name, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='grey', fontsize=9)
    ax.set_yticklabels([])
    ax.set_title(city_name, size=13, color=color, loc='center', pad=20)

# Colors for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a grid of subplots
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(14, 12), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.5, wspace=0.5)

# Plot the radar chart for each city
for ax, (city, color) in zip(axs.flat[:5], zip(cities, colors)):
    radar_chart(ax, data[city], city, color)

# Remove any extra subplot created in the grid
fig.delaxes(axs[2, 1])

# Adding a bar chart for average scores
ax_bar = fig.add_subplot(3, 1, 3)
ax_bar.bar(cities, [averages[city] for city in cities], color=colors, alpha=0.7)
ax_bar.set_title("Average Sustainability Performance", fontsize=13, color='darkgreen', pad=20)
ax_bar.set_ylabel("Average Achievement (%)")
ax_bar.set_ylim(0, 100)

# Add a super title
plt.suptitle("Sustainability Assessment in Urban Development: \nComparative Radar and Average Performance Analysis", 
             fontsize=16, fontweight='bold', color='darkgreen')

# Automatically adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the radar charts and bar chart
plt.show()