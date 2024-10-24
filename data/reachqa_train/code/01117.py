import matplotlib.pyplot as plt
import numpy as np

# Data for the energy distribution in Wonderland
energy_sources = ['Solar Power', 'Wind Power', 'Hydro Power', 'Geothermal', 'Biomass']
energy_percentages = [35, 25, 20, 10, 10]

# Colors associated with each energy source
colors = ['#ffd700', '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']

# Explode the solar power slice for emphasis
explode = (0.1, 0, 0, 0, 0)

# Additional data for a bar chart showing the growth of energy production
years = [2018, 2019, 2020, 2021, 2022]
solar_growth = [300, 320, 340, 360, 380]
wind_growth = [200, 210, 220, 230, 240]
hydro_growth = [150, 150, 155, 160, 165]
geothermal_growth = [80, 85, 90, 95, 100]
biomass_growth = [70, 75, 80, 85, 90]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Donut Chart
wedges, texts, autotexts = ax1.pie(
    energy_percentages, 
    explode=explode, 
    labels=energy_sources, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.axis('equal')
ax1.set_title('Renewable Energy Landscape in Wonderland:\nDistribution of Energy Sources', fontsize=16, weight='bold', pad=20)
ax1.legend(wedges, energy_sources, title="Energy Sources", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Bar Chart
width = 0.15
indices = np.arange(len(years))
ax2.bar(indices - 2*width, solar_growth, width, label='Solar Power', color=colors[0])
ax2.bar(indices - width, wind_growth, width, label='Wind Power', color=colors[1])
ax2.bar(indices, hydro_growth, width, label='Hydro Power', color=colors[2])
ax2.bar(indices + width, geothermal_growth, width, label='Geothermal', color=colors[3])
ax2.bar(indices + 2*width, biomass_growth, width, label='Biomass', color=colors[4])

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Energy Production (GWh)', fontsize=12)
ax2.set_title('Growth of Renewable Energy Production in Wonderland', fontsize=14)
ax2.set_xticks(indices)
ax2.set_xticklabels(years)
ax2.legend(title="Energy Sources")

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()