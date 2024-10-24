import matplotlib.pyplot as plt
import numpy as np

# Define years and countries
years = np.arange(2023, 2029)
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']

# Renewable energy sources data in percentages
solar = np.array([
    [10, 15, 20, 25, 30, 35],  # Country A
    [5, 10, 15, 20, 25, 30],   # Country B
    [8, 12, 18, 23, 28, 34],   # Country C
    [12, 17, 22, 28, 33, 38],  # Country D
    [7, 13, 19, 24, 30, 36]    # Country E
])

wind = np.array([
    [15, 20, 25, 30, 35, 40],  # Country A
    [12, 16, 22, 27, 32, 37],  # Country B
    [10, 15, 20, 27, 33, 38],  # Country C
    [18, 24, 30, 35, 40, 45],  # Country D
    [11, 17, 23, 28, 33, 39]   # Country E
])

hydro = np.array([
    [20, 25, 28, 32, 35, 40],  # Country A
    [18, 23, 28, 32, 36, 41],  # Country B
    [14, 20, 24, 30, 36, 42],  # Country C
    [16, 21, 27, 33, 38, 44],  # Country D
    [19, 24, 29, 34, 38, 44]   # Country E
])

# Calculate total renewable energy for each year across all countries
total_renewable = solar + wind + hydro
annual_totals = total_renewable.sum(axis=0)

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# Bar plot for renewable energy by country
bar_width = 0.15
x_indexes = np.arange(len(years))
colors = ['#FFD700', '#4169E1', '#32CD32']  # Solar, Wind, Hydro

for i, country in enumerate(countries):
    ax1.bar(x_indexes + i * bar_width, solar[i], width=bar_width, color=colors[0], alpha=0.8)
    ax1.bar(x_indexes + i * bar_width, wind[i], width=bar_width, bottom=solar[i], color=colors[1], alpha=0.8)
    ax1.bar(x_indexes + i * bar_width, hydro[i], width=bar_width, bottom=solar[i] + wind[i], color=colors[2], alpha=0.8)

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Renewable Energy Usage (%)', fontsize=12)
ax1.set_title('Projected Renewable Energy Adoption\n(2023-2028) Across Five Countries', fontsize=14, fontweight='bold')
ax1.set_xticks(x_indexes + bar_width * 2)
ax1.set_xticklabels(years)

# Add legend
handles = [plt.Rectangle((0,0),1,1, color=color, alpha=0.8) for color in colors]
ax1.legend(handles, ['Solar', 'Wind', 'Hydro'], loc='upper left', fontsize=10, title='Energy Source')

# Grid settings
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Line plot for cumulative renewable energy usage
ax2.plot(years, annual_totals, marker='o', color='#FF6347', linewidth=2, label='Total Renewable Usage')

# Add annotations to the line plot for each year
for (year, total) in zip(years, annual_totals):
    ax2.text(year, total + 2, f'{total}', ha='center', fontsize=9, color='#FF6347')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Total Renewable Energy (%)', fontsize=12)
ax2.set_title('Cumulative Renewable Energy Growth\n(2023-2028)', fontsize=14, fontweight='bold')

ax2.set_xticks(years)
ax2.set_xticklabels(years)
ax2.legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()
plt.show()