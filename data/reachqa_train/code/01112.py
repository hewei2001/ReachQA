import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2019
years = np.arange(2010, 2020)

# Number of visitors in millions (fictional data)
paris_visitors = [15, 16, 18, 19, 20, 22, 23, 25, 24, 26]
tokyo_visitors = [12, 14, 15, 17, 19, 20, 21, 22, 23, 24]
new_york_visitors = [20, 21, 23, 22, 24, 25, 27, 26, 28, 30]
sydney_visitors = [10, 11, 13, 14, 15, 16, 17, 18, 19, 20]

# Calculate average annual growth rate for each city
def calculate_growth_rate(visitors):
    growth_rates = [(visitors[i + 1] - visitors[i]) / visitors[i] * 100 for i in range(len(visitors) - 1)]
    average_growth_rate = np.mean(growth_rates)
    return average_growth_rate

cities = ['Paris', 'Tokyo', 'New York', 'Sydney']
growth_rates = [
    calculate_growth_rate(paris_visitors),
    calculate_growth_rate(tokyo_visitors),
    calculate_growth_rate(new_york_visitors),
    calculate_growth_rate(sydney_visitors)
]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Line plot for the evolution of visitors
ax1.plot(years, paris_visitors, marker='o', linestyle='-', color='blue', linewidth=2, label='Paris')
ax1.plot(years, tokyo_visitors, marker='s', linestyle='--', color='red', linewidth=2, label='Tokyo')
ax1.plot(years, new_york_visitors, marker='^', linestyle='-.', color='green', linewidth=2, label='New York')
ax1.plot(years, sydney_visitors, marker='d', linestyle=':', color='purple', linewidth=2, label='Sydney')
ax1.set_title('The Evolution of Popular Travel Destinations\nOver a Decade', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Visitors (millions)', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title='Destinations', loc='upper left', fontsize=12)
ax1.annotate('Tokyo gains popularity', xy=(2014, 17), xytext=(2015, 19),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='red')
ax1.annotate('New York surge', xy=(2018, 28), xytext=(2016, 29),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='green')
ax1.set_xlim(2010, 2019)
ax1.set_ylim(10, 32)

# Bar chart for the average annual growth rate
colors = ['blue', 'red', 'green', 'purple']
ax2.bar(cities, growth_rates, color=colors, alpha=0.7)
ax2.set_title('Average Annual Growth Rate\nof Visitors (2010-2019)', fontsize=16, fontweight='bold')
ax2.set_ylabel('Average Growth Rate (%)', fontsize=14)

# Final adjustments
plt.tight_layout()
plt.show()