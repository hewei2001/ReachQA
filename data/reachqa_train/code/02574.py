import matplotlib.pyplot as plt
import numpy as np

# Define the years for our chart
years = np.arange(2000, 2024)

# Data: Coffee consumption in millions of tons
north_america = np.array([5.0, 5.1, 5.2, 5.3, 5.5, 5.6, 5.8, 6.0, 6.2, 6.5, 6.8, 7.0, 7.3, 7.5, 7.7, 7.9, 8.0, 8.2, 8.3, 8.5, 8.6, 8.7, 8.8, 8.9])
europe = np.array([9.0, 9.2, 9.4, 9.5, 9.7, 9.9, 10.1, 10.4, 10.7, 11.0, 11.2, 11.5, 11.7, 12.0, 12.3, 12.5, 12.8, 13.0, 13.3, 13.5, 13.7, 13.9, 14.0, 14.2])
asia = np.array([2.0, 2.1, 2.3, 2.5, 2.8, 3.0, 3.3, 3.6, 4.0, 4.5, 5.0, 5.6, 6.2, 6.9, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0])
south_america = np.array([4.0, 4.2, 4.4, 4.6, 4.7, 4.8, 5.0, 5.2, 5.4, 5.7, 5.9, 6.1, 6.3, 6.5, 6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6])
africa = np.array([1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.3, 4.7, 5.0, 5.3, 5.5, 5.7, 5.9, 6.1, 6.3, 6.5])

# Calculate total global coffee consumption
total_consumption = north_america + europe + asia + south_america + africa

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data for each continent
ax.plot(years, north_america, label='North America', marker='o', color='b', linewidth=2)
ax.plot(years, europe, label='Europe', marker='s', color='g', linewidth=2, linestyle='--')
ax.plot(years, asia, label='Asia', marker='^', color='r', linewidth=2, linestyle='-.')
ax.plot(years, south_america, label='South America', marker='d', color='c', linewidth=2, linestyle=':')
ax.plot(years, africa, label='Africa', marker='p', color='m', linewidth=2)

# Overlay: Total global consumption as a filled area plot
ax.fill_between(years, total_consumption, color='lightgrey', alpha=0.3, label='Total Global Consumption')

# Annotations for key events
ax.annotate('Specialty Coffee Rise', xy=(2010, 6.8), xytext=(2006, 7.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')
ax.annotate('Emerging Asian Market', xy=(2020, 10.0), xytext=(2015, 11.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

# Trendlines (moving average over 3 years) for highlighting trends
north_america_trend = np.convolve(north_america, np.ones(3)/3, mode='valid')
europe_trend = np.convolve(europe, np.ones(3)/3, mode='valid')
ax.plot(years[1:-1], north_america_trend, color='b', linestyle='dotted', linewidth=1, alpha=0.8)
ax.plot(years[1:-1], europe_trend, color='g', linestyle='dotted', linewidth=1, alpha=0.8)

# Set title and labels
ax.set_title("The Great Coffee Boom:\nGlobal and Regional Consumption Trends (2000-2023)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Coffee Consumption (in millions of tons)", fontsize=12)

# Add legend
ax.legend(loc='upper left', title='Continents & Global Total', fontsize=10)

# Add grid for readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels
plt.xticks(years[::2], rotation=45)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()