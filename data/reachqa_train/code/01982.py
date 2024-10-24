import matplotlib.pyplot as plt
import numpy as np

# AQI data for five cities over two years (adjusted to 24 data points per city)
aqi_city_a = [55, 60, 65, 70, 66, 72, 68, 74, 67, 58, 59, 61, 63, 60, 64, 62, 70, 75, 73, 72, 68, 66, 67, 69]
aqi_city_b = [75, 78, 80, 85, 82, 83, 81, 86, 88, 79, 76, 81, 84, 85, 82, 79, 77, 80, 82, 83, 78, 81, 84, 85]
aqi_city_c = [45, 48, 52, 49, 50, 46, 51, 53, 47, 44, 43, 45, 46, 48, 49, 47, 50, 52, 53, 48, 45, 44, 46, 48]
aqi_city_d = [68, 71, 73, 75, 72, 70, 69, 74, 76, 72, 70, 69, 67, 71, 73, 74, 70, 68, 69, 72, 74, 75, 73, 72]
aqi_city_e = [60, 63, 65, 67, 66, 62, 64, 68, 70, 65, 63, 61, 62, 64, 66, 68, 67, 65, 63, 64, 66, 69, 70, 72]

# Aggregate AQI data
aqi_data = [aqi_city_a, aqi_city_b, aqi_city_c, aqi_city_d, aqi_city_e]
city_labels = ['City A', 'City B', 'City C', 'City D', 'City E']

# Calculate monthly average AQI
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_avg_aqi = np.mean(aqi_data, axis=0).reshape(-1, 2).mean(axis=1)

# Setup the figure and subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Box Plot - AQI Distribution
ax[0].boxplot(aqi_data, vert=False, patch_artist=True, notch=True,
              boxprops=dict(facecolor='lightgreen', edgecolor='green'),
              whiskerprops=dict(color='green'),
              capprops=dict(color='green'),
              flierprops=dict(marker='o', color='red', alpha=0.5),
              medianprops=dict(color='orange'),
              widths=0.6)
ax[0].set_title('AQI Distribution in Major Cities (2020-2021)', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Air Quality Index (AQI)', fontsize=12)
ax[0].set_yticks(range(1, len(city_labels) + 1))
ax[0].set_yticklabels(city_labels, fontsize=11)
ax[0].grid(axis='x', linestyle='--', alpha=0.7)

# Line Plot - Average AQI Trend Over Time
for i, city_data in enumerate(aqi_data):
    city_avg = np.array(city_data).reshape(-1, 2).mean(axis=1)
    ax[1].plot(months, city_avg, marker='o', label=city_labels[i])

ax[1].set_title('Average Monthly AQI Trend (2020-2021)', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Month', fontsize=12)
ax[1].set_ylabel('Average AQI', fontsize=12)
ax[1].legend(fontsize=10, loc='upper right')
ax[1].grid(linestyle='--', alpha=0.7)

# Adjust layout for clear visualization
plt.tight_layout()

# Show the plots
plt.show()