import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ['2018', '2019', '2020', '2021', '2022']
satellite_dev = [150, 180, 200, 220, 210]
propulsion_sys = [100, 110, 140, 160, 180]
space_habitats = [70, 90, 120, 130, 150]
robotics_ai = [60, 80, 100, 120, 140]

# Stack calculations
propulsion_bottom = np.array(satellite_dev)
space_habitats_bottom = propulsion_bottom + np.array(propulsion_sys)
robotics_ai_bottom = space_habitats_bottom + np.array(space_habitats)

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(years, satellite_dev, label='Satellite Development', color='cornflowerblue')
ax.bar(years, propulsion_sys, bottom=propulsion_bottom, label='Propulsion Systems', color='coral')
ax.bar(years, space_habitats, bottom=space_habitats_bottom, label='Space Habitats', color='lightgreen')
ax.bar(years, robotics_ai, bottom=robotics_ai_bottom, label='Robotics & AI', color='orchid')

# Adding titles and labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Funding (in millions)', fontsize=12)
ax.set_title('Space Technology Funding Allocation\n(2018-2022)', fontsize=16, fontweight='bold')

# Rotate x-axis labels for better readability
ax.set_xticklabels(years, rotation=45)

# Grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Sectors')

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()