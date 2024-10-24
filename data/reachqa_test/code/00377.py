import numpy as np
import matplotlib.pyplot as plt

# Define the data for average temperature and humidity
cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Rio de Janeiro', 'Mumbai', 'Cairo', 'Beijing', 'Moscow', 'Los Angeles']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = np.array([
    [-1, 1, 6, 12, 18, 24, 28, 27, 23, 16, 10, 3],  # New York
    [4, 5, 8, 11, 15, 18, 21, 21, 18, 14, 9, 5],    # London
    [5, 7, 10, 15, 20, 24, 28, 30, 26, 20, 14, 8],  # Tokyo
    [23, 24, 22, 19, 16, 14, 13, 14, 17, 19, 21, 23],  # Sydney
    [26, 27, 25, 23, 22, 21, 22, 24, 25, 25, 26, 27],  # Rio de Janeiro
    [24, 25, 28, 31, 33, 33, 32, 31, 29, 28, 27, 25],  # Mumbai
    [13, 15, 20, 25, 30, 34, 36, 35, 32, 27, 20, 15],  # Cairo
    [-4, 2, 10, 17, 22, 26, 29, 28, 23, 16, 8, -1],   # Beijing
    [-10, -8, -2, 6, 14, 19, 22, 20, 14, 6, -2, -8],  # Moscow
    [14, 15, 16, 18, 20, 22, 24, 24, 23, 20, 17, 15]   # Los Angeles
])

humidity = np.array([
    [60, 57, 54, 60, 65, 70, 75, 78, 75, 70, 65, 60],  # New York
    [85, 80, 75, 70, 65, 60, 60, 65, 70, 75, 80, 85],  # London
    [50, 48, 46, 50, 55, 60, 70, 75, 70, 65, 60, 55],  # Tokyo
    [65, 70, 75, 80, 75, 70, 65, 60, 65, 70, 75, 70],  # Sydney
    [80, 80, 78, 76, 75, 74, 76, 78, 80, 82, 80, 80],  # Rio de Janeiro
    [75, 74, 72, 70, 69, 68, 72, 75, 78, 78, 77, 75],  # Mumbai
    [55, 50, 45, 40, 35, 30, 28, 30, 35, 40, 45, 50],  # Cairo
    [40, 42, 45, 50, 55, 60, 65, 70, 60, 55, 50, 45],  # Beijing
    [80, 75, 70, 65, 60, 55, 55, 60, 65, 70, 75, 80],  # Moscow
    [65, 62, 60, 62, 65, 70, 73, 75, 73, 70, 67, 65]   # Los Angeles
])

# Create a figure and axis
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Plot the temperature heat map with 'coolwarm' colormap
temp_im = axs[0].imshow(temperature, cmap='coolwarm', interpolation='nearest', aspect='auto')
axs[0].set_title("Avg Temperature (°C)", fontsize=14)
axs[0].set_xlabel('Month', fontsize=12)
axs[0].set_ylabel('City', fontsize=12)
axs[0].set_xticks(np.arange(len(months)))
axs[0].set_yticks(np.arange(len(cities)))
axs[0].set_xticklabels(months, rotation=45, ha='right', fontsize=10)
axs[0].set_yticklabels(cities, fontsize=10)

# Plot the humidity heat map with 'YlGnBu' colormap
hum_im = axs[1].imshow(humidity, cmap='YlGnBu', interpolation='nearest', aspect='auto')
axs[1].set_title("Avg Humidity (%)", fontsize=14)
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('City', fontsize=12)
axs[1].set_xticks(np.arange(len(months)))
axs[1].set_yticks(np.arange(len(cities)))
axs[1].set_xticklabels(months, rotation=45, ha='right', fontsize=10)
axs[1].set_yticklabels(cities, fontsize=10)

# Add colorbars for each heatmap
temp_cbar = fig.colorbar(temp_im, ax=axs[0], orientation='vertical', fraction=0.046, pad=0.04)
temp_cbar.set_label('Temperature (°C)', fontsize=12)

hum_cbar = fig.colorbar(hum_im, ax=axs[1], orientation='vertical', fraction=0.046, pad=0.04)
hum_cbar.set_label('Humidity (%)', fontsize=12)

# Automatically adjust the layout
plt.tight_layout()

plt.show()
