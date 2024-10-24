import matplotlib.pyplot as plt
import numpy as np

# Define a larger set of countries and renewable energy sources
countries = ['Germany', 'France', 'Spain', 'Italy', 'Sweden', 'Norway', 'Denmark', 'Netherlands']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal', 'Tidal']

# Percentage contribution of each energy source per country for the current year
data_current = np.array([
    [30, 40, 20, 8, 2, 0],   # Germany
    [25, 35, 30, 9, 1, 0],   # France
    [45, 30, 15, 9, 1, 0],   # Spain
    [35, 25, 20, 18, 2, 0],  # Italy
    [20, 25, 35, 15, 5, 0],  # Sweden
    [5, 10, 50, 30, 5, 0],   # Norway
    [10, 50, 20, 15, 5, 0],  # Denmark
    [30, 20, 25, 20, 5, 0]   # Netherlands
])

# Transpose for easier plotting
data_current = data_current.T

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#228B22', '#8B4513', '#FF6347', '#4682B4']

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Initialize bottoms for stacking
bottoms = np.zeros(len(countries))
for i, (source, color) in enumerate(zip(energy_sources, colors)):
    ax.bar(countries, data_current[i], bottom=bottoms, color=color, label=source)
    bottoms += data_current[i]

# Adding title with multiline
ax.set_title('Renewable Energy Sources Contribution\nAcross Various European Countries in the Current Year', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Countries', fontsize=12)
ax.set_ylabel('Percentage of Total Renewable Energy', fontsize=12)
ax.set_ylim(0, 100)

# Adding y-axis grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Adding legend at a strategic location
ax.legend(title='Energy Sources', loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3, frameon=False)

# Add percentage labels with color contrast adjustment
for i, country in enumerate(countries):
    cumulative = 0
    for j, (source, color) in enumerate(zip(energy_sources, colors)):
        percentage = data_current[j, i]
        cumulative += percentage
        text_color = 'white' if percentage > 10 else 'black'
        ax.text(i, cumulative - percentage / 2, f'{percentage}%', ha='center', va='center', color=text_color, fontsize=9, fontweight='bold')

# Conditional formatting example - highlight countries with > 40% wind energy
for i, country in enumerate(countries):
    wind_percentage = data_current[1, i]  # Wind is at index 1
    if wind_percentage > 40:
        ax.text(i, 105, 'High Wind', ha='center', fontsize=10, color='red')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()