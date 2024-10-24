import matplotlib.pyplot as plt
import numpy as np

# Define data representing annual tea consumption per person (in kg) for each region
asia_consumption = [3.1, 2.9, 3.5, 3.2, 4.0, 2.8, 3.3, 3.7, 2.6, 3.8, 3.0, 4.1, 3.9, 3.0, 3.4]
europe_consumption = [1.2, 1.4, 1.0, 0.8, 1.5, 1.3, 1.6, 1.1, 0.9, 1.7, 1.4, 0.7, 1.3, 1.5, 1.1]
north_america_consumption = [0.5, 0.6, 0.4, 0.7, 0.5, 0.8, 0.6, 0.5, 0.3, 0.9, 0.7, 0.4, 0.6, 0.5, 0.7]
africa_consumption = [1.0, 1.3, 0.9, 0.8, 1.1, 1.2, 1.4, 1.0, 0.7, 1.3, 1.1, 0.8, 1.2, 1.0, 1.3]
oceania_consumption = [1.8, 1.9, 2.0, 1.7, 1.6, 2.1, 1.8, 2.2, 1.9, 2.0, 1.7, 1.8, 1.9, 1.6, 2.1]

# Group all consumption data into a list for plotting
all_consumption = [
    asia_consumption,
    europe_consumption,
    north_america_consumption,
    africa_consumption,
    oceania_consumption
]

# Region labels
region_labels = ["Asia", "Europe", "North America", "Africa", "Oceania"]

# Calculate average consumption over the years for the line plot
years = np.arange(2000, 2015)
average_consumption = np.array([asia_consumption, europe_consumption, north_america_consumption, 
                                africa_consumption, oceania_consumption]).mean(axis=0)

# Create the figure and axis
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Left subplot: Box Plot
box = axes[0].boxplot(all_consumption, labels=region_labels, patch_artist=True, notch=True, vert=True)
colors = ['#FFD700', '#ADFF2F', '#FF69B4', '#87CEEB', '#FFA07A']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axes[0].set_title("Global Tea Consumption Patterns:\nAnnual Per Capita Consumption by Region", fontsize=16, weight='bold')
axes[0].set_xlabel("Regions", fontsize=12)
axes[0].set_ylabel("Tea Consumption (kg/person)", fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Customize box plots further
for element in ['whiskers', 'caps', 'medians']:
    plt.setp(box[element], color='black')
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.5)

# Right subplot: Line Plot
axes[1].plot(years, average_consumption, marker='o', linestyle='-', color='b', label='Average Consumption')
for i, region in enumerate(region_labels):
    axes[1].plot(years, all_consumption[i], linestyle='--', label=f'{region} Trend', alpha=0.6)

axes[1].set_title("Trend in Average Tea Consumption\n(2000-2014)", fontsize=16, weight='bold')
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Tea Consumption (kg/person)", fontsize=12)
axes[1].legend(loc='upper left', frameon=False)
axes[1].grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()