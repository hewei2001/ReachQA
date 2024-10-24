import matplotlib.pyplot as plt
import numpy as np

# Define the years and milestones data
years = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
launch_vehicles = np.array([1, 3, 5, 10, 15, 20, 25])
spacecraft = np.array([0, 1, 4, 6, 12, 18, 23])
robotics = np.array([0, 0, 2, 3, 8, 12, 15])
satellite_technology = np.array([0, 2, 5, 9, 16, 25, 30])

# Data for the additional subplot: funding over time
funding = np.array([0.1, 0.5, 1.5, 3.0, 5.0, 7.0, 10.0])  # in billions
technology_funding = {
    'Launch Vehicles': np.array([0.01, 0.07, 0.3, 0.8, 1.5, 2.5, 4.0]),
    'Spacecraft': np.array([0.02, 0.1, 0.4, 0.8, 1.5, 3.0, 4.5]),
    'Robotics': np.array([0.00, 0.01, 0.1, 0.2, 0.5, 1.0, 1.5]),
    'Satellite Tech': np.array([0.01, 0.02, 0.1, 0.3, 0.7, 1.5, 2.5]),
}

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Area chart for cumulative milestones
ax1.fill_between(years, launch_vehicles, color="skyblue", alpha=0.6, label='Launch Vehicles')
ax1.fill_between(years, launch_vehicles + spacecraft, launch_vehicles, color="orange", alpha=0.6, label='Spacecraft')
ax1.fill_between(years, launch_vehicles + spacecraft + robotics,
                 launch_vehicles + spacecraft, color="lightgreen", alpha=0.6, label='Robotics')
ax1.fill_between(years, launch_vehicles + spacecraft + robotics + satellite_technology,
                 launch_vehicles + spacecraft + robotics, color="lightcoral", alpha=0.6, label='Satellite Technology')

# Titles and labels for the area chart
ax1.set_title('Evolution of Space Exploration Technologies\nCumulative Milestones (1960-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Cumulative Milestones', fontsize=12)
ax1.set_xticks(years)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(title='Technology Categories', loc='upper left')

# Line plot for funding over time
for tech, values in technology_funding.items():
    ax2.plot(years, values, marker='o', label=tech)

# Titles and labels for the funding chart
ax2.set_title('Funding in Space Exploration Technologies (1960-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Funding (in billions)', fontsize=12)
ax2.set_xticks(years)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(title='Technology Categories', loc='upper left')

# Adjust layout to prevent clipping of labels and ensure text is displayed clearly
plt.tight_layout()
plt.show()