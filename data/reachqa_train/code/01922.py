import matplotlib.pyplot as plt
import numpy as np

# Define continents and renewable energy data as percentage contributions
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
renewable_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']

# Hypothetical percentage data for each continent
renewable_data = np.array([
    [40, 25, 30, 3, 2],
    [35, 15, 40, 5, 5],
    [20, 35, 25, 10, 10],
    [25, 30, 30, 5, 10],
    [15, 20, 50, 5, 10],
    [45, 30, 10, 10, 5]
])

# Additional data for new plot: total renewable energy growth rates (hypothetical values)
growth_rates = np.array([5.0, 6.2, 4.1, 3.5, 7.0, 5.8])  # Growth rates in percentage

# Define colors for each renewable source
colors = plt.cm.Paired(np.arange(len(renewable_sources)))

# Initialize the figure with two subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
fig.subplots_adjust(wspace=0.4)

# First subplot: Stacked bar chart
ax1 = axs[0]
for i, (continent, data) in enumerate(zip(continents, renewable_data)):
    bottom = 0
    for j, (source, percent) in enumerate(zip(renewable_sources, data)):
        ax1.barh(continent, percent, color=colors[j], edgecolor='black', left=bottom, label=source if i == 0 else "")
        ax1.text(bottom + percent / 2, i, f'{percent}%', va='center', ha='center', fontsize=9, color='black', weight='bold')
        bottom += percent

ax1.set_title("2023 Renewable Energy Adoption\nAcross Continents by Source", fontsize=14, fontweight='bold')
ax1.set_xlabel("Percentage (%)", fontsize=12)
ax1.set_ylabel("Continent", fontsize=12)
ax1.set_xlim(0, 100)

# Add legend
handles, labels = ax1.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax1.legend(by_label.values(), by_label.keys(), loc='upper left', title="Energy Source", bbox_to_anchor=(1, 1))

# Customize grid
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.yaxis.grid(False)

# Second subplot: Line plot for growth rates
ax2 = axs[1]
ax2.plot(continents, growth_rates, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8)
ax2.set_title("Growth Rate of Renewable Energy\nAdoption by Continent (2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Continent", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)
ax2.set_ylim(0, 10)
ax2.grid(True, linestyle='--', alpha=0.6)

# Annotate growth rates
for continent, growth in zip(continents, growth_rates):
    ax2.text(continent, growth + 0.3, f'{growth}%', ha='center', va='bottom', fontsize=9, color='black')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()