import matplotlib.pyplot as plt
import numpy as np

# Data for the line chart
decades = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
average_heights = np.array([80, 120, 150, 170, 180, 200, 300, 350, 400, 450, 500, 600, 650])

# Data for the bar chart
num_skyscrapers = np.array([10, 15, 20, 30, 25, 40, 55, 70, 90, 110, 130, 150, 180])

# Create subplots
fig, ax1 = plt.subplots(1, 2, figsize=(18, 7), sharex=True)

# Line chart (average heights)
ax1[0].plot(decades, average_heights, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8)
ax1[0].set_title('Evolution of Skyscraper Heights\nOver the 20th and 21st Centuries', fontsize=16, fontweight='bold', pad=20)
ax1[0].set_xlabel('Decade', fontsize=12)
ax1[0].set_ylabel('Average Height of Tallest Skyscraper (meters)', fontsize=12)
ax1[0].set_xticks(decades)
ax1[0].set_yticks(np.arange(0, 701, step=50))
ax1[0].grid(True, linestyle='--', alpha=0.5)
ax1[0].legend(['Average Height'], loc='upper left', fontsize=10)

# Annotate key milestones
milestones = {'1900s': 80, '1960s': 300, '2010s': 600}
for decade, height in milestones.items():
    ax1[0].annotate(f'{decade}: {height}m', xy=(int(decade[:-1] + '0'), height), xytext=(-40, 10),
                 textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Bar chart (number of skyscrapers)
ax1[1].bar(decades, num_skyscrapers, color='skyblue', width=8)
ax1[1].set_title('Number of Skyscrapers Built\nEach Decade', fontsize=16, fontweight='bold', pad=20)
ax1[1].set_xlabel('Decade', fontsize=12)
ax1[1].set_ylabel('Number of Skyscrapers', fontsize=12)
ax1[1].set_yticks(np.arange(0, 201, step=20))
ax1[1].legend(['Number of Skyscrapers'], loc='upper left', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Display the plots
plt.show()