import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
energy_sources = ['Wind', 'Solar', 'Hydroelectric', 'Biomass', 'Geothermal']
percentages = np.array([35, 30, 20, 10, 5])

# Colors for each sector
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Explode the 'Wind' sector slightly for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.3),
    pctdistance=0.85,
    textprops={'fontsize': 12}
)

# Make the percentage text bold and white for better contrast
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Title of the chart with line break for readability
ax.set_title('Renewable Energy Mix\nin Europe: 2023', fontsize=16, fontweight='bold', pad=20)

# Draw a circle at the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Use tight_layout() to adjust layout for better readability
plt.tight_layout()

# Display the plot
plt.show()