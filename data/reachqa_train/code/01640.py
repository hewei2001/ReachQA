import matplotlib.pyplot as plt
import numpy as np

# Data: Art gallery visitors (in thousands) from 2010 to 2020
years = np.arange(2010, 2021)
gallery_visitors = {
    'New York': [950, 920, 970, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1400],
    'Paris': [750, 780, 760, 800, 850, 880, 910, 930, 950, 970, 1000],
    'Tokyo': [600, 620, 650, 670, 700, 730, 750, 770, 800, 830, 860],
    'London': [890, 870, 880, 920, 940, 960, 1000, 1020, 1040, 1060, 1100],
    'Berlin': [400, 420, 430, 450, 480, 500, 520, 540, 550, 570, 600]
}

# Setup the plot
plt.figure(figsize=(14, 8))

# Colors for each city line
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2']

# Plot data with annotations for each city
for (city, visitors), color in zip(gallery_visitors.items(), colors):
    plt.plot(years, visitors, '-o', label=city, color=color, linewidth=2, markersize=6, alpha=0.8)
    
    # Annotate for key data points for each city (first, midpoint, and last)
    midpoint_index = len(years) // 2
    key_points = [(years[0], visitors[0]), (years[midpoint_index], visitors[midpoint_index]), (years[-1], visitors[-1])]
    for (year, visitor) in key_points:
        plt.annotate(f'{visitor}k', xy=(year, visitor), xytext=(5, -15 if visitor < max(visitors) else 5), 
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color=color), 
                     fontsize=10, color=color, ha='center')

# Set titles and labels
plt.title('Art Gallery Visitors Trend (2010-2020)\nPublic Engagement in Major Cities', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Visitors (in thousands)', fontsize=12)

# Add legend
plt.legend(title='Cities', loc='upper left', fontsize=10)

# Add grid for clarity
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Ensure tight layout for readability
plt.tight_layout()

# Show the plot
plt.show()