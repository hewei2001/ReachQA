import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data for the plot
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
green_spaces = {
    "New York": np.array([200, 220, 260, 300, 350, 400]),
    "London": np.array([150, 170, 190, 210, 230, 260]),
    "Tokyo": np.array([180, 200, 210, 240, 280, 310]),
    "Sydney": np.array([130, 160, 190, 220, 260, 300]),
    "Paris": np.array([110, 140, 160, 180, 210, 250])
}

# Colors for each city's area
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create an area chart with markers and gradients
fig, ax = plt.subplots(figsize=(14, 8))

for (city, data), color in zip(green_spaces.items(), colors):
    ax.fill_between(years, data, label=city, color=color, alpha=0.3)
    ax.plot(years, data, color=color, alpha=0.7, linewidth=2, marker='o', markersize=6)

# Customize the plot
ax.set_title("Growth of Urban Green Spaces Over a Decade:\nA Comparison of Major Cities", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Green Space (Hectares)", fontsize=12)
ax.set_xticks(years)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotations for significant growth years
highlight_points = [(2016, 300), (2020, 400)]
for year, height in highlight_points:
    ax.annotate(f'Peak: {height}', xy=(year, height), xytext=(year, height + 30),
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10, color='black')

# Adjust plot layout for better readability
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 450, 50))
plt.tight_layout()

# Custom legend with small icons
legend_elements = [Patch(facecolor=colors[i], label=list(green_spaces.keys())[i]) for i in range(len(colors))]
ax.legend(handles=legend_elements, title='Cities', fontsize=10, loc='upper left')

# Highlight specific years across all cities
for year in [2014, 2018]:
    ax.axvline(x=year, color='gray', linestyle='--', linewidth=1, alpha=0.5)

# Display the plot
plt.show()