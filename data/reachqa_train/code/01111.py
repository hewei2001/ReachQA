import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2019
years = np.arange(2010, 2020)

# Number of visitors in millions (fictional data)
paris_visitors = [15, 16, 18, 19, 20, 22, 23, 25, 24, 26]
tokyo_visitors = [12, 14, 15, 17, 19, 20, 21, 22, 23, 24]
new_york_visitors = [20, 21, 23, 22, 24, 25, 27, 26, 28, 30]
sydney_visitors = [10, 11, 13, 14, 15, 16, 17, 18, 19, 20]

# Create the plot
plt.figure(figsize=(14, 8))

# Plot data for each city with different styles
plt.plot(years, paris_visitors, marker='o', linestyle='-', color='blue', linewidth=2, label='Paris')
plt.plot(years, tokyo_visitors, marker='s', linestyle='--', color='red', linewidth=2, label='Tokyo')
plt.plot(years, new_york_visitors, marker='^', linestyle='-.', color='green', linewidth=2, label='New York')
plt.plot(years, sydney_visitors, marker='d', linestyle=':', color='purple', linewidth=2, label='Sydney')

# Add titles and labels
plt.title('The Evolution of Popular Travel Destinations\nOver a Decade', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Visitors (millions)', fontsize=14)

# Add a grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend
plt.legend(title='Destinations', loc='upper left', fontsize=12)

# Set x and y limits
plt.xlim(2010, 2019)
plt.ylim(10, 32)

# Add annotations to highlight interesting points
plt.annotate('Tokyo gains popularity', xy=(2014, 17), xytext=(2015, 19),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='red')

plt.annotate('New York surge', xy=(2018, 28), xytext=(2016, 29),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='green')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()