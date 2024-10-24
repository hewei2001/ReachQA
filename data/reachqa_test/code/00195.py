import matplotlib.pyplot as plt
import numpy as np

# Decades
decades = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Original data for celestial events
solar_flares = np.array([30, 45, 50, 60, 55, 65, 70, 85, 90, 95, 100])
meteor_showers = np.array([10, 15, 20, 25, 20, 30, 35, 40, 50, 45, 55])
lunar_eclipses = np.array([5, 8, 10, 7, 9, 12, 10, 15, 18, 17, 20])
auroras = np.array([25, 30, 35, 40, 38, 42, 45, 50, 48, 55, 60])

# Additional data for another subplot (e.g., Sunspot activities)
sunspots = np.array([60, 75, 65, 85, 80, 90, 85, 110, 105, 120, 130])

# Create subplots: 1 row, 2 columns
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Plot original line chart
axs[0].plot(decades, solar_flares, marker='o', color='darkorange', linestyle='-', linewidth=2, label='Solar Flares')
axs[0].plot(decades, meteor_showers, marker='s', color='royalblue', linestyle='--', linewidth=2, label='Meteor Showers')
axs[0].plot(decades, lunar_eclipses, marker='^', color='green', linestyle='-.', linewidth=2, label='Lunar Eclipses')
axs[0].plot(decades, auroras, marker='d', color='violet', linestyle=':', linewidth=2, label='Auroras')

# Add title, labels, and legend to the first plot
axs[0].set_title("The Rhythm of the Cosmos:\nTracking Celestial Events Over a Century", fontsize=14, ha='center')
axs[0].set_xlabel("Decade", fontsize=12)
axs[0].set_ylabel("Event Frequency and Intensity", fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(title="Celestial Events", fontsize=9, title_fontsize=10, loc='upper left')
axs[0].set_xticks(decades)
axs[0].tick_params(axis='x', rotation=45)

# Highlight peak solar flares
peak_index = np.argmax(solar_flares)
axs[0].annotate('Peak Solar Flares', xy=(decades[peak_index], solar_flares[peak_index]),
                xytext=(decades[peak_index] + 5, solar_flares[peak_index] + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

# Plot additional bar chart subplot for sunspots
axs[1].bar(decades, sunspots, color='goldenrod', alpha=0.7, width=8, label='Sunspots')

# Add title, labels, and legend to the bar chart
axs[1].set_title("Decadal Sunspot Activity", fontsize=14)
axs[1].set_xlabel("Decade", fontsize=12)
axs[1].set_ylabel("Sunspot Count", fontsize=12)
axs[1].legend(fontsize=9, loc='upper left')
axs[1].set_xticks(decades)
axs[1].tick_params(axis='x', rotation=45)

# Layout adjustment to prevent overlap
plt.tight_layout()

# Show the combined plot
plt.show()