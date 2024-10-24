import matplotlib.pyplot as plt
import numpy as np

# Data representing PM2.5 levels (micrograms per cubic meter) for five cities
metropolisville_pm25 = [56, 60, 62, 55, 65, 70, 58, 63, 61, 68]
greenburg_pm25 = [30, 29, 34, 28, 33, 32, 31, 35, 36, 29]
smogton_pm25 = [80, 85, 88, 83, 87, 90, 86, 89, 91, 84]
clearview_pm25 = [22, 20, 25, 23, 21, 24, 26, 22, 27, 23]
industriapolis_pm25 = [72, 78, 75, 80, 76, 77, 74, 79, 81, 73]

# Combine data into a list for plotting
data = [metropolisville_pm25, greenburg_pm25, smogton_pm25, clearview_pm25, industriapolis_pm25]

# City labels for the x-axis
city_labels = ["Metropolisville", "Greenburg", "Smogton", "Clearview", "Industriapolis"]

# Create the box plot
plt.figure(figsize=(12, 7))
plt.boxplot(data, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            flierprops=dict(markerfacecolor='blue', marker='o', markersize=5, linestyle='none', markeredgecolor='blue'))

# Set titles and labels
plt.title("Urban Air Quality Monitoring\nPM2.5 Levels Across Major Cities", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("City", fontsize=12)
plt.ylabel("PM2.5 Concentration (µg/m³)", fontsize=12)

# Set x-ticks as city names
plt.xticks(ticks=np.arange(1, len(city_labels) + 1), labels=city_labels, rotation=15, fontsize=10)

# Add a grid for better readability
plt.grid(True, linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Highlight significant threshold lines
plt.axhline(y=35, color='green', linestyle='--', linewidth=1, label='WHO Guideline (Safe Level)')
plt.axhline(y=70, color='orange', linestyle='--', linewidth=1, label='Unhealthy Level')

# Add legend for the thresholds
plt.legend(loc='upper right', fontsize=10)

# Adjust layout for neatness and avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()