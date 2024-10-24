import matplotlib.pyplot as plt
import numpy as np

# Data for the cities (increased to 20)
cities = [
    'New York', 'London', 'Tokyo', 'Berlin', 'Sydney',
    'Toronto', 'Paris', 'Los Angeles', 'Singapore', 'Barcelona',
    'Beijing', 'Moscow', 'Dubai', 'São Paulo', 'Mumbai',
    'Cairo', 'Rome', 'Mexico City', 'Bangkok', 'Seoul'
]
green_space = np.array([
    18, 24, 12, 30, 28, 15, 20, 22, 19, 17,
    14, 16, 25, 12, 10, 8, 11, 21, 27, 23
])
happiness_index = np.array([
    7, 8, 6, 9, 9, 7, 6, 5, 8, 7,
    6, 5, 7, 4, 3, 6, 5, 8, 7, 9
])
health_index = np.array([
    6, 7, 5, 8, 8, 6, 5, 4, 7, 6,
    5, 4, 7, 3, 2, 5, 4, 6, 8, 9
])
pollution_index = np.array([
    40, 30, 25, 35, 50, 45, 35, 55, 60, 25,
    70, 65, 80, 75, 85, 90, 60, 55, 45, 50
])  # Example pollution levels

# Create the main scatter plot
plt.figure(figsize=(14, 10))
scatter = plt.scatter(
    green_space, happiness_index, 
    s=health_index * 100, alpha=0.7, 
    edgecolors='w', linewidth=1, 
    c=pollution_index, cmap='plasma', marker='o'
)

# Annotate each city
for i, city in enumerate(cities):
    plt.annotate(city, (green_space[i] + 0.5, happiness_index[i]),
                 fontsize=8, ha='left', va='center', 
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# Set the title and labels
plt.title('Impact of Urban Green Spaces, Happiness, and Pollution\nin Major Cities Worldwide', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Green Space per Capita (sq meters)', fontsize=12)
plt.ylabel('Happiness Index (1-10 scale)', fontsize=12)
plt.xlim(0, 35)
plt.ylim(0, 10)

# Create a color bar based on the pollution index
cbar = plt.colorbar(scatter)
cbar.set_label('Pollution Index (Lower is better)', fontsize=12)
cbar.set_ticks(np.arange(20, 90, 10))
cbar.ax.tick_params(labelsize=10)

# Add gridlines for better readability
plt.grid(alpha=0.5)

# Add regression line (if desired)
m, b = np.polyfit(green_space, happiness_index, 1)
plt.plot(green_space, m * green_space + b, color='black', linestyle='--', label='Trend Line')
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()