import matplotlib.pyplot as plt
import numpy as np

# Define the years and the cities
years = np.arange(2023, 2033)
cities = ['City of Azure', 'Metropolis Nova', 'Tech Haven', 'EcoVille', 'Cyber Heights']

# Projected population density growth (in thousands per square km) for each city
growth_data = np.array([
    [15, 16, 18, 20, 22, 23, 25, 27, 29, 31],
    [18, 19, 20, 22, 24, 26, 28, 29, 31, 33],
    [12, 14, 16, 17, 19, 21, 23, 25, 26, 28],
    [10, 12, 13, 15, 17, 19, 21, 22, 24, 26],
    [22, 24, 26, 27, 29, 31, 32, 34, 36, 38]
])

# Define variability in projection due to socio-economic factors
variability = np.array([
    [1.5, 1.4, 1.6, 1.8, 2.0, 1.7, 2.1, 2.3, 2.2, 2.5],
    [1.3, 1.5, 1.2, 1.7, 1.9, 2.0, 1.8, 2.2, 2.3, 2.4],
    [1.6, 1.4, 1.7, 1.5, 1.9, 2.1, 2.0, 2.3, 2.5, 2.2],
    [1.2, 1.3, 1.4, 1.6, 1.8, 2.1, 1.9, 2.0, 2.3, 2.1],
    [1.7, 1.9, 1.5, 1.8, 2.1, 2.4, 2.2, 2.5, 2.6, 2.7]
])

# Set up the plot
plt.figure(figsize=(14, 8))

# Color palette for cities
colors = ['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#9370DB']

# Different line styles for each city
line_styles = ['-', '--', '-.', ':', '-']

# Plot data with error bars for each city
for i, city in enumerate(cities):
    plt.errorbar(
        years, growth_data[i], yerr=variability[i],
        label=city, color=colors[i], linestyle=line_styles[i], linewidth=2, capsize=4, marker='o', alpha=0.9
    )

# Add annotations for maximum growth points
for i, city in enumerate(cities):
    max_index = np.argmax(growth_data[i])
    plt.annotate(
        f'Max: {growth_data[i, max_index]}k',
        xy=(years[max_index], growth_data[i, max_index]),
        xytext=(years[max_index] + 0.3, growth_data[i, max_index] + 2),
        arrowprops=dict(arrowstyle='->', color=colors[i]),
        fontsize=10
    )

# Customize plot
plt.title('Projected Population Density Growth\nof Future Cities (2023-2032)', fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Density Growth (thousands/sq km)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 41, 5))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Futuristic Cities', loc='upper left', fontsize=10)

# Highlight significant growth periods
for start, end in [(2025, 2026), (2030, 2031)]:
    plt.axvspan(start, end, color='gray', alpha=0.1)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()