import matplotlib.pyplot as plt
import numpy as np

# Data for the Galactic Exploration Fleet Allocation
mission_types = ['Exoplanet Studies', 'Deep Space Probes', 'Astrobiology Research',
                 'Asteroid Mining', 'Cosmic Observations']
fleet_distribution = [25, 30, 20, 15, 10]  # Representing percentage of fleet allocation

# Cosmic-themed colors for each mission type
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Create a figure for the pie chart
plt.figure(figsize=(10, 7))

# Plotting the sector pie chart with adjustments
wedges, texts, autotexts = plt.pie(
    fleet_distribution, labels=mission_types, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, textprops={'fontsize': 10, 'color': 'navy'},
    explode=(0.05, 0.05, 0.05, 0.1, 0.05)  # Slightly explode the 'Asteroid Mining' for emphasis
)

# Add a circle in the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

# Ensure the pie is drawn as a circle
plt.axis('equal')

# Title for the plot with a line break
plt.title("Galactic Exploration Initiative Fleet Allocation\nAcross Various Mission Types", fontsize=14, fontweight='bold', pad=20)

# Adding a legend for clarity
plt.legend(wedges, mission_types, title="Mission Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Improve the layout for better presentation
plt.tight_layout()

# Show the plot
plt.show()