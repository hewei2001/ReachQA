import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories for smart city metrics
categories = ["Transportation", "Energy", "Connectivity", "Waste Mgmt", "Safety"]
N = len(categories)

# Define the smart city metrics for each city
techopolis = [9, 8, 9, 7, 8]
greenberg = [8, 9, 7, 9, 7]
metroworld = [7, 6, 8, 8, 9]

# Calculate angles for the radar chart, adding the first angle to close the chart loop
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to plot one city on the radar chart
def plot_radar(ax, city_data, label, color):
    city_data += city_data[:1]  # Closing the loop
    ax.fill(angles, city_data, color=color, alpha=0.25)
    ax.plot(angles, city_data, color=color, linewidth=2, label=label)

# Plot radar chart for each city
plot_radar(ax, techopolis, 'Techopolis', '#1f77b4')
plot_radar(ax, greenberg, 'Greenberg', '#2ca02c')
plot_radar(ax, metroworld, 'Metroworld', '#ff7f0e')

# Add category labels to the radar chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='grey', size=10)

# Set radial limits for the radar chart
ax.set_ylim(0, 10)

# Title and Legend for the radar chart
ax.set_title("Smart City Metrics Assessment", size=14, color='black', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, frameon=False)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()