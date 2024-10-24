import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.colors as mcolors

# Snack categories and preference percentages
snacks = ['Astro Chips', 'Lunar Puffs', 'Star Cookies', 'Galaxy Gummies', 'Nebula Noodles']
preferences = [25, 15, 30, 20, 10]

# Colors for each snack type with added transparency
colors = ['#ff9999cc', '#66b3ffcc', '#99ff99cc', '#ffcc99cc', '#c2c2f0cc']

# Additional data: popularity increase over a fictional period
popularity_increase = [5, 3, 4, 2, 1]

# Create a figure with a subplot layout
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# Plotting the Donut Pie Chart
wedges, texts, autotexts = ax.pie(preferences, colors=colors, labels=snacks,
                                  autopct='%1.1f%%', startangle=90,
                                  pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'),
                                  shadow=True)

# Add a circle at the center for the 'donut' effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white', lw=1.5)
fig.gca().add_artist(centre_circle)

# Ensure equal aspect ratio for a perfect circle
ax.axis('equal')  

# Detailed title using text alignment and line break
plt.title("The Galactic Snack Federation's Favorite Snacks\nand Their Recent Popularity Surge",
          fontsize=14, fontweight='bold', va='baseline', ha='center')

# Set properties for the auto text
plt.setp(autotexts, size=10, weight="bold", color="black")

# Adding annotations with arrows
for i, (wedge, preference, increase) in enumerate(zip(wedges, preferences, popularity_increase)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x, y = np.cos(np.radians(angle)), np.sin(np.radians(angle))
    ax.annotate(f"{increase}% increase", xy=(x, y), xytext=(1.1 * x, 1.1 * y),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Legend outside the chart with background
legend = ax.legend(wedges, snacks, title="Snacks", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(legend.get_title(), fontsize='12', fontweight='bold')

# Additional customization for legend background
for text in legend.get_texts():
    text.set_bbox(dict(facecolor='whitesmoke', edgecolor='black', boxstyle='round,pad=0.3'))

# Add grid-like pattern to the background to simulate a futuristic theme
fig.patch.set_visible(True)
fig.patch.set_color('#f0f0f5')
fig.patch.set_alpha(0.8)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()