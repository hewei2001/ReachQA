import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch

# Decades from 1970s to 2020s
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Popularity data for different instrument families as percentages
strings = np.array([30, 28, 25, 22, 20, 18])
percussion = np.array([20, 18, 20, 22, 24, 25])
brass = np.array([25, 22, 20, 18, 16, 15])
woodwind = np.array([15, 15, 15, 15, 15, 15])
electronic = np.array([10, 17, 20, 23, 25, 27])

# Stack the data for the area chart
instrument_data = np.vstack([strings, percussion, brass, woodwind, electronic])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the area chart with gradient colors
colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd']
labels = ['Strings', 'Percussion', 'Brass', 'Woodwind', 'Electronic']
stack_colors = [plt.cm.Blues, plt.cm.Oranges, plt.cm.Greens, plt.cm.Reds, plt.cm.Purples]

# Create the stacked area chart with shading
for i, (instrument, color_map) in enumerate(zip(instrument_data, stack_colors)):
    color = color_map(np.linspace(0.2, 0.8, 6))
    ax.fill_between(decades, instrument_data[:i+1].sum(axis=0), instrument_data[:i].sum(axis=0),
                    color=color, alpha=0.7, label=labels[i])

# Overlay trend lines with markers
for instrument, color in zip(instrument_data, colors):
    ax.plot(decades, instrument, color=color, linewidth=2, linestyle='--', marker='o', markersize=6)

# Customize plot
ax.set_title("Sound Waves Through Time:\nEvolution of Musical Instrument Preferences (1970s-2020s)",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Decade", fontsize=14)
ax.set_ylabel("Popularity (%)", fontsize=14)

# Add enhanced grid
ax.grid(linestyle='-.', alpha=0.5, color='grey')

# Rotate x-axis labels to align with decades
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 101, 10))

# Annotate with more insights
annotations = [
    (1980, 17, 'Rise of Electronic Music'),
    (2020, 27, 'Electronic Dominance'),
    (2000, 22, 'Growth in Percussion'),
    (1970, 30, 'Dominance of Strings')
]

for x, y, note in annotations:
    ax.annotate(note, xy=(x, y), xytext=(-30, -20 if y < 25 else 20),
                 textcoords='offset points', fontsize=10,
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

# Custom legend
ax.legend(loc='upper right', fontsize=10, title="Instrument Families")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()