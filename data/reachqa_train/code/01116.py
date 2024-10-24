import matplotlib.pyplot as plt

# Data for the energy distribution in Wonderland
energy_sources = ['Solar Power', 'Wind Power', 'Hydro Power', 'Geothermal', 'Biomass']
energy_percentages = [35, 25, 20, 10, 10]

# Colors associated with each energy source
colors = ['#ffd700', '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']

# Explode the solar power slice for emphasis
explode = (0.1, 0, 0, 0, 0)  # Emphasize the first slice (i.e., Solar Power)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_percentages, 
    explode=explode, 
    labels=energy_sources, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85
)

# Format autotexts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Draw a circle at the center of pie to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')  

# Title with line breaks for clarity
plt.title(
    'Renewable Energy Landscape in Wonderland:\nDistribution of Energy Sources', 
    fontsize=16, 
    weight='bold', 
    pad=20
)

# Add a legend outside the plot
ax.legend(wedges, energy_sources, title="Energy Sources", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()