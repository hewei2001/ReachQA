import numpy as np
import matplotlib.pyplot as plt

# Data Setup
missions = ['Orbital Satellite', 'Lunar Lander', 'Mars Rover']
criteria = ['Communication', 'Propulsion', 'Payload', 'Navigation', 'Life Support', 'Instruments']

# Scores for each mission type on a scale of 0 to 10
orbital_satellite = [9, 8, 7, 9, 0, 6]
lunar_lander = [7, 7, 8, 6, 5, 8]
mars_rover = [6, 9, 6, 8, 7, 9]

# Calculating average scores for overlay plot
avg_scores = np.array([orbital_satellite, lunar_lander, mars_rover]).mean(axis=0).tolist()
avg_scores += avg_scores[:1]

# Append first element to the end to close the radar chart loop
orbital_satellite += orbital_satellite[:1]
lunar_lander += lunar_lander[:1]
mars_rover += mars_rover[:1]

# Angles for each criteria axis, equally spaced around a circle
num_vars = len(criteria)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each mission's capabilities
ax.fill(angles, orbital_satellite, color='skyblue', alpha=0.3, label='Orbital Satellite')
ax.fill(angles, lunar_lander, color='seagreen', alpha=0.3, label='Lunar Lander')
ax.fill(angles, mars_rover, color='salmon', alpha=0.3, label='Mars Rover')

# Connect the points with lines for each mission
ax.plot(angles, orbital_satellite, color='skyblue', linewidth=2)
ax.plot(angles, lunar_lander, color='seagreen', linewidth=2)
ax.plot(angles, mars_rover, color='salmon', linewidth=2)

# Overlay plot for average scores
ax.plot(angles, avg_scores, color='black', linestyle='--', linewidth=2, marker='o', label='Average Score')

# Labels for each criteria
ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=10, color='black', wrap=True)

# Remove y-tick labels and set grid for better clarity
ax.set_yticklabels([])
ax.grid(linewidth=0.5, color='grey', linestyle='--')

# Add a title with a line break
ax.set_title("Comparative Assessment of Space Mission Capabilities\nIncluding Average Scores", 
             fontsize=14, fontweight='bold', va='bottom')

# Add legend with adjustment to avoid overlap
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=10)

# Automatically adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the radar chart
plt.show()