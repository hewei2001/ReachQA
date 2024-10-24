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
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']

# Create the figure and axis
plt.figure(figsize=(14, 8))

# Plot the stacked area chart with patterns
plt.stackplot(decades, expeditions_ocean, expeditions_mountain, expeditions_polar, expeditions_desert, 
              labels=['Ocean', 'Mountain', 'Polar', 'Desert'], colors=colors, alpha=0.8)

# Enhance data visibility with markers
plt.plot(decades, expeditions_ocean, 'o-', color='#1b9e77', label='_nolegend_')
plt.plot(decades, expeditions_mountain, 's-', color='#d95f02', label='_nolegend_')
plt.plot(decades, expeditions_polar, '^-', color='#7570b3', label='_nolegend_')
plt.plot(decades, expeditions_desert, 'D-', color='#e7298a', label='_nolegend_')

# Set the title and labels
plt.title('Century of Global Exploration:\nExpeditions from 1920 to 2020', fontsize=16, fontweight='bold')
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Number of Expeditions', fontsize=14)

# Add legend with a new layout
plt.legend(loc='upper left', title='Expedition Categories', fontsize=12, bbox_to_anchor=(1.02, 1))

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate a notable point for emphasis
peak_decade = 2020
total_expeditions = expeditions_ocean[-1] + expeditions_mountain[-1] + expeditions_polar[-1] + expeditions_desert[-1]
plt.annotate('Peak Ocean Exploration', 
             xy=(peak_decade, total_expeditions),
             xytext=(peak_decade - 20, total_expeditions + 40),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), 
             fontsize=11, color='black', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

# Adding vertical lines to mark significant years
significant_years = [1940, 1960, 1980, 2000]
for year in significant_years:
    plt.axvline(x=year, color='gray', linestyle='--', lw=0.8, alpha=0.7)
    plt.text(year, -10, f'{year}', rotation=90, verticalalignment='bottom', fontsize=10)

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Allow space for the legend

# Display the plot
plt.show()