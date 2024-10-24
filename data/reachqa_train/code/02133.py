import matplotlib.pyplot as plt
import numpy as np

# Define cities and years
cities = ['Alphaville', 'Betatown', 'Gammaville', 'Deltacity', 'Epsilontown']
years = [2019, 2020, 2021, 2022, 2023]

# Data: Area of new urban parks developed (in hectares)
urban_parks_area = np.array([
    [10, 15, 20, 25, 30],  # Alphaville
    [5, 10, 15, 15, 20],   # Betatown
    [12, 18, 25, 22, 28],  # Gammaville
    [8, 12, 18, 20, 25],   # Deltacity
    [7, 9, 11, 15, 19]     # Epsilontown
])

# Set the positions of the bars
bar_width = 0.15
x = np.arange(len(years))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Colors for each city
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Create a bar for each city
for i, city in enumerate(cities):
    ax.bar(x + i * bar_width, urban_parks_area[i], width=bar_width, label=city, color=colors[i])

# Customize the plot
ax.set_title('Green Urban Spaces Initiative:\nExpansion of Urban Parks (2019-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Area of New Urban Parks (Hectares)', fontsize=13)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years)
ax.legend(title='Cities', fontsize=10, title_fontsize='11')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations on each bar for better insight
for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, urban_parks_area[i, j] + 0.5, str(urban_parks_area[i, j]), ha='center', va='bottom', fontsize=9)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()