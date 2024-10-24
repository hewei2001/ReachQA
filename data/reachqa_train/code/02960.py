import matplotlib.pyplot as plt

# Renewable energy sources and their projected contribution percentages
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal', 'Tidal']
contributions = [35, 25, 20, 10, 5, 5]

# Define colors for each energy source
colors = ['#FFD700', '#FF7F50', '#4682B4', '#9ACD32', '#DA70D6', '#40E0D0']

# Explode the slice for Solar to highlight it
explode = (0.1, 0, 0, 0, 0, 0)

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(contributions, explode=explode, labels=energy_sources, colors=colors, 
                                  autopct='%1.1f%%', startangle=140, pctdistance=0.85,
                                  wedgeprops=dict(edgecolor='white', width=0.3), shadow=True)

# Draw a circle at the center to transform pie into a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Enhance the text styles
plt.setp(autotexts, size=12, weight='bold', color='darkblue')
plt.setp(texts, size=14, weight='bold')

# Set the title
ax.set_title('Renewable Energy Contributions: \nA 2050 Vision for a Greener Tomorrow', 
             fontsize=16, weight='bold', pad=30)

# Position the legend outside the donut pie chart
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=12, title_fontsize='13', shadow=True)

# Adjust layout for better visual presentation
plt.tight_layout()

# Display the donut pie chart
plt.show()