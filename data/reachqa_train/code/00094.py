import matplotlib.pyplot as plt
import numpy as np

# Data for the fleet composition
ship_types = ['Exploration', 'Defense', 'Cargo', 'Scientific', 'Diplomatic']
percentages = [25, 35, 15, 10, 15]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Colors for each type

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Pie chart with a donut-style hole in the center
wedges, texts, autotexts = ax.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors, pctdistance=0.85,
                                  labels=ship_types, wedgeprops=dict(width=0.3), explode=(0.05, 0.05, 0.05, 0.05, 0.05))

# Draw circle in the center to create a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set the title of the chart
ax.set_title("Galactic Federation Fleet Composition\nShip Types and Capabilities", fontsize=14, fontweight='bold')

# Improve aesthetics of the texts
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=9)

# Custom legend
ax.legend(wedges, ship_types, title="Ship Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to fit everything without overlap
plt.tight_layout()

# Display the plot
plt.show()