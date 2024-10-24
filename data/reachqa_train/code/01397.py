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

# Create the figure and axis objects
plt.figure(figsize=(14, 8))

# Create the box plot with distinct color schemes and additional visual enhancements
box = plt.boxplot(data, patch_artist=True, notch=True, 
                  boxprops=dict(facecolor='lavender', color='blue', alpha=0.6),
                  medianprops=dict(color='red', linewidth=2),
                  whiskerprops=dict(color='blue'),
                  capprops=dict(color='blue'),
                  flierprops=dict(markerfacecolor='navy', marker='D', markersize=6, linestyle='none', markeredgecolor='navy'))

# Add colors to differentiate between cities
colors = ['lightcoral', 'lightseagreen', 'lightskyblue', 'palegoldenrod', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels with improved formatting
plt.title("Urban Air Quality Monitoring\nPM2.5 Levels Across Major Cities", fontsize=16, fontweight='bold', ha='center', pad=20)
plt.xlabel("City", fontsize=12, fontweight='bold')
plt.ylabel("PM2.5 Concentration (µg/m³)", fontsize=12, fontweight='bold')

# Set x-ticks as city names and improve readability
plt.xticks(ticks=np.arange(1, len(city_labels) + 1), labels=city_labels, rotation=15, fontsize=10)

# Add a grid for better readability with light gray lines
plt.grid(True, linestyle='--', linewidth=0.5, axis='y', color='lightgray', alpha=0.7)

# Highlight significant threshold lines with labels
plt.axhline(y=35, color='green', linestyle='--', linewidth=1, label='WHO Guideline (Safe Level)')
plt.axhline(y=70, color='orange', linestyle='--', linewidth=1, label='Unhealthy Level')

# Additional annotation for key data points
mean_values = [np.mean(city) for city in data]
for i, mean in enumerate(mean_values, start=1):
    plt.text(i, mean + 1, f'{mean:.1f}', fontsize=9, ha='center', color='black', fontweight='bold')

# Add legend for the threshold lines
plt.legend(loc='upper right', fontsize=10)

# Add shaded regions for PM2.5 categories
plt.axhspan(0, 35, facecolor='lightgreen', alpha=0.3, label='Safe')
plt.axhspan(35, 70, facecolor='khaki', alpha=0.3, label='Moderate')
plt.axhspan(70, max(max(data)) + 5, facecolor='salmon', alpha=0.3, label='Unhealthy')

# Adjust layout for neatness
plt.tight_layout()

# Display the plot
plt.show()