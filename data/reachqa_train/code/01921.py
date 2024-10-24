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

# Define colors for each renewable source
colors = plt.cm.Paired(np.arange(len(renewable_sources)))

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create stacked bar chart
for i, (continent, data) in enumerate(zip(continents, renewable_data)):
    bottom = 0
    for j, (source, percent) in enumerate(zip(renewable_sources, data)):
        ax.barh(continent, percent, color=colors[j], edgecolor='black', left=bottom, label=source if i == 0 else "")
        # Label each segment with its percentage
        ax.text(bottom + percent / 2, i, f'{percent}%', va='center', ha='center', fontsize=9, color='black', weight='bold')
        bottom += percent

# Title and axis labels
ax.set_title("2023 Renewable Energy Adoption Across Continents\nPercentage Distribution by Source", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Percentage (%)", fontsize=12)
ax.set_ylabel("Continent", fontsize=12)

# Set x-axis range from 0 to 100
ax.set_xlim(0, 100)

# Add legend and adjust it
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper left', title="Energy Source", bbox_to_anchor=(1, 1))

# Customize grid to enhance readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)
ax.yaxis.grid(False)

# Ensure no overlap of visual elements
plt.tight_layout()

# Display the plot
plt.show()