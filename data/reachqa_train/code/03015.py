import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Extended years from 2000 to 2025
years = np.arange(2000, 2026, 0.25)  # Quarterly data

# Average number of bicycles per household for each city with extended data
amsterdam_bicycles = np.linspace(1.2, 3.0, len(years)) + np.sin(years/1.5)
berlin_bicycles = np.linspace(0.8, 2.5, len(years)) + np.cos(years/1.2)
copenhagen_bicycles = np.linspace(1.5, 3.3, len(years)) + 0.1 * np.random.randn(len(years))
paris_bicycles = np.linspace(0.5, 2.0, len(years)) + 0.05 * (years - 2000)
vienna_bicycles = np.linspace(0.9, 2.6, len(years)) + 0.2 * np.random.randn(len(years))

# Smooth the data to make trends more visible
amsterdam_smooth = gaussian_filter1d(amsterdam_bicycles, sigma=2)
berlin_smooth = gaussian_filter1d(berlin_bicycles, sigma=2)
copenhagen_smooth = gaussian_filter1d(copenhagen_bicycles, sigma=2)
paris_smooth = gaussian_filter1d(paris_bicycles, sigma=2)
vienna_smooth = gaussian_filter1d(vienna_bicycles, sigma=2)

# Plotting
plt.figure(figsize=(14, 10))

# Plot each city's data with different styles
plt.plot(years, amsterdam_smooth, marker='o', label='Amsterdam', linestyle='-', linewidth=2, color='blue')
plt.plot(years, berlin_smooth, marker='s', label='Berlin', linestyle='--', linewidth=2, color='green')
plt.plot(years, copenhagen_smooth, marker='^', label='Copenhagen', linestyle='-.', linewidth=2, color='red')
plt.plot(years, paris_smooth, marker='d', label='Paris', linestyle=':', linewidth=2, color='purple')
plt.plot(years, vienna_smooth, marker='x', label='Vienna', linestyle='-', linewidth=2, color='orange')

# Annotate significant points with a larger change
for (year, bicycle_count, label) in zip(years[::20], amsterdam_smooth[::20], ["Rise", "Peak", "Decline"]):
    plt.annotate(f'{label}\n{bicycle_count:.1f}', xy=(year, bicycle_count), xytext=(year+1, bicycle_count+0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, ha='center')

# Customize plot
plt.title('Trends in Average Number of Bicycles Per Household\nin European Cities (2000-2025)', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Number of Bicycles', fontsize=12)
plt.xticks(np.arange(2000, 2026, 2), rotation=45)
plt.ylim(0, 4)
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend(title='City', loc='upper left', fontsize=10)

# Adjust layout to prevent text overlapping
plt.tight_layout()

# Display the plot
plt.show()