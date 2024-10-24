import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Expanded Data
years = np.array(range(1990, 2031))
books_read_physical = np.array([10, 11, 11, 12, 13, 14, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28, 28, 29, 29, 30, 31, 32, 33, 34, 34, 35, 36, 36, 37, 38, 39, 39, 40])
books_read_digital = np.array([0, 1, 2, 3, 5, 6, 8, 10, 13, 15, 18, 20, 23, 25, 28, 30, 33, 35, 38, 40, 43, 45, 48, 50, 53, 55, 58, 60, 63, 65, 68, 70, 73, 75, 78, 80, 83, 85, 88, 90, 93])

# Smooth fitting line for physical books
years_smooth = np.linspace(years.min(), years.max(), 300)
books_spline_physical = make_interp_spline(years, books_read_physical, k=3)
books_smooth_physical = books_spline_physical(years_smooth)

# Smooth fitting line for digital books
books_spline_digital = make_interp_spline(years, books_read_digital, k=3)
books_smooth_digital = books_spline_digital(years_smooth)

# Main Figure
plt.figure(figsize=(14, 8))

# Plotting data
plt.plot(years_smooth, books_smooth_physical, color='blue', linestyle='-', linewidth=2, label='Physical Books Read')
plt.plot(years_smooth, books_smooth_digital, color='red', linestyle='--', linewidth=2, label='Digital Books Read')

# Highlight Data Points
plt.scatter(years, books_read_physical, color='blue', s=50, edgecolors='black', alpha=0.5)
plt.scatter(years, books_read_digital, color='red', s=50, edgecolors='black', alpha=0.5)

# Annotations for key innovations
annotations = {
    1995: "Digital Print", 2000: "E-books", 2005: "Audiobooks", 
    2010: "Smartphones", 2015: "Reading Apps", 2020: "AI Recommendations"
}
for year, innovation in annotations.items():
    plt.annotate(innovation, xy=(year, (books_read_physical[year-1990] + books_read_digital[year-1990]) / 2), 
                 xytext=(year, (books_read_physical[year-1990] + books_read_digital[year-1990]) / 2 + 15),
                 arrowprops=dict(arrowstyle='->', color='grey'),
                 fontsize=9, ha='center')

# Titles and Labels
plt.title("Evolution of Reading Habits\nThe Shift from Physical to Digital (1990-2030)", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Books Read per Year", fontsize=12)

# Customizing x-ticks for better visibility
plt.xticks(np.arange(1990, 2031, 5), fontsize=10, rotation=45)
plt.yticks(fontsize=10)

# Legends and Grid
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()