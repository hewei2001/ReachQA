import matplotlib.pyplot as plt
import numpy as np

# Define the data for the ring chart (donut chart)
energy_sources = ['Solar Energy', 'Wind Energy', 'Biomass Energy', 'Hydropower', 'Other Renewables']
percentages = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#00BFFF', '#8B4513', '#228B22', '#FF69B4']

# Define data for the bar chart
years = np.arange(2020, 2026)
solar = [30, 32, 34, 35, 36, 38]
wind = [22, 23, 24, 25, 26, 27]
biomass = [18, 19, 19, 20, 20, 20]
hydropower = [12, 13, 14, 15, 15, 15]
other_renewables = [5, 5, 5, 5, 5, 5]

# Create the figure with two subplots: 1x2 grid
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Donut chart
wedges, texts, autotexts = axs[0].pie(
    percentages, 
    labels=energy_sources, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axs[0].add_artist(centre_circle)
axs[0].set_title('GreenTech 2025: Renewable Energy Share\nin FutureCity', fontsize=14, fontweight='bold')

plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=10)
axs[0].axis('equal')

axs[0].legend(wedges, energy_sources, title="Energy Sources", loc='center left', bbox_to_anchor=(1.3, 0.5), fontsize=10)
axs[0].annotate('Renewable\nFocus 2025', xy=(0, 0), fontsize=12, fontweight='bold', color='#444444', ha='center', va='center')

# Bar chart
width = 0.15
bar_positions = np.arange(len(years))

axs[1].bar(bar_positions - 2*width, solar, width, label='Solar', color='#FFD700')
axs[1].bar(bar_positions - width, wind, width, label='Wind', color='#00BFFF')
axs[1].bar(bar_positions, biomass, width, label='Biomass', color='#8B4513')
axs[1].bar(bar_positions + width, hydropower, width, label='Hydropower', color='#228B22')
axs[1].bar(bar_positions + 2*width, other_renewables, width, label='Other', color='#FF69B4')

axs[1].set_title('Yearly Growth in Renewable Energy Capacity', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Capacity (%)', fontsize=12)
axs[1].set_xticks(bar_positions)
axs[1].set_xticklabels(years)
axs[1].legend(title="Energy Sources", fontsize=10, loc='upper left')

plt.tight_layout()
plt.show()