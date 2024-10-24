import matplotlib.pyplot as plt
import numpy as np

# Data: Spice levels (in Scoville Heat Units, SHU) for different world regions over the decades
asia = [2000, 2200, 2500, 2800, 3100, 3300, 3700, 4000, 4500, 4800]
europe = [100, 150, 200, 300, 400, 550, 700, 900, 1200, 1500]
north_america = [300, 350, 450, 600, 750, 850, 1000, 1200, 1500, 1800]
south_america = [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2300, 2500, 2600]
africa = [800, 850, 900, 950, 1000, 1100, 1150, 1200, 1250, 1300]

# Combine data into a list for the box plot
data = [asia, europe, north_america, south_america, africa]

# Calculate average spice levels per region for overlay line plot
average_spice_levels = [np.mean(region) for region in data]

# Define labels for each region
region_labels = ['Asia', 'Europe', 'North America', 'South America', 'Africa']

# Plotting
fig, ax = plt.subplots(figsize=(14, 9))

# Creating the horizontal box plot
boxplot = ax.boxplot(data, vert=False, patch_artist=True, notch=True, widths=0.6)

# Customize the box plot colors
colors = ['lightcoral', 'lightblue', 'lightgreen', 'lightyellow', 'lightpink']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Overlay line plot
ax.plot(average_spice_levels, range(1, len(region_labels) + 1), marker='o', linestyle='-', color='purple', linewidth=2, label='Average Spice Level')

# Customize the plot
ax.set_title('Culinary Evolution: Changing Spice Levels\nin Global Cuisine (1970-2020)', fontsize=16, pad=20)
ax.set_xlabel('Spice Intensity (Scoville Heat Units)', fontsize=12)
ax.set_ylabel('Regions', fontsize=12)

# Customize y-axis with region labels
ax.set_yticklabels(region_labels, fontsize=10, ha='right')

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Highlight median values for clarity
for median in boxplot['medians']:
    median.set(color='darkred', linewidth=1.5)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Annotate the line plot with average values
for i, avg in enumerate(average_spice_levels):
    ax.annotate(f'{int(avg)} SHU', (avg, i + 1), textcoords="offset points", xytext=(5,-5), ha='left', fontsize=8)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()