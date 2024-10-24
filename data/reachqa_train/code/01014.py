import matplotlib.pyplot as plt
import numpy as np

# Define the types of coffee beans and continents
bean_types = ['Arabica', 'Robusta', 'Liberica', 'Excelsa']
continents = ['North America', 'Europe', 'Asia', 'Africa', 'South America']

# Number of coffee roasteries primarily using each bean type per continent
roastery_data = np.array([
    [200, 50, 20, 10],  # North America
    [180, 60, 25, 15],  # Europe
    [150, 80, 35, 20],  # Asia
    [90, 120, 40, 25],  # Africa
    [170, 70, 30, 15]   # South America
])

# Construct additional data for a new plot (Proportion of bean types over years for a continent)
years = np.arange(2018, 2024)
arabica_proportion = [0.6, 0.62, 0.64, 0.65, 0.67, 0.7]
robusta_proportion = [0.2, 0.18, 0.18, 0.17, 0.17, 0.15]
liberica_proportion = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
excelsa_proportion = [0.1, 0.1, 0.08, 0.08, 0.06, 0.05]

# Setup figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))

# Bar chart for roasteries by continent and bean type
bar_width = 0.18
x_indices = np.arange(len(continents))
colors = ['#8B4513', '#CD853F', '#DAA520', '#D2B48C']

for i, bean_type in enumerate(bean_types):
    ax1.bar(x_indices + i * bar_width, roastery_data[:, i], width=bar_width, label=bean_type, color=colors[i])

for i, continent_data in enumerate(roastery_data):
    for j, value in enumerate(continent_data):
        ax1.text(i + j * bar_width, value + 3, str(value), ha='center', va='bottom', fontsize=9, color='black')

ax1.set_xlabel('Continents', fontsize=12, labelpad=10)
ax1.set_ylabel('Number of Roasteries', fontsize=12, labelpad=10)
ax1.set_title('Coffee Roasteries by Bean Type\nacross Continents in 2023', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(x_indices + bar_width * 1.5)
ax1.set_xticklabels(continents, rotation=20)
ax1.legend(title='Coffee Bean Types', loc='upper right', bbox_to_anchor=(1.15, 1))
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)

# Stacked area chart for bean type proportions over years
ax2.stackplot(years, arabica_proportion, robusta_proportion, liberica_proportion, excelsa_proportion, labels=bean_types, colors=colors)
ax2.set_xlabel('Year', fontsize=12, labelpad=10)
ax2.set_ylabel('Proportion of Bean Types', fontsize=12, labelpad=10)
ax2.set_title('Proportion of Coffee Bean Types over Years\nin North America', fontsize=14, fontweight='bold', pad=15)
ax2.legend(title='Coffee Bean Types', loc='upper right')
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_xlim(years[0], years[-1])

# Adjust layout and display plot
plt.tight_layout()
plt.show()