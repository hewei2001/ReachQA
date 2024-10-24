import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data
years = np.array([1995, 2000, 2005, 2010, 2015, 2020, 2025])
books_read = np.array([10, 12, 15, 20, 28, 30, 35])

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(years, books_read, color='blue', s=100, edgecolors='black', alpha=0.7, label='Data Points')

# Smooth fitting line
years_smooth = np.linspace(years.min(), years.max(), 300)
books_spline = make_interp_spline(years, books_read, k=3)
books_smooth = books_spline(years_smooth)
plt.plot(years_smooth, books_smooth, color='green', linestyle='-', linewidth=2, label='Trend Line')

# Annotations for innovations
annotations = {
    1995: "Digital Print",
    2000: "E-books",
    2005: "Audiobooks",
    2010: "Smartphones",
    2015: "Reading Apps",
    2020: "AI Recommendations"
}

for year, innovation in annotations.items():
    plt.annotate(innovation, xy=(year, books_read[list(years).index(year)]), 
                 xytext=(year+2, books_read[list(years).index(year)] + 5),
                 arrowprops=dict(arrowstyle='->', color='grey'),
                 fontsize=9, rotation=30)

# Labels and Title
plt.title("Impact of Publishing Innovations\non Reader Engagement", fontsize=14)
plt.xlabel("Year of Innovation", fontsize=12)
plt.ylabel("Average Books Read per Year", fontsize=12)
plt.xticks(years, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper left')

# Layout and grid
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show plot
plt.show()