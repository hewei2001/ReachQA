import matplotlib.pyplot as plt
import numpy as np

# Mission types and their proportions
mission_types = ['Landing Missions', 'Orbital Studies', 'Rover Explorations', 'Flyby Missions', 'Sample Return']
missions_proportions = [20, 35, 25, 10, 10]  # Total sums up to 100%

# Define colors for each mission type
colors = ['#FFA07A', '#8A2BE2', '#7FFF00', '#DC143C', '#FFD700']

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    missions_proportions, labels=mission_types, autopct='%1.1f%%', startangle=140,
    colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='white'))

# Customize text properties
plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=10)

# Title and central text
ax.set_title('AstroVentures Missions (2000-2023)\nPlanetary Exploration Focus', fontsize=14, weight='bold', pad=20)

# Central circle for the ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Legend outside the chart
ax.legend(wedges, mission_types, title="Mission Types", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Annotations for emphasis
ax.annotate('Focus on\nOrbital Studies', xy=(-0.7, 0.3), xytext=(-1.5, 0.9),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='lightgrey')

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()