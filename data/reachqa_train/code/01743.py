import matplotlib.pyplot as plt
import numpy as np

# Original data for each alien species: temperature (°C) and radiation levels (arbitrary units)
species_names = ['Zenithorans', 'Qoranians', 'Plasmexians', 'Nebulites', 'Astrotoids']
temperatures = np.array([30, 45, 60, 50, 40])
radiation_levels = np.array([120, 150, 110, 160, 130])

# Constructing a related dataset for the line plot overlay (e.g., a theoretical model)
theoretical_temperatures = np.linspace(25, 65, 100)
theoretical_radiation = 2 * theoretical_temperatures + 60  # Example linear relationship

# Custom markers and colors for scatter plot
markers = ['o', 's', 'D', '^', 'P']
colors = ['cyan', 'magenta', 'yellow', 'green', 'orange']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Scatter plot for each alien species
for i in range(len(species_names)):
    ax.scatter(temperatures[i], radiation_levels[i], 
               marker=markers[i], color=colors[i],
               s=200, label=species_names[i], 
               edgecolors='black', linewidth=1.5)

# Overlay plot for theoretical model
ax.plot(theoretical_temperatures, theoretical_radiation, 
        color='darkblue', linestyle='--', linewidth=2,
        label='Theoretical Radiation Model')

# Annotate the species with the highest radiation preference
max_radiation_index = np.argmax(radiation_levels)
ax.annotate('Highest Radiation Preference',
            xy=(temperatures[max_radiation_index], radiation_levels[max_radiation_index]),
            xytext=(temperatures[max_radiation_index] + 3, radiation_levels[max_radiation_index] + 15),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, color='red', fontweight='bold')

# Set plot title and axis labels
ax.set_title('Planetary Footprint: Discovering Alien Life Forms\'\nEnvironmental Preferences in Andromeda Galaxy', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Atmospheric Temperature (°C)', fontsize=12, labelpad=10)
ax.set_ylabel('Ambient Radiation Levels (Arbitrary Units)', fontsize=12, labelpad=10)

# Add gridlines
ax.grid(True, which='both', linestyle='--', linewidth=0.7, color='gray', alpha=0.7)

# Add a legend with a frame for clarity
ax.legend(title='Alien Species & Model', loc='upper left', fontsize=10, frameon=True, edgecolor='black')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()