import matplotlib.pyplot as plt

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal', 'Ocean']
energy_share = [30, 25, 20, 15, 5, 5]

# Colors for each segment
colors = ['#FFD700', '#87CEEB', '#00FA9A', '#8B4513', '#FF6347', '#4682B4']

# Explode the 'Solar' slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_share, labels=energy_sources, autopct='%1.1f%%',
    startangle=140, colors=colors, explode=explode, shadow=True,
    textprops=dict(color='black')
)

# Style the chart
plt.setp(autotexts, size=10, weight="bold")
plt.setp(texts, size=12)

# Title and legend setup
ax.set_title(
    "Global Renewable Energy Mix in 2050:\nA Sustainable Future", 
    fontsize=16, fontweight='bold', pad=20
)
ax.legend(
    wedges, energy_sources, title="Energy Sources", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()