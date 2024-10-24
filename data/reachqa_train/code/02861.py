import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of birds observed per session in different seasons
spring_observations = [15, 18, 20, 22, 25, 30, 28, 32, 35, 38]
summer_observations = [10, 12, 15, 18, 20, 22, 24, 25, 26, 28]
autumn_observations = [20, 22, 24, 26, 28, 30, 32, 35, 38, 40]
winter_observations = [5, 7, 9, 11, 13, 14, 15, 16, 18, 20]

# Combine data into a list for plotting
observations = [spring_observations, summer_observations, autumn_observations, winter_observations]

# Labels for each season
season_labels = ['Spring', 'Summer', 'Autumn', 'Winter']

# Plotting the vertical box chart
plt.figure(figsize=(10, 6))
bplot = plt.boxplot(observations, vert=True, patch_artist=True, labels=season_labels, notch=True,
                    boxprops=dict(facecolor='lightblue', color='darkblue'),
                    whiskerprops=dict(color='darkblue', linewidth=1.5),
                    capprops=dict(color='darkblue', linewidth=1.5),
                    medianprops=dict(color='darkorange', linewidth=2),
                    flierprops=dict(marker='o', markerfacecolor='red', markersize=6, linestyle='none', markeredgecolor='darkblue'))

# Customize background and grid
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.6)

# Adding the title and axis labels
plt.title('Seasonal Variation in Bird Observations\nin the Region of Aviania', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Seasons', fontsize=12, labelpad=10)
plt.ylabel('Number of Birds Observed per Session', fontsize=12, labelpad=10)

# Annotation for visual insight
plt.text(1, 42, 'Spring\nMost Active', fontsize=10, color='forestgreen', ha='center')
plt.text(2, 30, 'Summer\nDecline', fontsize=10, color='darkred', ha='center')
plt.text(3, 44, 'Autumn\nReturn', fontsize=10, color='goldenrod', ha='center')
plt.text(4, 22, 'Winter\nLeast Active', fontsize=10, color='navy', ha='center')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()