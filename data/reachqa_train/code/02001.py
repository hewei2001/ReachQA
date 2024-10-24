import matplotlib.pyplot as plt
import numpy as np

# Define continents and decades
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa']
decades = ['2000s', '2010s', '2020s']

# Renewable energy adoption data in gigawatts for each continent over the decades
# Format: [[solar, wind, hydro], ...] for each continent
asia = [[30, 20, 50], [150, 100, 70], [300, 250, 120]]
europe = [[40, 60, 30], [200, 300, 50], [350, 500, 80]]
north_america = [[20, 40, 60], [180, 150, 100], [300, 320, 130]]
south_america = [[10, 10, 80], [50, 70, 90], [100, 150, 140]]
africa = [[5, 5, 20], [25, 30, 40], [80, 110, 60]]

data = [asia, europe, north_america, south_america, africa]

colors = ['#ffdd57', '#76c7c0', '#68a7ad']
sources = ['Solar', 'Wind', 'Hydroelectric']

fig, ax = plt.subplots(figsize=(14, 9))

x_offsets = np.linspace(-0.35, 0.35, len(continents))

# Plot each continent's data as stacked bars with gradient effect
for i, continent_data in enumerate(data):
    solar, wind, hydro = np.array(continent_data).T
    bar1 = ax.bar(np.arange(len(decades)) + x_offsets[i], solar, width=0.1, color=colors[0], 
                  label=sources[0] if i == 0 else "", alpha=0.8, edgecolor='darkorange')
    bar2 = ax.bar(np.arange(len(decades)) + x_offsets[i], wind, width=0.1, color=colors[1], 
                  label=sources[1] if i == 0 else "", alpha=0.8, bottom=solar, edgecolor='seagreen')
    bar3 = ax.bar(np.arange(len(decades)) + x_offsets[i], hydro, width=0.1, color=colors[2], 
                  label=sources[2] if i == 0 else "", alpha=0.8, bottom=solar+wind, edgecolor='steelblue')

    # Annotate each continent's total in the decade
    for j in range(len(decades)):
        ax.text(j + x_offsets[i], solar[j] + wind[j] + hydro[j] + 10, continents[i],
                ha='center', va='bottom', fontsize=8, weight='bold', color='black')

# Configure plot with a title
ax.set_title('Renewable Energy Adoption Across Continents:\nA Decadal Analysis (2000-2020)',
             fontsize=14, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Adoption (Gigawatts)', fontsize=12)
ax.set_ylim(0, 1000)
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, fontsize=12)

# Add gridlines for better visibility
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Add legend with a title
ax.legend(loc='upper left', fontsize=10, title='Energy Source', title_fontsize='12')

# Add a secondary subplot to show global trend
global_growth = [sum(s) for s in np.sum([asia, europe, north_america, south_america, africa], axis=0)]
ax2 = ax.twinx()
ax2.plot(decades, global_growth, color='darkred', linestyle='-', marker='o', markersize=8,
         linewidth=2, label='Global Trend')
ax2.set_ylabel('Global Total (Gigawatts)', fontsize=12, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')
ax2.legend(loc='upper center', fontsize=10)

plt.tight_layout()
plt.show()