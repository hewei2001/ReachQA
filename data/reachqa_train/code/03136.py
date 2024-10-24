import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and teams
categories = ['AI', 'Robotics', 'Quantum Computing', 'Bioengineering', 'Space Exploration']
teams = ['Alpha Centauri Innovators', 'Sirius Robotics Guild', 'Andromeda Tech Masters']

# Number of variables (categories)
num_vars = len(categories)

# Data for each team (score out of 10 in each category)
data = {
    'Alpha Centauri Innovators': [8, 9, 7, 6, 8],
    'Sirius Robotics Guild': [7, 8, 8, 7, 6],
    'Andromeda Tech Masters': [9, 7, 6, 8, 9],
}

# Calculate the angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each team's performance
for team, values in data.items():
    values += values[:1]  # Repeat the first value to close the chart
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=team)
    ax.fill(angles, values, alpha=0.25)

# Add labels for each category
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='gray')

# Set the chart range
ax.set_ylim(0, 10)

# Add a title and legend
plt.title("Intergalactic Innovation Championship 2135:\nUnveiling Tomorrow's Technology", fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()