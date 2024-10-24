import matplotlib.pyplot as plt
import numpy as np

# Define energy sources and their respective proportions
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
proportions = np.array([40, 25, 15, 10, 10])

# Define colors for each segment
colors = ['#FFD700', '#00BFFF', '#7CFC00', '#FF8C00', '#8B4513']

# Create the pie chart with a hole in the center (donut chart)
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    proportions,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=(0.1, 0, 0, 0, 0),  # Slightly highlight the Solar segment
    shadow=True  # Add shadow for depth
)

# Draw circle for donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Style labels
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=10, color="darkblue")

# Add a legend outside the plot area
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Title with backstory context, split into two lines for better readability
ax.set_title("GreenTown's Renewable Energy Mix\nin 2023", fontsize=14, fontweight='bold', color='darkgreen')

# Final adjustments to prevent label overlap and improve layout
plt.tight_layout()

# Show the plot
plt.show()