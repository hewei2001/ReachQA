import matplotlib.pyplot as plt
import numpy as np

# Define the sectors (axes) for the radar chart
labels = ['Solar Energy', 'Wind Energy', 'Hydro Energy', 'Geothermal Energy', 'Bioenergy']
num_vars = len(labels)

# Calculate the angle for each axis on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Renewable energy allocation data for each city
city_a = [30, 25, 15, 20, 10]  # In percentage
city_b = [25, 20, 25, 15, 15]  # In percentage
city_c = [20, 30, 20, 10, 20]  # In percentage

# Complete the loop to close the radar chart
city_a += city_a[:1]
city_b += city_b[:1]
city_c += city_c[:1]
angles += angles[:1]

# Create a radar chart figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw each sector and add labels to each axis
plt.xticks(angles[:-1], labels, color='grey', size=10)

# Define y-labels and limits for each axis
ax.set_ylim(0, 35)
ax.yaxis.set_tick_params(labelsize=8)

# Plot data for City A and fill the area
ax.plot(angles, city_a, linewidth=1.5, linestyle='solid', label='City A', color='#1f77b4')
ax.fill(angles, city_a, '#1f77b4', alpha=0.1)

# Plot data for City B and fill the area
ax.plot(angles, city_b, linewidth=1.5, linestyle='solid', label='City B', color='#ff7f0e')
ax.fill(angles, city_b, '#ff7f0e', alpha=0.1)

# Plot data for City C and fill the area
ax.plot(angles, city_c, linewidth=1.5, linestyle='solid', label='City C', color='#2ca02c')
ax.fill(angles, city_c, '#2ca02c', alpha=0.1)

# Add a descriptive title, broken into two lines for better readability
ax.set_title("Renewable Energy Resource Allocation\nfor Urban Sustainability in 2030",
             size=15, color='darkgreen', y=1.1)

# Customize the grid for clarity
ax.grid(color='grey', linestyle='--', linewidth=0.5)

# Add a legend with customized location and appearance
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()