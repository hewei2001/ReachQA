import matplotlib.pyplot as plt

# Data for renewable energy sources and their respective percentages
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Biomass', 'Geothermal']
percentages = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513', '#FF4500']

# Create a ring chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='w'),
    textprops=dict(color="darkslategray", weight='bold')
)

# Add a circle at the center to transform the pie chart into a ring chart
center_circle = plt.Circle((0, 0), 0.6, fc='white')
fig.gca().add_artist(center_circle)

# Adjust properties of the texts for better readability
plt.setp(autotexts, size=10, weight='bold', color='navy')
plt.setp(texts, size=12, weight='bold')

# Title and central label
plt.title(
    "Greenfield City's 2023 Green Energy Initiative\nDistribution of Renewable Energy Sources",
    fontsize=14, weight='bold', color='darkgreen', pad=20
)

# Adding a central label within the ring
ax.text(0, 0, 'Green Energy\n2023', horizontalalignment='center', verticalalignment='center',
        fontsize=12, color='darkgreen', weight='bold')

# Move legend outside of the plot area
ax.legend(wedges, energy_sources,
          title="Energy Sources",
          loc='center left',
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=10)

# Ensure layout is adjusted
plt.tight_layout()

# Display the ring chart
plt.show()