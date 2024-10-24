import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Popularity scores for each genre (values between 0 and 100)
fiction_popularity = [80, 82, 85, 88, 87, 89, 90, 91, 94, 93, 92, 95, 96, 98, 100, 98, 97, 96, 95, 94, 93]
non_fiction_popularity = [60, 61, 63, 65, 68, 70, 72, 74, 76, 75, 77, 78, 79, 81, 83, 85, 88, 90, 91, 93, 95]
science_fiction_popularity = [40, 42, 45, 48, 50, 52, 55, 57, 58, 60, 63, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87]
fantasy_popularity = [30, 32, 35, 38, 40, 43, 46, 48, 50, 53, 55, 58, 60, 62, 64, 67, 69, 72, 75, 78, 80]

# Initialize the plot
plt.figure(figsize=(12, 8))

# Plotting each genre's popularity over the years
plt.plot(years, fiction_popularity, label='Fiction', marker='o', linestyle='-', linewidth=2, color='#FF6347')
plt.plot(years, non_fiction_popularity, label='Non-Fiction', marker='^', linestyle='-', linewidth=2, color='#4682B4')
plt.plot(years, science_fiction_popularity, label='Science Fiction', marker='s', linestyle='-', linewidth=2, color='#32CD32')
plt.plot(years, fantasy_popularity, label='Fantasy', marker='D', linestyle='-', linewidth=2, color='#8A2BE2')

# Add titles and labels
plt.title("Reading Renaissance: Trends in Genre Popularity\nOver Two Decades (2000-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Popularity Score (0-100)', fontsize=12, fontweight='bold')

# Customize the legend
plt.legend(title='Book Genres', fontsize=10, title_fontsize='12', loc='upper left')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Annotate significant trends
plt.annotate('Rising trend in Fiction', xy=(2012, 96), xytext=(2005, 85),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='darkred')

plt.annotate('Non-Fiction Peaks', xy=(2020, 95), xytext=(2015, 85),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold', color='navy')

# Ensure layout does not overlap and display the plot
plt.tight_layout()
plt.show()