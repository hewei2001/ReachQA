import matplotlib.pyplot as plt

# AQI data for five cities over three years
aqi_city_a = [55, 60, 65, 70, 66, 72, 68, 74, 67, 58, 59, 61, 63, 60, 64, 62, 70, 75, 73, 72, 68, 66, 67, 69, 70, 72]
aqi_city_b = [75, 78, 80, 85, 82, 83, 81, 86, 88, 79, 76, 81, 84, 85, 82, 79, 77, 80, 82, 83, 78, 81, 84, 85, 82, 79]
aqi_city_c = [45, 48, 52, 49, 50, 46, 51, 53, 47, 44, 43, 45, 46, 48, 49, 47, 50, 52, 53, 48, 45, 44, 46, 48, 50, 51]
aqi_city_d = [68, 71, 73, 75, 72, 70, 69, 74, 76, 72, 70, 69, 67, 71, 73, 74, 70, 68, 69, 72, 74, 75, 73, 72, 70, 71]
aqi_city_e = [60, 63, 65, 67, 66, 62, 64, 68, 70, 65, 63, 61, 62, 64, 66, 68, 67, 65, 63, 64, 66, 69, 70, 72, 68, 66]

# Aggregated AQI data in a list
aqi_data = [aqi_city_a, aqi_city_b, aqi_city_c, aqi_city_d, aqi_city_e]

# Labels for the cities
city_labels = ['City A', 'City B', 'City C', 'City D', 'City E']

# Create the horizontal box plot
plt.figure(figsize=(10, 6))
boxprops = dict(facecolor='lightgreen', edgecolor='green')
whiskerprops = dict(color='green')
capprops = dict(color='green')
flierprops = dict(marker='o', color='red', alpha=0.5)
medianprops = dict(color='orange')

plt.boxplot(aqi_data, vert=False, patch_artist=True, notch=True,
            boxprops=boxprops,
            whiskerprops=whiskerprops,
            capprops=capprops,
            flierprops=flierprops,
            medianprops=medianprops,
            widths=0.6)

# Title and labels
plt.title('Air Quality Index (AQI) Distribution in Major Cities (2020-2022)\nAssessing Urban Pollution Control Efforts', fontsize=14, fontweight='bold')
plt.xlabel('Air Quality Index (AQI)', fontsize=12)
plt.yticks(range(1, len(city_labels) + 1), city_labels, fontsize=11)

# Add gridlines
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()