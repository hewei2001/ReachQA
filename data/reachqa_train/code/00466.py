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

# Convert data to the appropriate radar chart format
labels = np.array(metrics)
num_vars = len(labels)

# Function to draw radar charts
def radar_chart(ax, values, city_name, color):
    # Calculate angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop by appending the start to the end
    values += values[:1]
    angles += angles[:1]

    # Draw the outline of the radar chart
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2)

    # Set labels for each axis
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='grey', fontsize=10)
    ax.set_yticklabels([])
    
    # Add a title for each subplot
    ax.set_title(city_name, size=13, color=color, loc='center', pad=20)

# Colors for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a grid of subplots
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(14, 8), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# Plot the radar chart for each city
for ax, (city, color) in zip(axs.flat, zip(cities, colors)):
    radar_chart(ax, data[city], city, color)

# Remove the extra subplot
fig.delaxes(axs[1, 2])

# Add a super title
plt.suptitle("Sustainability Assessment in Urban Development: Comparative Radar Analysis", 
             fontsize=16, fontweight='bold', color='darkgreen')

# Automatically adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the radar charts
plt.show()