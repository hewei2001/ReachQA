import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2000, 2024)

# Efficiency improvements over the years for each technology (as percentages)
solar_efficiency = [10, 11, 13, 15, 17, 19, 21, 23, 24, 26, 28, 29, 32, 34, 36, 37, 38, 40, 41, 44, 46, 47, 49, 52]
wind_efficiency = [25, 26, 27, 28, 29, 30, 31, 33, 35, 36, 37, 39, 40, 42, 43, 45, 46, 47, 48, 50, 51, 53, 54, 56]
hydro_efficiency = [60, 61, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 71, 72, 73, 73, 74, 75, 76, 77, 78, 79, 80]
geothermal_efficiency = [45, 45, 46, 47, 48, 49, 50, 51, 51, 52, 53, 54, 55, 56, 57, 57, 58, 59, 60, 61, 62, 63, 63, 64]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each technology line with annotations
ax.plot(years, solar_efficiency, marker='o', linestyle='-', linewidth=2, label='Solar Cells', color='#FF7F50')
ax.annotate('Major Breakthrough', xy=(2013, 32), xytext=(2009, 36),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

ax.plot(years, wind_efficiency, marker='s', linestyle='--', linewidth=2, label='Wind Turbines', color='#1E90FF')
ax.annotate('New Designs', xy=(2017, 45), xytext=(2012, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

ax.plot(years, hydro_efficiency, marker='^', linestyle='-.', linewidth=2, label='Hydroelectric', color='#3CB371')
ax.annotate('Advanced Dams', xy=(2019, 75), xytext=(2014, 78),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

ax.plot(years, geothermal_efficiency, marker='D', linestyle=':', linewidth=2, label='Geothermal', color='#FFD700')
ax.annotate('Policy Impact', xy=(2015, 57), xytext=(2010, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

# Title and labels
ax.set_title("Advancements in Renewable Energy Technologies:\nA Two-Decade Journey in Efficiency Improvements", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Efficiency (%)", fontsize=14)

# Grid
ax.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(title='Renewable Technologies', fontsize=10, loc='lower right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()