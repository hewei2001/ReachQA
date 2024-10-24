import matplotlib.pyplot as plt
import numpy as np

# Data: Green space areas in square kilometers over the years
years = np.arange(2012, 2023)
nyc = [700, 710, 715, 720, 725, 730, 735, 740, 750, 760, 770]
london = [620, 625, 630, 635, 640, 645, 655, 660, 670, 680, 690]
tokyo = [500, 505, 510, 515, 520, 530, 535, 540, 545, 550, 560]
sydney = [400, 405, 410, 420, 425, 430, 435, 440, 445, 450, 455]
rio = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]

# Create cumulative data for stacking
nyc_cum = np.array(nyc)
london_cum = nyc_cum + np.array(london)
tokyo_cum = london_cum + np.array(tokyo)
sydney_cum = tokyo_cum + np.array(sydney)
rio_cum = sydney_cum + np.array(rio)

# Plotting the area chart
plt.figure(figsize=(14, 8))

plt.fill_between(years, rio_cum, color='#7fc97f', alpha=0.7, label='Rio de Janeiro')
plt.fill_between(years, sydney_cum, rio_cum, color='#beaed4', alpha=0.7, label='Sydney')
plt.fill_between(years, tokyo_cum, sydney_cum, color='#fdc086', alpha=0.7, label='Tokyo')
plt.fill_between(years, london_cum, tokyo_cum, color='#ffff99', alpha=0.7, label='London')
plt.fill_between(years, nyc_cum, london_cum, color='#386cb0', alpha=0.7, label='New York City')

# Adding labels and title
plt.title('Growth of Urban Green Spaces\nin Major Cities Over the Last Decade', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=14, weight='bold')
plt.ylabel('Green Space Area (sq km)', fontsize=14, weight='bold')

# Customizing the legend
plt.legend(loc='upper left', fontsize=12)

# Enhancing readability with grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust x-tick labels to avoid overlap
plt.xticks(years, rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()