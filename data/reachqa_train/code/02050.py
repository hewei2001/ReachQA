import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Define months as the x-axis (1 to 12 representing January to December)
months = np.arange(1, 13)

# Simulate light intensity data using a sinusoidal pattern with arbitrary units
base_intensity = 100  # Base intensity level
seasonal_variation = 15 * np.sin(2 * np.pi * (months - 1) / 12)  # Seasonal change
atmospheric_effects = np.array([5, -3, 2, -1, 6, -2, 4, -4, 3, -1, 2, 0])  # Other effects
light_intensity = base_intensity + seasonal_variation + atmospheric_effects

# Simulate a related variable, e.g., temperature changes
temperature_changes = 10 * np.cos(2 * np.pi * (months - 1) / 12) + np.array([1, -2, 3, -1, 1, -3, 2, 0, -2, 1, -1, 3])

# Create a color gradient based on light intensity
colors = cm.viridis((light_intensity - light_intensity.min()) / (light_intensity.max() - light_intensity.min()))

# Create the figure and axes with a secondary y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Plot the light intensity with color gradient
ax1.plot(months, light_intensity, marker='o', linestyle='-', linewidth=2, color='royalblue', label='Zoltar-5 Light Intensity')
for i in range(len(months)):
    ax1.plot(months[i], light_intensity[i], marker='o', color=colors[i], markersize=8)

# Plot the temperature on the secondary axis
ax2.plot(months, temperature_changes, marker='s', linestyle='--', linewidth=2, color='orange', label='Temperature Changes')

# Annotate the plot
for i, intensity in enumerate(light_intensity):
    if i % 2 == 0:  # Annotate every other month for clarity
        ax1.annotate(f'{intensity:.1f}', (months[i], intensity), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color='blue')

# Customize x-ticks to represent months
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Titles and labels
plt.title("Simulated Light Intensity Variations\nfrom Zoltar-5 Over One Earth Year\nand Corresponding Temperature Changes", fontsize=16, fontweight='bold')
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Light Intensity (Arbitrary Units)", fontsize=12, color='royalblue')
ax2.set_ylabel("Temperature Change (Degrees)", fontsize=12, color='orange')

# Add grid and shaded areas for better visual complexity
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.axvspan(3, 5, color='lightgrey', alpha=0.3, label='Spring Season')
ax1.axvspan(9, 11, color='lightblue', alpha=0.3, label='Autumn Season')

# Legend for both lines
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()