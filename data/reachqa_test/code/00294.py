import matplotlib.pyplot as plt
import numpy as np

# Constructing artificial PM2.5 data for each season
spring_pm25 = [12, 15, 14, 17, 13, 16, 18, 15, 16, 17]
summer_pm25 = [20, 19, 23, 22, 21, 24, 25, 21, 22, 23]
autumn_pm25 = [35, 36, 38, 37, 39, 40, 41, 39, 37, 38]
winter_pm25 = [50, 53, 52, 55, 54, 56, 58, 55, 56, 57]

# Data for histogram or line plot (e.g., average PM2.5 levels per week over seasons)
avg_pm25 = [
    np.mean(spring_pm25),
    np.mean(summer_pm25),
    np.mean(autumn_pm25),
    np.mean(winter_pm25)
]

weeks = np.arange(1, 11)

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Boxplot
boxprops = dict(linestyle='-', linewidth=1, color='darkblue')
whiskerprops = dict(color='darkred', linestyle='--')
capprops = dict(color='black')
medianprops = dict(linestyle='-', linewidth=2, color='orange')

axes[0].boxplot([spring_pm25, summer_pm25, autumn_pm25, winter_pm25], labels=['Spring', 'Summer', 'Autumn', 'Winter'],
                patch_artist=True, notch=True, boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops, medianprops=medianprops)

colors = ['#87CEEB', '#FFD700', '#FF7F50', '#4682B4']
for patch, color in zip(axes[0].artists, colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

axes[0].set_title('Seasonal Variation of PM2.5 Levels\nin Greenfield', fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Season', fontsize=12)
axes[0].set_ylabel('PM2.5 Levels (µg/m³)', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.5)

# Line Plot
axes[1].plot(weeks, spring_pm25, label='Spring', color='#87CEEB', marker='o')
axes[1].plot(weeks, summer_pm25, label='Summer', color='#FFD700', marker='o')
axes[1].plot(weeks, autumn_pm25, label='Autumn', color='#FF7F50', marker='o')
axes[1].plot(weeks, winter_pm25, label='Winter', color='#4682B4', marker='o')

axes[1].set_title('Weekly PM2.5 Level Trends by Season', fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel('Week', fontsize=12)
axes[1].set_ylabel('PM2.5 Levels (µg/m³)', fontsize=12)
axes[1].legend(title='Season', loc='upper left', fontsize=10, title_fontsize='11')
axes[1].grid(True, linestyle='--', alpha=0.5)

# Improve layout to prevent text overlap
plt.tight_layout()

# Show plot
plt.show()