import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Data for Elysium Literary Festival
years = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Years since the festival started

# Average ratings for each genre
fiction_ratings = np.array([7.8, 8.0, 7.7, 8.2, 8.5, 8.1, 8.6, 8.8, 9.0, 8.9, 9.1])
non_fiction_ratings = np.array([6.5, 6.7, 7.0, 6.9, 7.2, 7.1, 7.3, 7.5, 7.6, 7.7, 7.8])
mystery_ratings = np.array([7.0, 7.3, 7.1, 7.5, 7.8, 8.0, 7.9, 8.1, 8.3, 8.4, 8.5])
sci_fi_ratings = np.array([8.2, 8.3, 8.1, 8.4, 8.6, 8.5, 8.7, 8.9, 9.2, 9.1, 9.3])
fantasy_ratings = np.array([8.0, 8.1, 7.9, 8.3, 8.2, 8.4, 8.5, 8.6, 8.9, 9.0, 9.2])

# Set up the figure
plt.figure(figsize=(12, 8))
plt.title('Elysium Literary Festival: Genre Ratings Trends\n(Decade Overview)', fontsize=16, fontweight='bold')

# Function to plot data with a smooth fit line
def plot_with_smooth_fit(years, ratings, label, color):
    plt.scatter(years, ratings, color=color, s=100, edgecolor='black', label=label, alpha=0.7)

    # Create smooth fitting using cubic interpolation
    tck = interpolate.splrep(years, ratings, s=1)
    x_smooth = np.linspace(years.min(), years.max(), 200)
    y_smooth = interpolate.splev(x_smooth, tck, der=0)
    plt.plot(x_smooth, y_smooth, color=color, linestyle='-', linewidth=2)

# Plot each genre with smooth fits
plot_with_smooth_fit(years, fiction_ratings, 'Fiction', '#1f77b4')
plot_with_smooth_fit(years, non_fiction_ratings, 'Non-Fiction', '#ff7f0e')
plot_with_smooth_fit(years, mystery_ratings, 'Mystery', '#2ca02c')
plot_with_smooth_fit(years, sci_fi_ratings, 'Sci-Fi', '#d62728')
plot_with_smooth_fit(years, fantasy_ratings, 'Fantasy', '#9467bd')

# Label customization
plt.xlabel('Years Since Inception', fontsize=14)
plt.ylabel('Average Rating (Out of 10)', fontsize=14)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend to explain data points and lines
plt.legend(title='Genres', fontsize=11, title_fontsize=12, loc='lower right')

# Adjust layout to ensure no overlapping
plt.tight_layout()

# Display the plot
plt.show()