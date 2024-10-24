import matplotlib.pyplot as plt
import numpy as np

# Data for the scatter plot
cities = ['New York', 'Berlin', 'Tokyo', 'Rio de Janeiro', 'Sydney', 'Cape Town']
performances = np.array([120, 85, 100, 90, 75, 65])
decibel_levels = np.array([75, 72, 80, 78, 70, 68])
cultural_index = np.array([8, 7, 9, 8, 6, 5])  # Used for marker size

# Create the scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(performances, decibel_levels, s=cultural_index * 100, alpha=0.7, 
                      c=decibel_levels, cmap='coolwarm', edgecolor='w')

# Annotate each city on the plot
for i, city in enumerate(cities):
    plt.annotate(city, (performances[i], decibel_levels[i]), fontsize=10, ha='right', va='bottom')

# Title and axis labels
plt.title("Harmonies and Decibels:\nThe Soundscape of Global Music Festivals", fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Number of Music Performances', fontsize=12)
plt.ylabel('Average Decibel Levels (dB)', fontsize=12)

# Add a color bar to represent decibel levels
cbar = plt.colorbar(scatter)
cbar.set_label('Decibel Level (dB)', fontsize=12)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust the layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()