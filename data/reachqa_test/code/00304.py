import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define bird species and their song duration and frequency data
species = ['Nightingale', 'Wood Thrush', 'Warbler', 'Finch', 'Sparrow']
song_durations = np.array([
    [30, 45, 55, 70, 85],  # Nightingale
    [25, 35, 40, 60, 70],  # Wood Thrush
    [20, 25, 30, 40, 55],  # Warbler
    [15, 20, 25, 35, 45],  # Finch
    [10, 15, 20, 25, 35]   # Sparrow
])
song_frequencies = np.array([
    [500, 520, 530, 550, 580],  # Nightingale
    [450, 460, 480, 510, 530],  # Wood Thrush
    [400, 420, 430, 460, 480],  # Warbler
    [380, 390, 405, 425, 445],  # Finch
    [370, 375, 390, 405, 420]   # Sparrow
])

# Define a quadratic function to fit the data
def quadratic_fit(x, a, b, c):
    return a * x ** 2 + b * x + c

# Compute average frequencies for the bar chart
avg_frequencies = [np.mean(freqs) for freqs in song_frequencies]

# Create subplots: scatter plot and bar chart
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Colors and markers for each species
colors = ['#FF6347', '#FFD700', '#32CD32', '#00CED1', '#9370DB']
markers = ['o', 's', '^', 'D', 'p']

# Scatter plot with curve fitting
ax1 = axes[0]
for i, (species_name, color, marker) in enumerate(zip(species, colors, markers)):
    ax1.scatter(song_durations[i], song_frequencies[i], label=species_name, color=color, s=100, marker=marker, alpha=0.7)
    popt, _ = curve_fit(quadratic_fit, song_durations[i], song_frequencies[i])
    x_fit = np.linspace(min(song_durations[i]), max(song_durations[i]), 100)
    y_fit = quadratic_fit(x_fit, *popt)
    ax1.plot(x_fit, y_fit, color=color, linestyle='--', linewidth=1)

ax1.set_title('The Whispering Forest:\nBird Songs and Their Frequencies', fontsize=16, fontweight='bold')
ax1.set_xlabel('Song Duration (seconds)', fontsize=14)
ax1.set_ylabel('Song Frequency (Hz)', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(title='Bird Species', fontsize=12)

# Bar chart for average frequencies
ax2 = axes[1]
ax2.bar(species, avg_frequencies, color=colors, alpha=0.7)
ax2.set_title('Average Song Frequency per Species', fontsize=16, fontweight='bold')
ax2.set_xlabel('Bird Species', fontsize=14)
ax2.set_ylabel('Average Frequency (Hz)', fontsize=14)

# Ensure layout is optimized to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()