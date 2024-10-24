import matplotlib.pyplot as plt
import numpy as np

# Define habitats and insect types
habitats = ['Forests', 'Grasslands', 'Wetlands', 'Deserts', 'Urban Areas']
insect_types = ['Beetles', 'Butterflies', 'Bees', 'Ants', 'Dragonflies']

# Number of insects (in thousands) in each habitat
population_data = np.array([
    [150, 50, 40, 10, 20],  # Forests
    [70, 60, 25, 5, 10],    # Grasslands
    [90, 70, 80, 15, 30],   # Wetlands
    [15, 7, 3, 35, 5],      # Deserts
    [50, 30, 60, 30, 20]    # Urban Areas
])

# Calculate total populations for each habitat
total_populations = np.sum(population_data, axis=1)

# Calculate the average number of Dragonflies across habitats
dragonfly_data = population_data[:, -1]  # Last column: Dragonflies
average_dragonflies = np.mean(population_data, axis=1)

# Create plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Colors for bar chart
colors = ['#8c564b', '#e377c2', '#2ca02c', '#1f77b4', '#ff7f0e']

# Create horizontal bar chart
bars = ax1.barh(habitats, total_populations, color=colors, edgecolor='black', height=0.6, label='Total Population')

# Add data labels to each bar
for bar in bars:
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}k', va='center', fontsize=10, fontweight='bold', color='black')

# Customize x-axis
ax1.set_xlabel("Insect Population (Thousands)", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 350)

# Create a secondary y-axis for the overlay line plot
ax2 = ax1.twiny()

# Add a line plot for the average Dragonflies
ax2.plot(average_dragonflies, habitats, color='darkred', marker='o', linestyle='-', linewidth=2, markersize=8, label='Average Dragonflies')
ax2.set_xlim(0, 100)

# Add a legend
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.9))

# Set titles and labels
ax1.set_title("The Buzz of the Ecosystem:\nInsect Population and Average Dragonflies Across Habitats",
              fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()