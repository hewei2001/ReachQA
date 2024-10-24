import matplotlib.pyplot as plt

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal']
energy_shares = [35, 30, 20, 10, 5]  # Percentage shares

# Colors for each energy source
colors = ['#FFD700', '#87CEEB', '#4682B4', '#8B4513', '#556B2F']

# Optionally explode the largest segment (Solar) for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(
    energy_shares, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode, 
    shadow=True
)

# Enhance text properties
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

# Set the chart title
ax.set_title(
    'Global Renewable Energy\nSources Share - 2023', 
    fontsize=16, 
    fontweight='bold', 
    pad=30
)

# Ensure the pie chart is a perfect circle
ax.axis('equal')

# Place the legend outside the pie chart
plt.legend(
    wedges, energy_sources,
    title="Energy Sources",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=12
)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()