import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2010, 2023)

# Artificial data for green space growth in square kilometers
city_data = {
    'Greenapolis': np.array([0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90]),
    'EcoCity': np.array([0, 1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89]),
    'SustainVille': np.array([0, 3, 6, 11, 17, 24, 32, 41, 51, 62, 74, 87, 101])
}

values = list(city_data.values())

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Define a diverging color scheme
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

# Plot the area chart with stacking and gradient effect
ax.stackplot(years, values, labels=city_data.keys(), colors=colors, alpha=0.8)

# Title and axis labels with line breaks for clarity
ax.set_title('Reimagining Urban Spaces:\nGreening Initiatives in Metropolitan Areas (2010-2022)',
             fontsize=16, fontweight='bold', ha='center')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Green Space (sq. km)', fontsize=12)

# Adding detailed annotations for significant changes
annotations = {
    'Greenapolis': 77,
    'EcoCity': 76,
    'SustainVille': 87
}

for city, space in annotations.items():
    ax.annotate(f"{city}: {space} sq.km", xy=(2021, space), xytext=(2016, space + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
                fontsize=10, fontweight='bold', color='darkslategray')

# Adding a secondary plot for percentage growth
percent_growth = [100 * (values[2][i] - values[2][0]) / values[2][0] for i in range(len(years))]
ax2 = ax.twinx()
ax2.plot(years, percent_growth, 'k--', linewidth=2, label='SustainVille Growth (%)')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='gray')
ax2.tick_params(axis='y', labelcolor='gray')
ax2.legend(loc='upper right', frameon=False)

# Adding a legend
ax.legend(loc='upper left', frameon=False)

# Enhanced grid for readability
ax.grid(linestyle='--', linewidth=0.7, alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()