import matplotlib.pyplot as plt
import numpy as np

# Define the decades from 1920 to 2020
decades = np.arange(1920, 2030, 10)

# Fictional expedition data for each exploration category
expeditions_ocean = np.array([5, 10, 15, 30, 50, 40, 45, 60, 55, 70, 80])
expeditions_mountain = np.array([20, 25, 35, 45, 60, 65, 75, 80, 85, 90, 95])
expeditions_polar = np.array([2, 5, 7, 10, 18, 25, 30, 35, 32, 38, 40])
expeditions_desert = np.array([10, 15, 20, 25, 30, 35, 40, 50, 48, 52, 58])

# Colors for each expedition category
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a']

# Create the figure and axis
plt.figure(figsize=(14, 8))

# Plot the stacked area chart
plt.stackplot(decades, expeditions_ocean, expeditions_mountain, expeditions_polar, expeditions_desert, 
              labels=['Ocean', 'Mountain', 'Polar', 'Desert'], colors=colors, alpha=0.8)

# Set the title and labels
plt.title('Century of Global Exploration:\nExpeditions from 1920 to 2020', fontsize=16, fontweight='bold')
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Number of Expeditions', fontsize=14)

# Add legend
plt.legend(loc='upper left', title='Expedition Categories', fontsize=12, bbox_to_anchor=(1, 1))

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate a notable point for emphasis (e.g., peak ocean exploration)
peak_decade = 2020
plt.annotate('Peak Ocean Exploration', 
             xy=(peak_decade, expeditions_ocean[-1] + expeditions_mountain[-1] + expeditions_polar[-1] + expeditions_desert[-1]),
             xytext=(peak_decade, expeditions_ocean[-1] + expeditions_mountain[-1] + expeditions_polar[-1] + expeditions_desert[-1] + 20),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), 
             fontsize=11, color='black')

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Allow space for the legend

# Display the plot
plt.show()