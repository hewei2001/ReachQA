import matplotlib.pyplot as plt
import numpy as np

# Expanded categories for evaluation
categories = [
    'Atmosphere', 'Surface Water', 'Radiation\nLevels', 'Temperature', 
    'Energy\nPotential', 'Mineral\nComposition', 'Gravity', 
    'Magnetic\nField', 'Surface\nComposition', 'Atmospheric\nPressure'
]
num_vars = len(categories)

# Data representing each celestial body's suitability (scores out of 10)
# Scores are now more complex to reflect mathematical manipulation
mars = [7.5, 3.2, 6.8, 4.1, 8.3, 5.5, 3.8, 2.7, 6.1, 5.2]
europa = [2.4, 8.7, 3.1, 5.3, 6.4, 7.5, 6.2, 4.8, 5.9, 7.1]
titan = [5.9, 7.1, 5.5, 6.2, 7.4, 8.6, 4.9, 3.4, 5.8, 6.3]
venus = [1.2, 2.8, 9.7, 1.3, 5.7, 6.3, 5.2, 7.4, 3.8, 4.2]
moon = [3.7, 1.9, 7.3, 3.5, 4.6, 3.9, 5.7, 2.6, 4.4, 6.9]

# Adding a new celestial body for more complexity
exoplanet = [8.1, 5.7, 4.8, 7.2, 9.0, 6.5, 7.3, 5.6, 8.8, 7.5]

# Arrange data in a list
data = [mars, europa, titan, venus, moon, exoplanet]
labels = ['Mars', 'Europa', 'Titan', 'Venus', 'Moon', 'Exoplanet']

# Function to repeat the first point to close the radar chart
def repeat_first(data):
    return np.concatenate((data, [data[0]]))

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Set up the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each celestial body's suitability data
colors = ['b', 'g', 'r', 'c', 'm', 'y']
for i in range(len(data)):
    values = repeat_first(data[i])
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=labels[i], color=colors[i])
    ax.fill(angles, values, alpha=0.25, color=colors[i])

# Add labels for categories at correct angles
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, wrap=True)

# Set the title and legend, breaking the title into two lines
ax.set_title("Interplanetary Habitat Suitability Analysis:\nYear 2050", size=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Automatically adjust the plot to prevent overlap and improve layout
plt.tight_layout()

# Show the plot
plt.show()