import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Population data for each species in thousands
jellyfish = np.array([5, 6, 7, 8, 9, 11, 13, 16, 18, 21, 25, 29, 34, 40, 47, 55, 64, 74, 85, 97, 110])
turtles = np.array([50, 48, 47, 46, 45, 44, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 33, 34, 35, 36, 37])
sharks = np.array([20, 21, 22, 23, 24, 25, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 16, 17, 18, 19, 20])
whales = np.array([5, 5, 5, 6, 7, 8, 10, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114, 129])
dolphins = np.array([15, 16, 18, 20, 22, 25, 29, 34, 40, 47, 55, 64, 74, 85, 97, 110, 124, 139, 155, 172, 190])

# Set up figure and axes
fig, ax = plt.subplots(figsize=(16, 10))

# Create stackplot
ax.stackplot(years, jellyfish, turtles, sharks, whales, dolphins, 
             labels=['Jellyfish', 'Turtles', 'Sharks', 'Whales', 'Dolphins'],
             colors=['#FFDDC1', '#FFABAB', '#FFC3A0', '#D5AAFF', '#85E3FF'],
             alpha=0.8)

# Title and labels
ax.set_title('Exploring Ocean Biodiversity Over Time:\nMarine Species Populations (2000-2020)', fontsize=18, weight='bold')
ax.set_xlabel('Year', fontsize=14, weight='bold')
ax.set_ylabel('Population (Thousands)', fontsize=14, weight='bold')

# Format y-axis labels to show thousands
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}k'))

# Enhancing Legend
ax.legend(loc='upper left', title='Marine Species', fontsize=12, title_fontsize='13')

# Annotations for significant years
for index, year in enumerate(years):
    if year in [2000, 2010, 2020]:
        ax.annotate(f'{year}\n{whales[index]}k whales',
                    xy=(year, whales[index] + dolphins[index] + sharks[index] + turtles[index] + jellyfish[index]/2), 
                    xytext=(10, -30), textcoords='offset points',
                    arrowprops=dict(arrowstyle='->', color='gray'),
                    fontsize=10, color='black', weight='bold')

# Add a trendline (average increase for dolphins)
z = np.polyfit(years, dolphins, 1)
p = np.poly1d(z)
ax.plot(years, p(years), linestyle='--', color='green', linewidth=1.5, label='Dolphins Trend Line')
ax.legend(loc='upper left', title='Marine Species & Trends', fontsize=12, title_fontsize='13')

# X-axis customization
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adding grid and background
ax.grid(True, linestyle='--', alpha=0.5)
fig.patch.set_facecolor('#F0F0F5')  # Subtle background color

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()