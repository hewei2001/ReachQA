import matplotlib.pyplot as plt
import numpy as np

# Define the years for the trend analysis
years = np.arange(1990, 2025, 5)

# Define the popularity indices for each fashion style over the decades
grunge_popularity = np.array([15, 60, 30, 10, 5, 3, 2])
hiphop_popularity = np.array([20, 40, 55, 70, 60, 50, 45])
bohemian_popularity = np.array([5, 10, 20, 35, 45, 60, 75])
minimalist_popularity = np.array([2, 5, 15, 25, 35, 45, 60])

# Set up the plot
plt.figure(figsize=(12, 6))

# Plot each fashion style
plt.plot(years, grunge_popularity, marker='o', linestyle='-', linewidth=2, color='#4B0082', label='Grunge')
plt.plot(years, hiphop_popularity, marker='s', linestyle='--', linewidth=2, color='#FF4500', label='Hip-Hop')
plt.plot(years, bohemian_popularity, marker='^', linestyle='-.', linewidth=2, color='#32CD32', label='Bohemian')
plt.plot(years, minimalist_popularity, marker='d', linestyle=':', linewidth=2, color='#4682B4', label='Minimalist')

# Customize the plot
plt.title('Fashion Trend Popularity Over the Decades\n(1990-2020)', fontsize=14, fontweight='bold', color='darkslategray')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Index', fontsize=12)
plt.xticks(years)
plt.yticks(range(0, 101, 10))
plt.legend(loc='upper left', fontsize=10, frameon=False)
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, color='gray')

# Add annotations for significant points
plt.annotate('Peak of Grunge', xy=(1995, 60), xytext=(2000, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkred')

# Highlight the rising trend of Minimalism with a filled area
plt.fill_between(years, minimalist_popularity, color='#B0E0E6', alpha=0.3, label='Minimalism Rising')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()