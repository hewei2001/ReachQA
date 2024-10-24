import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

# Define the percentage of different mission types for each year
manned_missions = np.array([30, 28, 27, 25, 23, 20])
satellite_deployments = np.array([25, 30, 32, 35, 38, 40])
rover_missions = np.array([15, 12, 10, 10, 9, 8])
space_telescopes = np.array([10, 10, 11, 12, 13, 15])
space_probes = np.array([20, 20, 20, 18, 17, 17])

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 7))

# Colors for each mission type
colors = ['#FF6347', '#4682B4', '#90EE90', '#FFD700', '#9370DB']

# Create the percentage bar chart
ax.bar(years, manned_missions, color=colors[0], label='Manned Missions')
ax.bar(years, satellite_deployments, bottom=manned_missions, color=colors[1], label='Satellite Deployments')
ax.bar(years, rover_missions, bottom=manned_missions + satellite_deployments, color=colors[2], label='Rover Missions')
ax.bar(years, space_telescopes, bottom=manned_missions + satellite_deployments + rover_missions, color=colors[3], label='Space Telescopes')
ax.bar(years, space_probes, bottom=manned_missions + satellite_deployments + rover_missions + space_telescopes, color=colors[4], label='Space Probes')

# Customize the plot with title and labels
ax.set_title('Distribution of Space Exploration Missions\n(2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Missions (%)', fontsize=12)
ax.legend(title='Mission Types', loc='upper right', fontsize=10)
ax.set_xlim(years[0] - 1, years[-1] + 1)
ax.set_ylim(0, 100)
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Add percentage labels on each section
for i, year in enumerate(years):
    total_height = 0
    for mission_type, color in zip([manned_missions, satellite_deployments, rover_missions, space_telescopes, space_probes], colors):
        height = mission_type[i]
        ax.text(year, total_height + height / 2, f'{height}%', ha='center', va='center', fontsize=9, color='black', weight='bold')
        total_height += height

# Add annotations to highlight significant shifts
ax.annotate('Increase in Satellite Deployments', xy=(2016, 70), xytext=(2014, 85),
            arrowprops=dict(arrowstyle='->', color='black'), fontsize=10, ha='center')

ax.annotate('Rise of Space Telescopes', xy=(2020, 98), xytext=(2018, 90),
            arrowprops=dict(arrowstyle='->', color='black'), fontsize=10, ha='center')

# Ensure tight layout
plt.tight_layout()

# Display the chart
plt.show()