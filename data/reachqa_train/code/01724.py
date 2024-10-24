import matplotlib.pyplot as plt
import numpy as np

# Define artificial spectral data for each star type, tweaked for better visual representation
red_dwarfs = [1.1, 1.3, 1.2, 1.4, 1.2, 1.5, 1.3, 1.6, 1.4]
sun_like_stars = [2.3, 2.6, 2.5, 2.7, 2.4, 2.8, 2.7, 2.9, 2.5]
giants = [3.1, 3.5, 3.4, 3.3, 3.2, 3.6, 3.5, 3.7, 3.4]
supergiants = [4.2, 4.5, 4.4, 4.3, 4.6, 4.5, 4.7, 4.4, 4.8]

# Create a related but different set of data for a violin plot
variation_factors = [0.5, 0.7, 0.6, 0.8, 0.6, 0.9, 0.7, 1.0, 0.9]
red_dwarfs_var = np.multiply(red_dwarfs, variation_factors)
sun_like_stars_var = np.multiply(sun_like_stars, variation_factors)
giants_var = np.multiply(giants, variation_factors)
supergiants_var = np.multiply(supergiants, variation_factors)

# Prepare data for the plots
box_plot_data = [red_dwarfs, sun_like_stars, giants, supergiants]
violin_plot_data = [red_dwarfs_var, sun_like_stars_var, giants_var, supergiants_var]
labels = ["Red Dwarfs", "Sun-like Stars", "Giants", "Supergiants"]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Horizontal box plot
axs[0].boxplot(box_plot_data, vert=False, patch_artist=True, notch=True, whis=1.5,
               boxprops=dict(facecolor='lightblue', color='navy', linewidth=1.5),
               whiskerprops=dict(color='navy', linewidth=1.5),
               capprops=dict(color='navy', linewidth=1.5),
               medianprops=dict(color='red', linewidth=1.5))

# Color each box differently for distinction
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'gold']
for patch, color in zip(axs[0].artists, colors):
    patch.set_facecolor(color)

# Titles and labels for the box plot
axs[0].set_title("Stellar Spectra Analysis:\nBox Plot of Light Emission Profiles", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Spectral Intensity", fontsize=12)
axs[0].set_yticks(np.arange(1, len(labels) + 1))
axs[0].set_yticklabels(labels, fontsize=12)

# Second subplot: Violin plot
violin_parts = axs[1].violinplot(violin_plot_data, vert=False, showmeans=False, showmedians=True)

# Color the violin plots
for pc, color in zip(violin_parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('navy')
    pc.set_alpha(0.7)

# Set color for median lines
violin_parts['cmedians'].set_color('red')
violin_parts['cmedians'].set_linewidth(1.5)

# Titles and labels for the violin plot
axs[1].set_title("Violin Plot of Light Emission Variability Across Star Types", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Spectral Intensity with Variability", fontsize=12)
axs[1].set_yticks(np.arange(1, len(labels) + 1))
axs[1].set_yticklabels(labels, fontsize=12)

# Adjust layout for both plots
plt.tight_layout()

# Show the plot
plt.show()