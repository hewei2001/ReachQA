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
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#f0f0f5')  # Light background color

# Draw each sector and add labels to each axis with customized color
plt.xticks(angles[:-1], labels, color='#333333', size=11)

# Define y-labels and limits for each axis
ax.set_ylim(0, 35)
ax.yaxis.set_tick_params(labelsize=9)
ax.set_yticks([10, 20, 30])
ax.set_yticklabels(['10%', '20%', '30%'], color='#555555')

# Improved gridlines and radial background shading
ax.yaxis.grid(True, linestyle='--', color='#d9d9d9')
ax.spines['polar'].set_visible(False)

# Plot data for City A with markers and line style
ax.plot(angles, city_a, linewidth=2.0, linestyle='-', label='City A', color='#1f77b4', marker='o')
ax.fill(angles, city_a, '#1f77b4', alpha=0.1)

# Plot data for City B with different line style and markers
ax.plot(angles, city_b, linewidth=2.0, linestyle='--', label='City B', color='#ff7f0e', marker='x')
ax.fill(angles, city_b, '#ff7f0e', alpha=0.1)

# Plot data for City C with another distinct line style and markers
ax.plot(angles, city_c, linewidth=2.0, linestyle='-.', label='City C', color='#2ca02c', marker='s')
ax.fill(angles, city_c, '#2ca02c', alpha=0.1)

# Add a descriptive title, broken into two lines for better readability
ax.set_title("Renewable Energy Resource Allocation\nfor Urban Sustainability in 2030",
             size=16, color='darkgreen', y=1.1, ha='center')

# Add annotations for the data points
for i, city in enumerate([city_a, city_b, city_c]):
    for j, value in enumerate(city[:-1]):
        ax.text(angles[j], value + 1, f"{value}%", color='black', ha='center', size=9)

# Add a legend with customized location and appearance
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()