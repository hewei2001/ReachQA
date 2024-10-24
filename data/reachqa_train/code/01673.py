import matplotlib.pyplot as plt

# Define the data
mission_types = ['Planetary Exploration', 'Astronomical Observation', 
                 'Technological Demonstration', 'Human Spaceflight']
mission_counts = [40, 30, 20, 10]

# Colors for each mission type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the ring chart
wedges, texts, autotexts = ax.pie(
    mission_counts, 
    labels=mission_types, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops={'fontsize': 12, 'color': 'black'}
)

# Draw a title in the center of the ring
plt.text(0, 0, 'AstroVentures\nMissions\n2013-2023', 
         horizontalalignment='center', verticalalignment='center', 
         fontsize=14, fontweight='bold', color='navy')

# Title above the chart
plt.title("AstroVentures' Decade of Discovery:\nSpace Mission Distribution",
          fontsize=16, fontweight='bold', color='navy', pad=20)

# Adjust legend to avoid overlap
plt.legend(wedges, mission_types, title="Mission Types",
           loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure layout is tight and no elements overlap
plt.tight_layout()

# Show the plot
plt.show()