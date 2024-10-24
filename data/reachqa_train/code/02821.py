import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Tree data (in thousands of trees) for each city
city_a_oaks = np.array([5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20])
city_a_maples = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
city_a_pines = np.array([2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9])
city_a_birches = np.array([1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9])

city_b_oaks = np.array([4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13])
city_b_maples = np.array([2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9])
city_b_pines = np.array([3, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10])
city_b_birches = np.array([2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8])

city_c_oaks = np.array([3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12])
city_c_maples = np.array([2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10])
city_c_pines = np.array([4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13])
city_c_birches = np.array([1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8])

# Colors for different tree species
colors = ['#8B4513', '#FF8C00', '#006400', '#8FBC8F']

# Create a figure and axes for subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 7), sharey=True)
fig.suptitle('Urban Forest Diversity: Predominant Tree Species in Major Cities (2010-2020)',
             fontsize=16, weight='bold')

# Plot stacked bar charts for each city
for ax, city, oaks, maples, pines, birches in zip(
    axes, ['City A', 'City B', 'City C'],
    [city_a_oaks, city_b_oaks, city_c_oaks],
    [city_a_maples, city_b_maples, city_c_maples],
    [city_a_pines, city_b_pines, city_c_pines],
    [city_a_birches, city_b_birches, city_c_birches]
):
    ax.bar(years, oaks, color=colors[0], label='Oaks')
    ax.bar(years, maples, bottom=oaks, color=colors[1], label='Maples')
    ax.bar(years, pines, bottom=oaks + maples, color=colors[2], label='Pines')
    ax.bar(years, birches, bottom=oaks + maples + pines, color=colors[3], label='Birches')

    ax.set_title(city)
    ax.set_xlabel('Year')
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45)
    ax.grid(True, linestyle='--', alpha=0.5)

axes[0].set_ylabel('Number of Trees (Thousands)')

# Add a legend
fig.legend(['Oaks', 'Maples', 'Pines', 'Birches'], loc='upper center', ncol=4, title='Tree Species', bbox_to_anchor=(0.5, 1.1))

# Adjust the layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()