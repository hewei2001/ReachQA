import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = np.arange(1960, 2021, 10)
temperature_anomalies = np.array([-0.3, 0.0, 0.2, 0.4, 0.8, 1.2, 1.5])
error_margins = np.array([0.05, 0.07, 0.08, 0.10, 0.12, 0.15, 0.20])

# Create the figure and axis
plt.figure(figsize=(14, 8))

# Create a color gradient
norm = plt.Normalize(years.min(), years.max())
cmap = plt.get_cmap('coolwarm')
colors = cmap(norm(years))

# Create the line chart with error bars
for i in range(len(years) - 1):
    plt.plot(years[i:i+2], temperature_anomalies[i:i+2], color=colors[i], linewidth=2)

# Add error bars
plt.errorbar(years, temperature_anomalies, yerr=error_margins, fmt='o', color='darkblue',
             ecolor='lightblue', elinewidth=2, capsize=5, label='Temperature Anomalies')

# Adding trend line using polynomial fitting
z = np.polyfit(years, temperature_anomalies, 3)
p = np.poly1d(z)
plt.plot(years, p(years), "r--", label='Trend Line', linewidth=1.5)

# Enhance background
plt.gca().set_facecolor('#f0f0f5')

# Adding plot details
plt.title("Global Temperature Anomalies (1960-2020)\nUnderstanding Variability and Measurement Uncertainty",
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Temperature Anomaly (°C)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, fontsize=12)
plt.yticks(np.arange(-0.4, 1.8, 0.2), fontsize=12)
plt.axhline(0, color='gray', linewidth=1.0, linestyle='--')
plt.legend(loc='upper left', fontsize=12)

# Annotate the significant increase in the last two decades
plt.annotate('Significant Rise in Anomalies', xy=(2010, 1.5), xytext=(1980, 1.6),
             arrowprops=dict(facecolor='orange', shrink=0.05, width=2, headwidth=8),
             fontsize=12, color='darkred', weight='bold')

# Highlight the last decade
plt.axvspan(2000, 2020, color='orange', alpha=0.1, label='Highlight: 2000s', zorder=1)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()