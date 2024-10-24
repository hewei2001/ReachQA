import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2030
years = np.arange(2010, 2031)

# Language popularity data over the years
python_popularity = [15, 16, 17, 19, 21, 24, 28, 33, 35, 38, 42, 45, 47, 49, 50, 52, 55, 56, 57, 58, 60]
javascript_popularity = [18, 19, 20, 22, 24, 26, 28, 30, 32, 34, 36, 37, 38, 38, 38, 37, 36, 35, 34, 34, 33]
java_popularity = [25, 25, 24, 23, 22, 22, 21, 20, 19, 18, 18, 17, 16, 15, 14, 13, 12, 12, 11, 11, 10]
cpp_popularity = [20, 18, 17, 16, 15, 14, 14, 13, 12, 11, 10, 10, 9, 9, 8, 8, 8, 8, 8, 8, 8]
ruby_popularity = [22, 22, 22, 20, 18, 14, 9, 4, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 7), dpi=100)

# Colors for each language
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot stacked area chart
ax.stackplot(years, python_popularity, javascript_popularity, java_popularity, cpp_popularity, ruby_popularity,
             labels=['Python', 'JavaScript', 'Java', 'C++', 'Ruby'], colors=colors, alpha=0.8)

# Title and labels
ax.set_title("Evolution of Language Popularity\nin Software Development (2010-2030)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Developer Usage', fontsize=12)

# Customizing the x-axis
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)

# Customize legend
ax.legend(loc='upper left', title='Programming Languages', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# Enhance visibility
ax.grid(alpha=0.4)

# Automatically adjust the layout for better spacing
plt.tight_layout()

# Display the chart
plt.show()