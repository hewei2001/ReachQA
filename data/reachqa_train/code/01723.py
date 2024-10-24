import matplotlib.pyplot as plt
import numpy as np

# Define artificial spectral data for each star type, tweaked for better visual representation
red_dwarfs = [1.1, 1.3, 1.2, 1.4, 1.2, 1.5, 1.3, 1.6, 1.4]
sun_like_stars = [2.3, 2.6, 2.5, 2.7, 2.4, 2.8, 2.7, 2.9, 2.5]
giants = [3.1, 3.5, 3.4, 3.3, 3.2, 3.6, 3.5, 3.7, 3.4]
supergiants = [4.2, 4.5, 4.4, 4.3, 4.6, 4.5, 4.7, 4.4, 4.8]

# Prepare data for the horizontal box plot
data = [red_dwarfs, sun_like_stars, giants, supergiants]
labels = ["Red Dwarfs", "Sun-like Stars", "Giants", "Supergiants"]

# Create the horizontal box plot with customized appearance
fig, ax = plt.subplots(figsize=(12, 7))
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5,
                boxprops=dict(facecolor='lightblue', color='navy', linewidth=1.5),
                whiskerprops=dict(color='navy', linewidth=1.5),
                capprops=dict(color='navy', linewidth=1.5),
                medianprops=dict(color='red', linewidth=1.5))

# Color each box differently for distinction
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'gold']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add title and labels with adjusted font sizes
ax.set_title("Stellar Spectra Analysis:\nLight Emission Profiles of Various Star Types",
             fontsize=14, fontweight='bold')
ax.set_xlabel("Spectral Intensity", fontsize=12)
ax.set_yticklabels(labels, fontsize=12)

# Automatically adjust layout to prevent any overlap
plt.tight_layout()

# Show the plot
plt.show()