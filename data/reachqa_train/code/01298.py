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

# Calculate angles for the radar chart, adding the first angle to close the chart loop
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

# Function to plot one suit on the radar chart
def plot_radar(suit_data, label, color):
    suit_data += suit_data[:1]  # Closing the loop
    ax.fill(angles, suit_data, color=color, alpha=0.25)
    ax.plot(angles, suit_data, color=color, linewidth=2, label=label)

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each suit with a unique color
plot_radar(mars_suit, 'Mars Suit', '#FF5733')  # Reddish for Mars
plot_radar(venus_suit, 'Venus Suit', '#FFC300')  # Yellowish for Venus
plot_radar(jupiter_suit, 'Jupiter Suit', '#DAF7A6')  # Light green for Jupiter
plot_radar(moon_suit, 'Moon Suit', '#C70039')  # Dark red for the Moon

# Add category labels
plt.xticks(angles[:-1], categories, color='grey', size=10)

# Set radial limits
ax.set_rscale('linear')
ax.set_ylim(0, 10)

# Title and Legend
plt.title("Planetary Exploration Suit\nCapability Assessment", size=15, color='black', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, frameon=False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()