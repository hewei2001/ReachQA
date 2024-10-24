import matplotlib.pyplot as plt

# Data representing Techburg's projected energy consumption by 2030
energy_sources = ['Solar Power', 'Wind Power', 'Hydroelectric', 'Geothermal', 'Nuclear', 'Natural Gas', 'Biofuels']
percentages = [30, 25, 20, 10, 5, 5, 5]

# Color palette for each energy source
colors = ['#FFD700', '#ADFF2F', '#00CED1', '#FF4500', '#8A2BE2', '#FF8C00', '#7FFF00']

# Highlight the largest segment (Solar Power) to emphasize its importance
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.4, edgecolor='w'),  # Create donut effect
    shadow=True  # Add shadow for visual depth
)

# Set font size and weight for labels and percentages
plt.setp(texts, size=10, fontweight='bold')
plt.setp(autotexts, size=10, fontweight='bold', color='black')

# Add a legend to the chart
ax.legend(
    wedges, energy_sources,
    title="Energy Sources",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Set the title, split across two lines for better readability
ax.set_title(
    'Techburg 2030:\nEnergy Consumption Breakdown',
    fontsize=16,
    fontweight='bold',
    color='darkgreen'
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()