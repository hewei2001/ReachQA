import matplotlib.pyplot as plt
import numpy as np

# Data for the exoplanet temperature variations
exoplanet_temperatures = {
    "Zeta-1": [-150, -100, -50, 0, 50, 100],
    "Omega-3": [-200, -150, -120, -70, -20, 30],
    "Alpha-7": [50, 70, 90, 110, 130, 150],
    "Theta-5": [-100, -75, -50, -30, -10, 10],
    "Lambda-9": [-50, 0, 50, 100, 150, 200]
}

# Prepare data for the box plot
data = list(exoplanet_temperatures.values())
labels = list(exoplanet_temperatures.keys())

# Create a figure with subplots
fig, ax = plt.subplots(1, 1, figsize=(14, 9))

# Create a box plot
box = ax.boxplot(data, vert=True, patch_artist=True, labels=labels, notch=True, widths=0.5)

# Add additional elements: violin plot to show density
violin = ax.violinplot(data, showmeans=False, showmedians=False)

# Customize the plot
ax.set_title("Temperature Variations Across Exoplanets\nin Different Star Systems", fontsize=16)
ax.set_ylabel("Temperature (°C)", fontsize=12)
ax.set_xlabel("Star Systems", fontsize=12)
ax.set_ylim(-250, 250)

# Apply colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, and medians
plt.setp(box['whiskers'], color='grey', linestyle='--')
plt.setp(box['caps'], color='grey')
plt.setp(box['medians'], color='black', linewidth=1.5)

# Gridlines for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotate median values on the box plot
for i, line in enumerate(box['medians']):
    x, y = line.get_xydata()[1]  # Median x, y values
    ax.annotate(f'{y:.1f}', xy=(x, y), xytext=(0, 5), textcoords='offset points', fontsize=10, color='black', ha='center')

# Enhance legend
legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=label) for color, label in zip(colors, labels)]
ax.legend(handles=legend_elements, loc='upper right', title='Star Systems', fontsize=10)

# Apply tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()