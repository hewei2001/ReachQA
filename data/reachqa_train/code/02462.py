import matplotlib.pyplot as plt
import numpy as np

# Define habitats and insect types
habitats = ['Forests', 'Grasslands', 'Wetlands', 'Deserts', 'Urban Areas']
insect_types = ['Beetles', 'Butterflies', 'Bees', 'Ants', 'Dragonflies']

# Number of insects (in thousands) in each habitat
# Modified data for clarity and diversity
population_data = np.array([
    [150, 50, 40, 10, 20],  # Forests
    [70, 60, 25, 5, 10],    # Grasslands
    [90, 70, 80, 15, 30],   # Wetlands
    [15, 7, 3, 35, 5],      # Deserts
    [50, 30, 60, 30, 20]    # Urban Areas
])

# Calculate total populations for each habitat
total_populations = np.sum(population_data, axis=1)

# Create plot
fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#8c564b', '#e377c2', '#2ca02c', '#1f77b4', '#ff7f0e']

# Create horizontal bar chart
bars = ax.barh(habitats, total_populations, color=colors, edgecolor='black', height=0.6)

# Add data labels to each bar
for bar in bars:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
            f'{int(bar.get_width())}k', va='center', fontsize=10, fontweight='bold', color='black')

# Set titles and labels
ax.set_title("The Buzz of the Ecosystem:\nInsect Population Distribution Across Habitats",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Insect Population (Thousands)", fontsize=12)
ax.xaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(0, 350)  # Adjusted based on maximum data value

# Customize y-ticks to ensure the label positions align perfectly with bars
ax.set_yticks(np.arange(len(habitats)))
ax.set_yticklabels(habitats, fontsize=12)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()