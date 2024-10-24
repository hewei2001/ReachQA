import matplotlib.pyplot as plt

# Define renewable energy sources and their respective global contribution percentages
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
contributions = [35, 30, 20, 10, 5]

# Colors for each sector of the pie chart
colors = ['#ffcc00', '#66b3ff', '#99ff99', '#ff9999', '#ffcc99']

# Explode to highlight Solar, the largest contributing source
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(contributions, labels=energy_sources, autopct='%1.1f%%',
                                  startangle=140, colors=colors, explode=explode,
                                  pctdistance=0.85, shadow=True, textprops=dict(color="black"))

# Draw a circle at the center of the pie to create a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is drawn as a circle
ax.axis('equal')

# Set the title for the chart with line breaks for readability
plt.title('Global Renewable Energy Distribution in 2023\nHighlighting Sustainable Contributions',
          fontsize=14, fontweight='bold')

# Format texts
plt.setp(texts, size=12, weight="bold")
plt.setp(autotexts, size=10, weight="bold")

# Adjust layout to prevent clipping of elements
plt.tight_layout()

# Add a legend with a title, positioned outside the chart
plt.legend(wedges, energy_sources, title="Energy Sources",
           loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Display the final plot
plt.show()