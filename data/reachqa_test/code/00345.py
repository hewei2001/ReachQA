import matplotlib.pyplot as plt
import numpy as np

# Define a more extensive set of solar panel types, including emerging technologies
solar_panel_types = [
    'Monocrystalline', 'Polycrystalline', 'Thin Film', 'BIPV',
    'Bifacial', 'PERC', 'Cadmium Telluride', 'Copper Indium Gallium Selenide'
]

# Hypothetical energy contribution percentages (summing to 100%)
energy_distribution = [20, 18, 15, 12, 10, 8, 9, 8]

# Additional hypothetical efficiency percentages for each type
efficiency_scores = [22, 18, 14, 16, 19, 20, 11, 13]

# Colors for different solar panel types
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 
          '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2']

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Donut Pie Chart for Energy Distribution
wedges, texts, autotexts = axs[0].pie(
    energy_distribution,
    labels=solar_panel_types,
    colors=colors,
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    autopct='%1.1f%%',
    textprops={'fontsize': 10},
    explode=[0.05 if i == 2 else 0 for i in range(len(solar_panel_types))],  # Highlight Thin Film
    shadow=True
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axs[0].add_artist(centre_circle)

for text in texts:
    text.set_color('grey')
    text.set_fontsize(9)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(9)
    autotext.set_weight('bold')

axs[0].set_title(
    "Solar Panel Energy Distribution\nin EcoSmart City, 2025", 
    fontsize=14, fontweight='bold', pad=20
)
axs[0].axis('equal')

axs[0].legend(
    wedges, solar_panel_types, title='Solar Panel Types', 
    loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9
)

axs[0].text(
    0, 0, 'EcoSmart\nCity 2025', horizontalalignment='center', 
    verticalalignment='center', fontsize=12, color='black', fontweight='bold'
)

# Bar Chart for Efficiency Scores
bar_width = 0.4
x_positions = np.arange(len(solar_panel_types))

axs[1].bar(x_positions, efficiency_scores, color=colors, width=bar_width, edgecolor='grey')
axs[1].set_title("Efficiency Scores of Solar Panels", fontsize=14, fontweight='bold')
axs[1].set_xlabel('Solar Panel Types', fontsize=12)
axs[1].set_ylabel('Efficiency (%)', fontsize=12)
axs[1].set_xticks(x_positions)
axs[1].set_xticklabels(solar_panel_types, rotation=45, ha='right')

# Display values on top of bars
for i, value in enumerate(efficiency_scores):
    axs[1].text(i, value + 0.5, f'{value}%', ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()