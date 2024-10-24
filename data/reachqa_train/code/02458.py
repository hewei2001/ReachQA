import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the number of capabilities and names
categories = ['Research', 'Logistics', 'Survival', 'Propulsion', 'Communication']
N = len(categories)

# Define the values for each type of mission
lunar_exploration = [8, 5, 6, 7, 9]
mars_colonization = [7, 9, 8, 6, 5]
asteroid_mining = [5, 7, 6, 8, 6]

# New overlay data: Ideal Mission profile
ideal_mission = [9, 8, 7, 8, 9]

# Combine data into a list
data = [lunar_exploration, mars_colonization, asteroid_mining]
labels = ['Lunar Exploration', 'Mars Colonization', 'Asteroid Mining']

# Create the angles for the radar chart (one per category plus initial position to close the radar chart)
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

# Extend each data point to close the radar chart loop
for i in range(len(data)):
    data[i] += data[i][:1]
ideal_mission += ideal_mission[:1]

# Function to create the radar chart
def create_radar_chart(data, labels, categories, angles, ideal_mission):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Colors for each mission type
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

    for d, label, color in zip(data, labels, colors):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color, linewidth=2, label=label)

    # Overlay: Ideal Mission
    ax.plot(angles, ideal_mission, color='black', linewidth=2, linestyle='--', label='Ideal Mission')
    ax.scatter(angles[:-1], ideal_mission[:-1], color='black', s=50, zorder=10)

    # Add category labels to each spoke
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)

    # Add a title with line breaks for better readability
    plt.title('Comparative Analysis of Space Mission Capabilities:\nRadar Chart with Ideal Mission Overlay', 
              size=15, weight='bold', pad=20)
    
    # Adding a legend and adjusting its position
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # Adjust layout to prevent overlap and ensure the plot is centered
    plt.tight_layout()
    
    # Show the plot
    plt.show()

# Create the radar chart
create_radar_chart(data, labels, categories, angles, ideal_mission)