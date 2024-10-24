import matplotlib.pyplot as plt

# Extended energy sources with fractional data
energy_sources = [
    'Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Nuclear Energy', 
    'Natural Gas', 'Coal', 'Geothermal', 'Tidal', 'Wave Energy', 'Other'
]
production_percentages = [22.5, 18.0, 12.0, 8.5, 14.5, 6.7, 4.8, 3.0, 2.5, 3.0, 4.0]

# Corresponding colors for energy sources
colors = [
    '#FFD700', '#87CEEB', '#00CED1', '#32CD32', '#8A2BE2', 
    '#FF6347', '#A9A9A9', '#FFDEAD', '#4682B4', '#5F9EA0', '#D3D3D3'
]

# Set figure size and layout
plt.figure(figsize=(12, 8))

# Create a multi-layered doughnut chart
wedges, texts, autotexts = plt.pie(
    production_percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90, 
    colors=colors, explode=[0.1 if i == 0 else 0 for i in range(len(energy_sources))], 
    shadow=True, pctdistance=0.85
)

# Draw a circle in the center to make it a doughnut chart
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Improve the pie chart appearance
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=8)

# Title with line breaks for better readability
plt.title(
    'Complex Energy Production Breakdown\nin EnergiaLand: 2023', 
    fontsize=16, fontweight='bold', pad=20
)

# Positioning the legend with a more comprehensive view
plt.legend(
    wedges, energy_sources, title="Energy Sources", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Ensure layout is clear and not overlapping
plt.tight_layout()

# Show the chart
plt.show()