import matplotlib.pyplot as plt
import squarify

# Data representing energy generation by source (in GWh)
renewable_data = {
    'North America': {'Solar': 300, 'Wind': 500, 'Hydro': 700, 'Biomass': 200},
    'South America': {'Solar': 200, 'Wind': 300, 'Hydro': 600, 'Biomass': 150},
    'Europe': {'Solar': 400, 'Wind': 700, 'Hydro': 500, 'Biomass': 250},
    'Africa': {'Solar': 250, 'Wind': 150, 'Hydro': 300, 'Biomass': 100},
    'Asia': {'Solar': 600, 'Wind': 800, 'Hydro': 900, 'Biomass': 300},
    'Oceania': {'Solar': 150, 'Wind': 100, 'Hydro': 250, 'Biomass': 80}
}

# Flatten data for squarify
labels = []
values = []
colors = []
base_colors = {
    'Solar': '#FFDD44',
    'Wind': '#77CCAA',
    'Hydro': '#44BBFF',
    'Biomass': '#99AA88'
}

for continent, sources in renewable_data.items():
    for source, value in sources.items():
        labels.append(f'{continent}\n{source}\n{value} GWh')
        values.append(value)
        colors.append(base_colors[source])

# Plotting the treemap
plt.figure(figsize=(14, 10))
squarify.plot(sizes=values, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold', 'wrap': True})

# Title and labels
plt.title('Global Renewable Energy Sources Distribution\nContinent-wise Contribution in GWh', fontsize=18, fontweight='bold', pad=30)
plt.axis('off')

# Adjust layout to prevent label overlapping
plt.tight_layout()

# Display the plot
plt.show()