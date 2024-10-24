import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from itertools import cycle

# Define years from 1980 to 2023
years = np.arange(1980, 2024)

# Artificial data representing perceived impact on language learning
# Extend data to match years length with some pattern changes
social_media_impact = np.array([2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 8, 7, 7, 7, 7, 8, 8, 9, 9, 9, 10])
video_conferencing_impact = np.array([1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10])
online_forums_impact = np.array([3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9])
instant_messaging_impact = np.array([1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10])
traditional_writing_impact = np.array([9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(20, 10), sharey=True)

# Labels for the new subplot
additional_methods = ["Podcasts", "Virtual Reality"]
additional_impacts = [
    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10]),
    np.array([2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9])
]

# Dictionary of method labels and their corresponding data
method_data = {
    'Social Media': social_media_impact,
    'Video Conferencing': video_conferencing_impact,
    'Online Forums': online_forums_impact,
    'Instant Messaging': instant_messaging_impact,
    'Traditional Writing': traditional_writing_impact,
}

# Plot settings
colors = cycle(['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta'])
markers = cycle(['o', 's', '^', 'D', '*', 'P'])

# Plotting original methods
for method, data in method_data.items():
    x_new = np.linspace(years.min(), years.max(), 500)
    smooth_data = make_interp_spline(years, data, k=3)(x_new)
    color = next(colors)
    marker = next(markers)
    ax[0].scatter(years, data, color=color, label=method, s=50, zorder=3, marker=marker)
    ax[0].plot(x_new, smooth_data, color=color, linestyle='-', alpha=0.5, zorder=2)

# Plotting additional methods
for idx, (method, data) in enumerate(zip(additional_methods, additional_impacts)):
    x_new = np.linspace(years.min(), years.max(), 500)
    smooth_data = make_interp_spline(years, data, k=3)(x_new)
    color = next(colors)
    marker = next(markers)
    ax[1].scatter(years, data, color=color, label=method, s=50, zorder=3, marker=marker)
    ax[1].plot(x_new, smooth_data, color=color, linestyle='-', alpha=0.5, zorder=2)

# Configure axes
for axi in ax:
    axi.set_xlabel('Year', fontsize=12)
    axi.set_ylabel('Perceived Impact on Language Learning (1 to 10)', fontsize=12)
    axi.set_xticks(years[::5])
    axi.set_xticklabels(years[::5], rotation=45)
    axi.set_ylim(0, 11)
    axi.grid(True, linestyle='--', alpha=0.5, zorder=1)
    axi.legend(loc='upper right', fontsize=10)

# Set titles
ax[0].set_title('Impact of Original Communication Methods\non Language Learning (1980-2023)', fontsize=14, pad=20)
ax[1].set_title('Impact of Additional Communication Methods\non Language Learning (1980-2023)', fontsize=14, pad=20)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()