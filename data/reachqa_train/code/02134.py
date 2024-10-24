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

# Calculate percentage change relative to the previous year
percentage_change = np.diff(urban_parks_area, axis=1) / urban_parks_area[:, :-1] * 100

# Set the positions of the bars
bar_width = 0.15
x = np.arange(len(years))

# Create the subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# First subplot: Bar Chart
for i, city in enumerate(cities):
    axs[0].bar(x + i * bar_width, urban_parks_area[i], width=bar_width, label=city, color=colors[i])

axs[0].set_title('Expansion of Urban Parks\n(2019-2023)', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Year', fontsize=13)
axs[0].set_ylabel('Area (Hectares)', fontsize=13)
axs[0].set_xticks(x + bar_width * 2)
axs[0].set_xticklabels(years)
axs[0].legend(title='Cities', fontsize=10, title_fontsize='11')
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations for bar chart
for i in range(len(cities)):
    for j in range(len(years)):
        axs[0].text(x[j] + i * bar_width, urban_parks_area[i, j] + 0.5, str(urban_parks_area[i, j]), ha='center', va='bottom', fontsize=9)

# Second subplot: Line Plot
for i, city in enumerate(cities):
    axs[1].plot(years[1:], percentage_change[i], marker='o', label=city, color=colors[i])

axs[1].set_title('Yearly Percentage Increase in Urban Park Area', fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel('Year', fontsize=13)
axs[1].set_ylabel('Percentage Change (%)', fontsize=13)
axs[1].set_xticks(years[1:])
axs[1].legend(title='Cities', fontsize=10, title_fontsize='11')
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations for line plot
for i in range(len(cities)):
    for j in range(len(percentage_change[i])):
        axs[1].text(years[j+1], percentage_change[i, j] + 1, f'{percentage_change[i, j]:.1f}%', ha='center', va='bottom', fontsize=9)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()