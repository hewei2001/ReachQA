import matplotlib.pyplot as plt
import numpy as np

# Define regions and spices
regions = ['North America', 'Europe', 'Asia', 'Africa']
spices = ['Turmeric', 'Cumin', 'Cinnamon', 'Black Pepper', 'Paprika']

# Define synthetic data for spice consumption (metric tons)
# Adjusted to ensure clear visualization
spice_consumption = np.array([
    [120, 80, 70, 90, 60],    # North America
    [100, 60, 80, 100, 50],   # Europe
    [200, 150, 180, 210, 130],# Asia
    [140, 130, 110, 150, 100] # Africa
])

# Create figure and axis for heatmap
plt.figure(figsize=(10, 8))
cmap = plt.get_cmap('YlOrBr')

# Plot the heatmap
plt.imshow(spice_consumption, cmap=cmap, aspect='auto')

# Add a color bar
cbar = plt.colorbar()
cbar.set_label('Avg. Yearly Consumption (Metric Tons)', fontsize=12)

# Set ticks and labels for axes
plt.xticks(ticks=np.arange(len(spices)), labels=spices, rotation=45, ha='right', fontsize=12)
plt.yticks(ticks=np.arange(len(regions)), labels=regions, fontsize=12)

# Add title and axis labels
plt.title("Global Spice Usage Patterns\nA Heatmap of Flavor", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Spice", fontsize=14)
plt.ylabel("Region", fontsize=14)

# Annotate each cell with the data value
for i in range(len(regions)):
    for j in range(len(spices)):
        plt.text(j, i, f'{spice_consumption[i, j]}', ha='center', va='center', color='black', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()