import matplotlib.pyplot as plt
import numpy as np

# Define more moons of Jupiter
moons = ['Io', 'Europa', 'Ganymede', 'Callisto', 'Amalthea', 'Himalia']

# Expanded Temperature data for each moon (in Kelvin)
io_temperatures = [np.sin(x / 5) * 50 + 130 for x in range(50)]
europa_temperatures = [np.sin(x / 6) * 20 + 100 for x in range(50)]
ganymede_temperatures = [np.cos(x / 6) * 15 + 95 for x in range(50)]
callisto_temperatures = [np.cos(x / 7) * 10 + 70 for x in range(50)]
amalthea_temperatures = [np.sin(x / 4) * 5 + 80 for x in range(50)]
himalia_temperatures = [np.cos(x / 5) * 8 + 85 for x in range(50)]

# Organize data into a list
temperature_data = [
    io_temperatures, europa_temperatures,
    ganymede_temperatures, callisto_temperatures,
    amalthea_temperatures, himalia_temperatures
]

# Define colors for each moon
colors = ['#FF6F61', '#6EC1E4', '#FFA500', '#8D99AE', '#B565A7', '#92A8D1']

# Plotting setup
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

# Create boxplot
box = axes[0].boxplot(temperature_data, vert=True, patch_artist=True, labels=moons, notch=True)

# Customize boxplot appearance
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize medians, whiskers, and caps
plt.setp(box['medians'], color='black', linewidth=1.5)
plt.setp(box['whiskers'], color='gray', linewidth=1.2)
plt.setp(box['caps'], color='gray', linewidth=1.2)

# Annotate with statistical insights
for i, temps in enumerate(temperature_data):
    mean_temp = np.mean(temps)
    axes[0].text(i + 1, mean_temp + 5, f'Mean: {mean_temp:.1f}K', ha='center', fontsize=9)

# Titles and labels
axes[0].set_title("Exploration of Jupiter's Moons: Temperature Variation Analysis", fontsize=14, weight='bold')
axes[0].set_ylabel('Temperature (K)', fontsize=12)
axes[0].set_xlabel('Moons of Jupiter', fontsize=12)

# Comparative line plot for mean temperature across moons
means = [np.mean(temps) for temps in temperature_data]
axes[1].plot(moons, means, marker='o', linestyle='-', color='teal')
axes[1].set_title('Mean Temperature Comparison Across Moons', fontsize=12, weight='bold')
axes[1].set_ylabel('Mean Temperature (K)', fontsize=12)
axes[1].set_xlabel('Moons of Jupiter', fontsize=12)

# Adding a legend to the line plot
axes[1].legend(['Mean Temperature'], loc='upper right')

# Layout optimization
plt.tight_layout()
plt.show()