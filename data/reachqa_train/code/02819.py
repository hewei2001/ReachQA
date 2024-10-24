import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
species = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects']
percentages = [20, 30, 10, 5, 35]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Data for the radar chart
population_index = [500, 700, 300, 150, 1000]
categories = len(species)

# Radar plot setup
angles = np.linspace(0, 2 * np.pi, categories, endpoint=False).tolist()
population_index += population_index[:1]  # Repeat the first value to close the circle
angles += angles[:1]

# Create a figure with a polar plot and an additional space for the pie chart
fig, ax = plt.subplots(1, 1, figsize=(10, 8), subplot_kw=dict(polar=True))

# Radar plot
ax.fill(angles, population_index, color='#ff6666', alpha=0.25)
ax.plot(angles, population_index, color='#ff6666', linewidth=2, label='Population Index')

# Add the species names as labels for the radar plot
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(species, fontweight='bold')

# Create a second axes in the same figure for the pie chart
fig, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(
    percentages, 
    labels=species, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(edgecolor='black'), 
    explode=(0.1, 0, 0, 0, 0.1), 
    shadow=True
)

# Titles and adjustments
plt.suptitle("Biodiversity in Rainforest X", fontsize=18, fontweight='bold', y=0.98)
ax.set_title("Species Population Index\n(Radar Chart)", fontsize=14, pad=20)
ax2.set_title("Species Distribution\n(Pie Chart)", fontsize=14, pad=20)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show legend for the radar plot
ax.legend(loc='upper right', bbox_to_anchor=(0.3, 0.1))

# Display the plots
plt.show()