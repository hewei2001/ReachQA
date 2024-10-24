import matplotlib.pyplot as plt
import numpy as np

# Define the plant species and their ecological services
species = ['Luminosus', 'Verdantia', 'Carbonsynth', 'Aquaflora', 'Cyclicus']
services = ['Oxygen Generation', 'CO2 Absorption', 'Nutrient Cycling', 'Water Retention']

# Ecological performance data for each plant species (percentages)
performance_data = [
    [80, 70, 65, 75],  # Luminosus
    [60, 85, 90, 80],  # Verdantia
    [90, 60, 75, 70],  # Carbonsynth
    [70, 75, 80, 85],  # Aquaflora
    [85, 65, 70, 90]   # Cyclicus
]

# Convert the data to a float array and normalize
performance_data = np.array(performance_data, dtype=float)
performance_data /= 100

# Calculate number of variables and angles for the radar chart
num_vars = len(services)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # To close the circle

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Draw one axis per variable and add labels
plt.xticks(angles[:-1], services, color='grey', size=12)

# Plot each species performance and fill the area
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']
for i, specie in enumerate(species):
    values = performance_data[i].tolist()
    values += values[:1]  # To close the loop
    ax.fill(angles, values, color=colors[i], alpha=0.3)
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=specie)

# Add title and legend
plt.title('Productivity Metrics of\nAlien Plant Species on Planet X', size=16, color='darkgreen', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Ensure the layout fits well
plt.tight_layout()

# Show the plot
plt.show()