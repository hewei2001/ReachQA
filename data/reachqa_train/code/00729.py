import matplotlib.pyplot as plt
import numpy as np

# Extended Years from 2010 to 2040 for more data points
years = np.arange(2010, 2041)

# Language popularity data over the years (normalized to sum to 100%)
python_popularity = [15, 16, 17, 19, 21, 24, 28, 33, 35, 38, 42, 45, 47, 49, 50, 52, 55, 56, 57, 58, 60, 62, 64, 66, 68, 70, 72, 73, 74, 75, 76]
javascript_popularity = [18, 19, 20, 22, 24, 26, 28, 30, 32, 34, 36, 37, 38, 38, 38, 37, 36, 35, 34, 34, 33, 33, 33, 33, 33, 32, 31, 30, 30, 29, 28]
java_popularity = [25, 25, 24, 23, 22, 22, 21, 20, 19, 18, 18, 17, 16, 15, 14, 13, 12, 12, 11, 11, 10, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6]
cpp_popularity = [20, 18, 17, 16, 15, 14, 14, 13, 12, 11, 10, 10, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 6, 6, 5, 5, 5, 4, 4]
ruby_popularity = [22, 22, 22, 20, 18, 14, 9, 4, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
swift_popularity = [0, 0, 0, 0, 1, 2, 3, 4, 6, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 19, 20, 21, 22, 22, 23, 24, 25, 25, 25, 26, 27]
rust_popularity = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Normalizing to ensure each column sums to 100%
popularity_stack = np.vstack((python_popularity, javascript_popularity, java_popularity, cpp_popularity, ruby_popularity, swift_popularity, rust_popularity))
popularity_stack_normalized = (popularity_stack / np.sum(popularity_stack, axis=0)) * 100

# Initialize plot
fig, ax = plt.subplots(figsize=(14, 8), dpi=100)

# Colors for each language
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb366', '#c2f0c2']

# Plot stacked area chart
ax.stackplot(years, *popularity_stack_normalized,
             labels=['Python', 'JavaScript', 'Java', 'C++', 'Ruby', 'Swift', 'Rust'], colors=colors, alpha=0.9)

# Title and labels
ax.set_title("Programming Language Popularity Evolution\nin Software Development (2010-2040)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)

# Customizing the x-axis
ax.set_xticks(years[::3])
ax.set_xticklabels(years[::3], rotation=45)

# Customize legend
ax.legend(loc='upper left', title='Languages', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Enhance visibility
ax.grid(alpha=0.4)

# Automatically adjust the layout for better spacing
plt.tight_layout()

# Display the chart
plt.show()