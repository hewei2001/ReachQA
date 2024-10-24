import matplotlib.pyplot as plt
import numpy as np

# Define the continents and their respective eco-friendly initiatives percentages
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica']
initiatives = [
    'Renewable Energy', 'Recycling', 'Conservation', 
    'Sustainable Farming', 'Green Tech', 'Water Management', 
    'Pollution Reduction', 'Urban Greening'
]
percentages = np.array([
    [15, 12, 18, 8, 6, 10, 9, 22],  # Africa
    [25, 10, 20, 10, 7, 8, 12, 8],  # Asia
    [18, 25, 15, 8, 8, 10, 10, 6],  # Europe
    [15, 15, 20, 15, 10, 5, 10, 10],  # North America
    [20, 8, 16, 12, 10, 8, 10, 16],  # South America
    [10, 20, 15, 12, 8, 15, 10, 10],  # Oceania
    [10, 15, 10, 10, 15, 20, 10, 10]   # Antarctica
])

# Define color palette for each initiative
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Create a figure and axes for a single stacked bar chart
fig, ax = plt.subplots(figsize=(14, 10))
ind = np.arange(len(continents))

bottom = np.zeros(len(continents))

# Plot each initiative
for i in range(len(initiatives)):
    ax.bar(ind, percentages[:, i], bottom=bottom, color=colors[i], width=0.6, label=initiatives[i])
    bottom += percentages[:, i]

# Adding title and axis labels
ax.set_title('Eco-Friendly Initiatives by Continent\nDiversity and Impact in Environmental Sustainability', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Continents', fontsize=12, fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
ax.set_xticks(ind)
ax.set_xticklabels(continents, fontsize=11, rotation=15)

# Adding percentage labels on each segment
for i in range(len(percentages)):
    cumulative_percent = 0
    for j in range(len(initiatives)):
        cumulative_percent += percentages[i, j]
        ax.text(i, cumulative_percent - percentages[i, j] / 2, f'{percentages[i, j]}%', 
                ha='center', va='center', fontsize=8, color='white', fontweight='bold')

# Add legend
ax.legend(title='Eco-Friendly Initiatives', title_fontsize='12', loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()