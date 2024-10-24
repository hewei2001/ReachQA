import matplotlib.pyplot as plt
import numpy as np

# Data: Annual increase in hectares of green space in major cities from 2018 to 2023
cities = ['City A', 'City B', 'City C', 'City D', 'City E']
years = ['2018', '2019', '2020', '2021', '2022', '2023']
green_space_increase = np.array([
    [5, 8, 7, 6, 9, 10],  # City A
    [4, 5, 6, 5, 7, 8],   # City B
    [3, 4, 5, 6, 7, 9],   # City C
    [2, 3, 3, 4, 6, 7],   # City D
    [1, 2, 2, 3, 5, 6]    # City E
])

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Bar positioning and width
bar_width = 0.15
indices = np.arange(len(years))

# Plot each city's data
colors = ['#76c7c0', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
for i, city in enumerate(cities):
    ax.bar(
        indices + i * bar_width,
        green_space_increase[i],
        bar_width,
        label=city,
        color=colors[i],
        alpha=0.8
    )

# Add annotations above bars
for i, city_data in enumerate(green_space_increase):
    for j, value in enumerate(city_data):
        ax.text(
            j + i * bar_width,
            value + 0.3,
            f'{value}',
            ha='center',
            va='bottom',
            fontsize=10,
            color='black'
        )

# Customize plot appearance
ax.set_title('Annual Increase in Urban Green Spaces\nMajor Cities (2018-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Increase in Green Space (Hectares)', fontsize=14)
ax.set_xticks(indices + 2 * bar_width)
ax.set_xticklabels(years)
ax.legend(title="Cities", title_fontsize='13', fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Enhance layout and display
plt.tight_layout()
plt.show()