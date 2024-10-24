import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories for assessment
categories = ["Radiation Protection", "Temperature Adaptability", "Terrain Navigation", 
              "Communication Systems", "Mobility"]
N = len(categories)

# Define the capabilities for each suit
mars_suit = [8, 7, 9, 6, 8]
venus_suit = [7, 9, 5, 8, 6]
jupiter_suit = [6, 8, 7, 7, 5]
moon_suit = [7, 6, 8, 8, 9]

# Calculate average capabilities across suits for the bar chart
average_capabilities = [
    np.mean([mars_suit[i], venus_suit[i], jupiter_suit[i], moon_suit[i]])
    for i in range(N)
]

# Calculate angles for the radar chart, adding the first angle to close the chart loop
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

# Initialize figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8), subplot_kw=dict(polar=True))

# Function to plot one suit on the radar chart
def plot_radar(ax, suit_data, label, color):
    suit_data += suit_data[:1]  # Closing the loop
    ax.fill(angles, suit_data, color=color, alpha=0.25)
    ax.plot(angles, suit_data, color=color, linewidth=2, label=label)

# Plot radar chart for each suit
plot_radar(ax1, mars_suit, 'Mars Suit', '#FF5733')
plot_radar(ax1, venus_suit, 'Venus Suit', '#FFC300')
plot_radar(ax1, jupiter_suit, 'Jupiter Suit', '#DAF7A6')
plot_radar(ax1, moon_suit, 'Moon Suit', '#C70039')

# Add category labels to radar chart
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, color='grey', size=10)

# Set radial limits for radar chart
ax1.set_ylim(0, 10)

# Title and Legend for radar chart
ax1.set_title("Planetary Exploration Suit\nCapability Assessment", size=14, color='black', y=1.1)
ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, frameon=False)

# Bar chart for average capabilities
ax2.bar(categories, average_capabilities, color=['#FF5733', '#FFC300', '#DAF7A6', '#C70039', '#FF5733'])

# Title and labels for the bar chart
ax2.set_title("Average Capabilities Across Suits", size=14, color='black')
ax2.set_ylim(0, 10)
ax2.set_ylabel("Average Capability Score")
ax2.set_xticklabels(categories, rotation=45, ha='right', size=10)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plots
plt.show()