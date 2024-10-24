import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as PathEffects

# Define continents and renewable energy sources
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Bioenergy']

# Define the percentage adoption for each energy source by continent
data = {
    'Africa': [35, 25, 30, 5, 5],
    'Asia': [20, 30, 40, 5, 5],
    'Europe': [30, 35, 15, 10, 10],
    'North America': [25, 40, 20, 10, 5],
    'South America': [10, 20, 60, 5, 5],
    'Oceania': [40, 30, 20, 5, 5]
}

# Gradient colors for each energy source
colors = [
    ('#ffcc00', '#ffd700'),  # Solar
    ('#6699cc', '#336699'),  # Wind
    ('#99cc00', '#66ff33'),  # Hydro
    ('#ff9966', '#ff6347'),  # Geothermal
    ('#9966cc', '#8a2be2')   # Bioenergy
]

fig, ax = plt.subplots(figsize=(14, 8), dpi=100)

cumulative = np.zeros(len(continents))

for i, energy in enumerate(energy_sources):
    values = [data[continent][i] for continent in continents]

    # Use gradient color effect
    bars = ax.bar(
        continents, values, bottom=cumulative,
        label=energy,
        color=[colors[i][0]], edgecolor='white',
        path_effects=[PathEffects.withStroke(linewidth=2, foreground='black')]
    )

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_y() + bar.get_height() / 2,
            f'{value}%',
            ha='center', va='center', fontsize=10, color='white',
            path_effects=[PathEffects.withStroke(linewidth=3, foreground='black')]
        )

    cumulative += values

# Add a background grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

ax.set_ylim(0, 100)

# Title with potential line break
ax.set_title('Green Energy Adoption Across Continents\nAnalyzed by Energy Source', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Continent', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))

# Optimized layout with legend outside
ax.legend(title='Energy Source', bbox_to_anchor=(1.05, 1), loc='upper left', frameon=False)

# Ensure layout is optimized
plt.tight_layout()

# Show the plot
plt.show()