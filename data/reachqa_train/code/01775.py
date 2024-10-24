import matplotlib.pyplot as plt
import numpy as np

# Original data
vitamin_intake = np.array([55, 75, 85, 95, 110, 130, 150, 165, 180, 200, 220, 240, 260, 280, 300])
energy_levels = np.array([3, 4, 4, 5, 6, 5, 7, 6, 8, 7, 8, 9, 8, 9, 10])

# Creating a new dataset for the second plot
# Group vitamin intake into ranges
bins = [50, 100, 150, 200, 250, 300]
bin_indices = np.digitize(vitamin_intake, bins)
average_energy_levels = [np.mean(energy_levels[bin_indices == i]) for i in range(1, len(bins))]

# Set up a 1x2 subplot layout
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Scatter plot
axes[0].scatter(vitamin_intake, energy_levels, color='orange', s=100, alpha=0.75, edgecolor='black', label='Participants')
axes[0].set_title("Impact of Vitamin Intake on Energy Levels:\nA Nutritional Study", fontsize=14, pad=20)
axes[0].set_xlabel("Daily Vitamin Intake (mg)", fontsize=12)
axes[0].set_ylabel("Energy Level (1 to 10)", fontsize=12)
axes[0].set_xlim(min(vitamin_intake) - 10, max(vitamin_intake) + 10)
axes[0].set_ylim(min(energy_levels) - 1, max(energy_levels) + 1)
axes[0].grid(True, linestyle='--', alpha=0.7)
axes[0].legend(loc='upper left', fontsize=10)
axes[0].annotate('Higher energy with increased intake', xy=(250, 9), xytext=(230, 9.5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, color='black')

# Second subplot: Bar chart
range_labels = ["50-100", "100-150", "150-200", "200-250", "250-300"]
axes[1].bar(range_labels, average_energy_levels, color='skyblue', edgecolor='black', alpha=0.8)
axes[1].set_title("Average Energy Levels by\nVitamin Intake Range", fontsize=14, pad=20)
axes[1].set_xlabel("Vitamin Intake Range (mg)", fontsize=12)
axes[1].set_ylabel("Average Energy Level", fontsize=12)
axes[1].set_ylim(min(average_energy_levels) - 1, max(average_energy_levels) + 1)
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()