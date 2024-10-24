import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years for the trend analysis
years = np.arange(1990, 2025, 5)

# Define the popularity indices for each fashion style over the decades
grunge_popularity = np.array([15, 60, 30, 10, 5, 3, 2])
hiphop_popularity = np.array([20, 40, 55, 70, 60, 50, 45])
bohemian_popularity = np.array([5, 10, 20, 35, 45, 60, 75])
minimalist_popularity = np.array([2, 5, 15, 25, 35, 45, 60])

# Set up the plot with subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Fashion Trend Popularity Over the Decades\n(1990-2020)', fontsize=16, fontweight='bold', color='darkslategray')

# Create a smooth line for each trend
def smooth_line(years, popularity):
    years_smooth = np.linspace(years.min(), years.max(), 300)
    spl = make_interp_spline(years, popularity, k=3)
    return years_smooth, spl(years_smooth)

# Main combined plot
axs[0, 0].plot(*smooth_line(years, grunge_popularity), linestyle='-', color='#4B0082', label='Grunge')
axs[0, 0].plot(*smooth_line(years, hiphop_popularity), linestyle='--', color='#FF4500', label='Hip-Hop')
axs[0, 0].plot(*smooth_line(years, bohemian_popularity), linestyle='-.', color='#32CD32', label='Bohemian')
axs[0, 0].plot(*smooth_line(years, minimalist_popularity), linestyle=':', color='#4682B4', label='Minimalist')
axs[0, 0].set_xlabel('Year', fontsize=12)
axs[0, 0].set_ylabel('Popularity Index', fontsize=12)
axs[0, 0].set_xticks(years)
axs[0, 0].set_yticks(range(0, 101, 10))
axs[0, 0].legend(loc='upper left', fontsize=10)
axs[0, 0].grid(True, linestyle='--', linewidth=0.5, color='gray')

# Highlight specific points
axs[0, 0].annotate('Peak of Grunge', xy=(1995, 60), xytext=(2000, 70),
                   arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')
axs[0, 0].fill_between(years, minimalist_popularity, color='#B0E0E6', alpha=0.3)

# Subplot for Grunge Trend
axs[0, 1].bar(years, grunge_popularity, color='#4B0082', alpha=0.7)
axs[0, 1].set_title('Grunge Popularity', fontsize=12)
axs[0, 1].set_xlabel('Year', fontsize=10)
axs[0, 1].set_ylabel('Popularity Index', fontsize=10)

# Subplot for Hip-Hop Trend
axs[1, 0].scatter(years, hiphop_popularity, color='#FF4500', marker='s')
axs[1, 0].set_title('Hip-Hop Popularity', fontsize=12)
axs[1, 0].set_xlabel('Year', fontsize=10)
axs[1, 0].set_ylabel('Popularity Index', fontsize=10)

# Subplot for Bohemian Trend
axs[1, 1].step(years, bohemian_popularity, color='#32CD32', where='mid')
axs[1, 1].set_title('Bohemian Popularity', fontsize=12)
axs[1, 1].set_xlabel('Year', fontsize=10)
axs[1, 1].set_ylabel('Popularity Index', fontsize=10)

# Adjust the layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show the plot
plt.show()