import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2026)
satellite_dev = [100 + 10*np.sin(i/2.0) + i*5 for i in range(len(years))]
propulsion_sys = [80 + 10*np.cos(i/3.0) + i*3 for i in range(len(years))]
space_habitats = [50 + 7*np.sin(i/1.5) + i*4 for i in range(len(years))]
robotics_ai = [40 + 5*np.cos(i/2.5) + i*2 for i in range(len(years))]
communication_sys = [60 + 8*np.sin(i/1.7) + i*2.5 for i in range(len(years))]

# Stack calculations
propulsion_bottom = np.array(satellite_dev)
space_habitats_bottom = propulsion_bottom + np.array(propulsion_sys)
robotics_ai_bottom = space_habitats_bottom + np.array(space_habitats)
comm_sys_bottom = robotics_ai_bottom + np.array(robotics_ai)

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(years, satellite_dev, label='Satellite Development', color='cornflowerblue')
ax.bar(years, propulsion_sys, bottom=propulsion_bottom, label='Propulsion Systems', color='coral')
ax.bar(years, space_habitats, bottom=space_habitats_bottom, label='Space Habitats', color='lightgreen')
ax.bar(years, robotics_ai, bottom=robotics_ai_bottom, label='Robotics & AI', color='orchid')
ax.bar(years, communication_sys, bottom=comm_sys_bottom, label='Communication Systems', color='gold')

# Cumulative percentage line
total_funding = comm_sys_bottom + np.array(communication_sys)
cumulative_percentage = (total_funding / total_funding[-1]) * 100
ax.plot(years, cumulative_percentage, color='black', marker='o', linestyle='-', linewidth=2, label='Cumulative % of Total Funding')

# Adding titles and labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Funding (in millions)', fontsize=12)
ax.set_title('Space Technology Funding Allocation\nAcross Various Sectors (2010-2025)', fontsize=16, fontweight='bold')

# Rotate x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Sectors', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()