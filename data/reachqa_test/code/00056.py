import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
galaxies = ['Milky Way', 'Andromeda', 'Triangulum', 'Whirlpool', 'Sombrero', 'Pinwheel']
tourists_percentage = [35, 25, 15, 10, 8, 7]
tourists_numbers = [35000, 25000, 15000, 10000, 8000, 7000]
colors = ['#FFD700', '#87CEEB', '#FF6347', '#4682B4', '#9ACD32', '#FFDDC1']
patterns = ['/', '\\', '|', '-', '+', '*']

# Explode the Milky Way slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0)

# Create the figure and a 3D axis
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Create the pie chart with enhancements
wedges, texts, autotexts = ax.pie(
    tourists_percentage, 
    explode=explode, 
    labels=galaxies, 
    autopct=lambda pct: f'{pct:.1f}%\n({int(pct*sum(tourists_numbers)/100):d})', 
    startangle=90, 
    colors=colors, 
    wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': 'solid'},
    textprops={'fontsize': 9, 'weight': 'bold', 'color': 'navy'},
    shadow=True
)

# Add pattern fills to each wedge
for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

# Title of the chart with a secondary line
plt.title('Galactic Tourism 2123\nDistribution of Tourists Across Galaxies', 
          fontsize=16, weight='bold', color='midnightblue', pad=20)

# Central circle for donut chart and text annotation
centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='black')
fig.gca().add_artist(centre_circle)
ax.text(0, 0, 'Total Tourists\n140,000', horizontalalignment='center',
        verticalalignment='center', fontsize=12, weight='bold', color='darkgreen')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Add a legend with galaxies, placed outside the pie
plt.legend(wedges, galaxies, title="Galaxies", loc="center left", 
           bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to make sure everything fits without overlap
plt.tight_layout()

# Display the plot
plt.show()