import matplotlib.pyplot as plt
import numpy as np

# Data for magical energy sources in Arcania
magic_sources = ['Elemental', 'Runic', 'Astral', 'Ancient', 'Spirit']
energy_distribution = [35, 25, 15, 10, 15]

# Colors for each magical source
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#D1BBFF']

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 7))

# Create the donut pie chart
wedges, texts, autotexts = ax.pie(
    energy_distribution,
    labels=magic_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Draw a center circle for the donut hole
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set chart title
ax.set_title("Magical Energy Sources\nin Arcania", fontsize=16, fontweight='bold', pad=30)

# Enhance the appearance of the text
plt.setp(autotexts, size=10, fontweight="bold", color="black")
plt.setp(texts, size=11, fontweight="bold")

# Add a shadow effect for the pie chart
ax.pie(energy_distribution, colors=colors, shadow=True, startangle=90, wedgeprops=dict(width=0.3))

# Add a legend to the side
ax.legend(wedges, magic_sources, title="Magic Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure a clean layout
plt.tight_layout()

# Display the plot
plt.show()