import matplotlib.pyplot as plt
import numpy as np

# Define decades and fictional regions
decades = ['1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
regions = ['Aridlandia', 'Temperaville', 'Wetville', 'Polarville', 'Islandia']

# Freshwater availability data (in cubic kilometers)
freshwater_data = np.array([
    [200, 450, 800, 300, 120],  # 1970s
    [180, 440, 790, 280, 130],  # 1980s
    [160, 420, 780, 260, 140],  # 1990s
    [150, 410, 760, 250, 150],  # 2000s
    [140, 400, 750, 240, 160],  # 2010s
    [130, 390, 740, 230, 170]   # 2020s
])

# Plot settings: colors and markers for differentiation
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']
markers = ['o', 's', 'D', '^', 'p']

# Create a figure and axes for plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each region's data
for i, (region, color, marker) in enumerate(zip(regions, colors, markers)):
    ax.plot(decades, freshwater_data[:, i], marker=marker, color=color, label=region, linewidth=2)

    # Annotate each data point with its value
    for j, decade in enumerate(decades):
        ax.annotate(f'{freshwater_data[j, i]}', 
                    (decade, freshwater_data[j, i]), 
                    textcoords="offset points", 
                    xytext=(0, 10), 
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor=color, facecolor='white', alpha=0.6))

# Customize the plot appearance
ax.set_title('The Quest for Pure Water:\nFreshwater Availability Trends Over Decades', fontsize=14, weight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Freshwater Availability (Cubic Kilometers)', fontsize=12)
ax.set_ylim(0, 1000)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(title='Region', loc='upper right', fontsize=10, framealpha=1)

# Enhance the layout for better readability
plt.tight_layout()

# Display the plot
plt.show()