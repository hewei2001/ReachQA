import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Efficiency', 'Environmental Impact', 'Cost-Effectiveness', 'Accessibility', 'Technological Maturity']
num_vars = len(categories)

# Define the data for each energy source
solar = [7, 9, 6, 5, 8]
wind = [8, 9, 7, 6, 9]
hydro = [7, 8, 7, 4, 7]
nuclear = [8, 5, 7, 3, 9]
coal = [5, 2, 9, 7, 4]

# Combine the data for easy iteration
energy_sources = [solar, wind, hydro, nuclear, coal]
labels = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Coal']

# Create an angle for each category in the plot
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Repeat the first angle to close the plot
angles += angles[:1]

# Setup the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to plot each energy source
for idx, data in enumerate(energy_sources):
    data += data[:1]  # Close the circle
    ax.fill(angles, data, alpha=0.25, label=labels[idx])
    ax.plot(angles, data, linewidth=2)

# Customize the plot
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)
ax.set_title("Sustainability Index of Energy Sources\nAn In-Depth Radar Analysis", size=15, ha='center')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Ensure layout doesn't overlap
plt.tight_layout()

# Display the radar chart
plt.show()