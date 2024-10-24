import matplotlib.pyplot as plt
import numpy as np

# Define global regions and renewable energy types
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Africa']
energy_types = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']

# Installed capacity data for each region and energy type (in GW)
capacities = [
    [150, 120, 110, 60, 30],   # North America
    [180, 200, 95, 45, 25],    # Europe
    [250, 300, 150, 70, 40],   # Asia-Pacific
    [100, 80, 120, 35, 15],    # Latin America
    [60, 50, 90, 20, 10]       # Africa
]

# Convert the data into a NumPy array
capacities = np.array(capacities)

# Setup bar plot
x = np.arange(len(regions))  # X locations for the groups
width = 0.15  # Width of the bars

fig, ax = plt.subplots(figsize=(14, 8))

# Colors for the different energy types
colors = ['#FF5733', '#33A1FF', '#33FF57', '#FFD733', '#FF33A1']

# Plot each energy type as a separate set of bars
for i, energy_type in enumerate(energy_types):
    bar = ax.bar(x + i * width, capacities[:, i], width, label=energy_type, color=colors[i])
    for rect in bar:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=9)

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Installed Capacity (GW)', fontsize=12)
ax.set_title('The Rise of Renewable Energy:\nInstalled Capacity in Global Regions (2023)', fontsize=14, weight='bold')
ax.set_xticks(x + width * (len(energy_types) / 2 - 0.5))
ax.set_xticklabels(regions, fontsize=10)
ax.legend(title='Energy Type', fontsize=10)

# Add gridlines for the y-axis to improve readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Ensure the layout fits well
plt.tight_layout()

# Display the plot
plt.show()