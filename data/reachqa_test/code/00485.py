import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
regions = ["North America", "Europe", "Asia", "South America", "Africa"]
solar_capacity = np.array([150, 180, 220, 60, 25])  # in Gigawatts
wind_capacity = np.array([120, 190, 200, 30, 15])   # in Gigawatts
hydro_capacity = np.array([80, 70, 110, 40, 25])    # in Gigawatts
biomass_capacity = np.array([20, 30, 15, 10, 5])    # in Gigawatts

# Set positions for the regions on the y-axis
y = np.arange(len(regions))

# Width of the bars
bar_width = 0.2

# Create the figure and axis
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Creating horizontal bars in the first subplot
axs[0].barh(y - 1.5 * bar_width, solar_capacity, bar_width, label='Solar', color='#ffcc00')
axs[0].barh(y - 0.5 * bar_width, wind_capacity, bar_width, label='Wind', color='#00ccff')
axs[0].barh(y + 0.5 * bar_width, hydro_capacity, bar_width, label='Hydropower', color='#009900')
axs[0].barh(y + 1.5 * bar_width, biomass_capacity, bar_width, label='Biomass', color='#8b4513')

# Setting labels and title for the first subplot
axs[0].set_title("Renewable Energy Capacity (in Gigawatts)\nby Region (2023)", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Capacity (Gigawatts)", fontsize=12)
axs[0].set_ylabel("Regions", fontsize=12)
axs[0].set_yticks(y)
axs[0].set_yticklabels(regions, fontsize=11)
axs[0].legend(title="Renewable Energy Sources", fontsize=10, title_fontsize='12')
axs[0].grid(axis='x', linestyle='--', alpha=0.7)

# Adding data labels to each bar in the first subplot
for idx in range(len(regions)):
    axs[0].text(solar_capacity[idx] + 5, idx - 1.5 * bar_width, str(solar_capacity[idx]), va='center', fontsize=9)
    axs[0].text(wind_capacity[idx] + 5, idx - 0.5 * bar_width, str(wind_capacity[idx]), va='center', fontsize=9)
    axs[0].text(hydro_capacity[idx] + 5, idx + 0.5 * bar_width, str(hydro_capacity[idx]), va='center', fontsize=9)
    axs[0].text(biomass_capacity[idx] + 5, idx + 1.5 * bar_width, str(biomass_capacity[idx]), va='center', fontsize=9)

# Creating a pie chart in the second subplot
total_capacity = solar_capacity + wind_capacity + hydro_capacity + biomass_capacity
axs[1].pie(total_capacity, labels=regions, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axs[1].set_title("Total Renewable Energy Capacity Distribution\nby Region (2023)", fontsize=16, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()