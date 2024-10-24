import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Butterfly species
species = ['Monarch', 'Painted Lady', 'Red Admiral', 'Clouded Yellow']

# Years since the study began
years = np.array(range(1, 11))

# Migration distances for each species in km (hypothetical)
monarch_distances = np.array([2500, 2600, 2700, 2550, 2650, 2750, 2800, 2850, 2900, 2950])
painted_lady_distances = np.array([1100, 1150, 1200, 1180, 1190, 1250, 1300, 1340, 1380, 1400])
red_admiral_distances = np.array([700, 750, 780, 820, 860, 900, 920, 950, 980, 1000])
clouded_yellow_distances = np.array([400, 420, 430, 450, 470, 490, 500, 520, 540, 560])

# Colors and markers for each species
colors = ['orange', 'blue', 'red', 'green']
markers = ['o', '^', 's', 'd']  # circle, triangle, square, diamond

# New data for temperature over the years (hypothetical)
average_temperature = np.array([14, 15, 15.5, 16, 16.5, 17, 17.2, 17.5, 18, 18.5])

fig, ax = plt.subplots(1, 2, figsize=(15, 7), constrained_layout=True)

# Scatter Plot with Trendlines
for distances, color, marker, specie in zip(
    [monarch_distances, painted_lady_distances, red_admiral_distances, clouded_yellow_distances], 
    colors, 
    markers, 
    species
):
    ax[0].scatter(years, distances, color=color, marker=marker, s=100, label=specie)
    slope, intercept, _, _, _ = linregress(years, distances)
    ax[0].plot(years, slope*years + intercept, color=color, linestyle='--')

ax[0].set_title("Migratory Patterns of Butterflies:\nA Decade of Movement", fontsize=14)
ax[0].set_xlabel("Years Since Study Start", fontsize=12)
ax[0].set_ylabel("Migration Distance (km)", fontsize=12)
ax[0].legend(title='Butterfly Species', fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.6)

# Line Plot of Average Temperature Over Time
ax[1].plot(years, average_temperature, color='purple', marker='x', linestyle='-', linewidth=2, markersize=8)
ax[1].set_title("Average Yearly Temperature Over Time", fontsize=14)
ax[1].set_xlabel("Years Since Study Start", fontsize=12)
ax[1].set_ylabel("Average Temperature (°C)", fontsize=12)
ax[1].grid(True, linestyle='--', alpha=0.6)

plt.show()