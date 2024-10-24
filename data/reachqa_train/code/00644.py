import matplotlib.pyplot as plt
import squarify

# Define data for the tree map
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania']
energy_sources = {
    'Solar': [25, 20, 30, 35, 20, 30],
    'Wind': [30, 35, 20, 25, 15, 40],
    'Hydro': [30, 25, 40, 20, 50, 20],
    'Biomass': [15, 20, 10, 20, 15, 10]
}

# Generate data structure for squarify
data = []
base_colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513']

for idx, region in enumerate(regions):
    for color_idx, (source, values) in enumerate(energy_sources.items()):
        label = f"{region} - {source}\n{values[idx]}%"
        color_intensity = 0.7 + (values[idx] / 100) * 0.3
        color = plt.cm.get_cmap('coolwarm')(color_intensity)[:3]
        data.append({'label': label, 'value': values[idx], 'color': color})

values = [item['value'] for item in data]
labels = [item['label'] for item in data]
colors = [item['color'] for item in data]

# Plotting the tree map
plt.figure(figsize=(16, 12))
ax = plt.gca()
squarify.plot(sizes=values, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 9, 'wrap': True})

# Titles and aesthetics
plt.title('Global Distribution of Renewable Energy Sources\nin 2023', fontsize=20, fontweight='bold')
plt.axis('off')

# Secondary plot (bar chart for visualizing total percentage per energy source)
plt.figure(figsize=(8, 6))
total_by_source = {source: sum(values) for source, values in energy_sources.items()}
sources = list(total_by_source.keys())
totals = list(total_by_source.values())
colors = [base_colors[i] for i in range(len(sources))]

plt.bar(sources, totals, color=colors)
plt.title('Total Renewable Energy by Source in 2023', fontsize=16, fontweight='bold')
plt.ylabel('Total Percentage (%)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()