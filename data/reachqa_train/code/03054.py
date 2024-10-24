import numpy as np
import matplotlib.pyplot as plt

# Seasons for the x-axis
seasons = ["Spring", "Summer", "Autumn", "Winter"]

# Data representing water consumption in millions of liters for each district
downtown = [150, 200, 180, 160]
suburbia = [100, 130, 110, 90]
industrial = [180, 220, 200, 170]
uptown = [130, 160, 140, 120]

# Aggregate the data for easy plotting
data = np.array([downtown, suburbia, industrial, uptown])

# Additional related data for yearly averages
districts = ["Downtown", "Suburbia", "Industrial", "Uptown"]
yearly_averages = [np.mean(downtown), np.mean(suburbia), np.mean(industrial), np.mean(uptown)]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Stack plot for seasonal consumption
axs[0].stackplot(seasons, data, labels=districts, colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.8)
axs[0].set_title("AquaMetropolis: Seasonal Water Consumption\nAcross Urban Districts", fontsize=14, weight='bold')
axs[0].set_xlabel("Season", fontsize=12)
axs[0].set_ylabel("Water Consumption (Millions of Liters)", fontsize=12)
axs[0].legend(loc='upper left', title="Urban District", fontsize=10, title_fontsize=12)
axs[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axs[0].annotate('Peak in Summer', xy=('Summer', 600), xytext=('Autumn', 650), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
axs[0].annotate('Low in Winter', xy=('Winter', 350), xytext=('Spring', 450), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Second subplot: Bar plot for yearly averages
axs[1].bar(districts, yearly_averages, color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
axs[1].set_title("Average Yearly Water Consumption\nPer Urban District", fontsize=14, weight='bold')
axs[1].set_xlabel("Urban District", fontsize=12)
axs[1].set_ylabel("Average Water Consumption (Millions of Liters)", fontsize=12)
axs[1].set_ylim(0, 200)
axs[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout for both subplots
plt.tight_layout()

# Display the plots
plt.show()