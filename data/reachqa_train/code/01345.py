import matplotlib.pyplot as plt

# Data: Contribution of each sector in percentage
sectors = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
energy_contribution = [30, 25, 20, 15, 10]

# Colors for the pie chart
colors = ['#ffcc00', '#66b3ff', '#99ff99', '#ff6666', '#c2c2f0']

# Explode the 'Solar' sector for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    energy_contribution,
    explode=explode,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='w', linewidth=2),
    shadow=True
)

# Draw a circle in the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax.axis('equal')

# Improve the appearance of the percentage labels
plt.setp(autotexts, size=10, weight="bold", color="black")

# Title of the chart
plt.title(
    "EcoLandia's Renewable Energy Generation in 2023:\nSector Contribution",
    fontsize=14,
    fontweight='bold'
)

# Adjust layout to avoid overlap
plt.tight_layout()

# Place the legend outside the pie
ax.legend(wedges, sectors,
          title="Energy Sectors",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Display the pie chart
plt.show()