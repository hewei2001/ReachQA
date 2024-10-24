import matplotlib.pyplot as plt
import numpy as np

# Define expanded types of renewable energy
energy_types = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal']

# Define percentage adoption for each energy type across different regions
# Ensure each category sums to 100% for every energy type
urban_adoption = [40, 20, 10, 5, 15, 10]
rural_adoption = [20, 25, 30, 10, 10, 5]
suburban_adoption = [25, 20, 15, 25, 5, 10]
industrial_adoption = [10, 15, 20, 30, 15, 20]
other_sources = [5, 20, 25, 30, 55, 55]

# Check that for each energy type, total adoption sums to 100%
assert all(sum(x) == 100 for x in zip(urban_adoption, rural_adoption, suburban_adoption, industrial_adoption, other_sources)), "Percentages must sum to 100."

# Create the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Define bar positions for grouped bars
bar_width = 0.15
x = np.arange(len(energy_types))

# Plot each category with stacked bars
p1 = ax.bar(x, urban_adoption, bar_width, label='Urban', color='lightblue')
p2 = ax.bar(x + bar_width, rural_adoption, bar_width, label='Rural', color='lightgreen')
p3 = ax.bar(x + 2*bar_width, suburban_adoption, bar_width, label='Suburban', color='lightyellow')
p4 = ax.bar(x + 3*bar_width, industrial_adoption, bar_width, label='Industrial', color='lightpink')
p5 = ax.bar(x + 4*bar_width, other_sources, bar_width, label='Other Sources', color='lightcoral')

# Annotate bars with percentage values
for bars in (p1, p2, p3, p4, p5):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                    xytext=(0, 0), textcoords='offset points', ha='center', va='center', fontsize=8)

# Customize the plot
ax.set_title("Renewable Energy Adoption Across Regions in 2023\nWith Diverse Energy Types", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Type of Renewable Energy", fontsize=12)
ax.set_ylabel("Percentage of Adoption (%)", fontsize=12)
ax.set_ylim(0, 100)
ax.set_xticks(x + 2*bar_width)
ax.set_xticklabels(energy_types, rotation=15, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Add legend
ax.legend(title='Regions', fontsize=10, title_fontsize=11, loc='upper right')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()