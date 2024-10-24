import matplotlib.pyplot as plt
import numpy as np

# Snack categories and preference percentages
snacks = ['Astro Chips', 'Lunar Puffs', 'Star Cookies', 'Galaxy Gummies', 'Nebula Noodles']
preferences = [25, 15, 30, 20, 10]

# Colors for each snack type
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Plotting the Donut Pie Chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(preferences, colors=colors, labels=snacks, autopct='%1.1f%%',
                                  startangle=90, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3), shadow=True)

# Add a circle at the center to create a 'donut' appearance
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Ensure equal aspect ratio to make the pie a perfect circle
ax.axis('equal')  

# Titles and customization
plt.title("The Galactic Snack Federation's Favorite Snacks", fontsize=14, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight="bold", color="black")

# Legend placed outside the chart
ax.legend(wedges, snacks, title="Snacks", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()