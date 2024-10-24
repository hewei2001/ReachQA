import matplotlib.pyplot as plt
import numpy as np

# Define districts of GreenVille
districts = ["Central", "North", "East", "South", "West", "Uptown", "Downtown", "Lakeside", "Old Town", "Newbury"]

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# AQI data showing air quality improvement over the years
aqi_data = np.array([
    [85, 82, 80, 78, 75, 72, 70, 68, 65, 63, 60],  # Central
    [90, 87, 85, 84, 83, 80, 79, 76, 74, 71, 69],  # North
    [88, 86, 84, 83, 80, 77, 75, 73, 70, 68, 65],  # East
    [92, 89, 88, 86, 84, 82, 79, 78, 76, 74, 72],  # South
    [87, 85, 83, 82, 80, 78, 75, 73, 71, 68, 66],  # West
    [91, 88, 86, 84, 83, 81, 78, 76, 73, 70, 68],  # Uptown
    [93, 90, 88, 87, 85, 82, 80, 78, 76, 73, 70],  # Downtown
    [86, 84, 82, 81, 79, 77, 74, 72, 70, 68, 65],  # Lakeside
    [89, 87, 85, 83, 82, 79, 77, 75, 72, 70, 68],  # Old Town
    [85, 83, 80, 78, 76, 74, 72, 70, 68, 66, 64],  # Newbury
])

# Transpose data for correct orientation in heatmap
aqi_data_transposed = aqi_data.T

# Plotting the heatmap
plt.figure(figsize=(12, 8))
heatmap = plt.imshow(aqi_data_transposed, cmap='YlGn', aspect='auto', interpolation='nearest')

# Add labels and title
plt.title("Air Quality Improvement in GreenVille Districts\nA Decade of Green Initiatives", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Districts of GreenVille', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.xticks(ticks=np.arange(len(districts)), labels=districts, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(years)), labels=years)

# Add a color bar
cbar = plt.colorbar(heatmap, orientation='vertical')
cbar.set_label('Air Quality Index (AQI)', fontsize=12)
cbar.ax.invert_yaxis()  # Better AQI at the top

# Annotate each cell with AQI value
for i in range(len(years)):
    for j in range(len(districts)):
        plt.text(j, i, aqi_data_transposed[i, j], ha='center', va='center', color='black', fontsize=9)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()