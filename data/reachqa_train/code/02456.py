import matplotlib.pyplot as plt

# Define data for the pie chart
focus_areas = ['Planetary Exploration', 'Asteroid Mining', 'Interstellar Probes', 'Lunar Bases', 'Space Tourism']
mission_distribution = [30, 15, 20, 25, 10]  # Data reflecting the percentage distribution

# Define colors for each focus area
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a pie chart
fig, ax = plt.subplots(figsize=(9, 9))

# Set the explode parameter to highlight 'Interstellar Probes'
explode = (0, 0, 0.1, 0, 0)  

# Draw the pie chart
wedges, texts, autotexts = ax.pie(
    mission_distribution, 
    labels=focus_areas, 
    autopct='%1.1f%%', 
    startangle=90,
    colors=colors, 
    explode=explode,
    textprops={'fontsize': 10, 'weight': 'bold'},
    pctdistance=0.8  # Distance of the percentage text from the center
)

# Add a circle in the middle to create a donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie chart is circular
ax.axis('equal')  

# Set the title
ax.set_title("Space Exploration Missions:\nFocus Areas in 2050", fontsize=15, fontweight='bold', ha='center')

# Improve layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()