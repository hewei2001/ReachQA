import matplotlib.pyplot as plt
import numpy as np

# Define years from 2015 to 2025
years = np.array(list(range(2015, 2026)))

# Percentage of students preferring each language
python_popularity = [20, 25, 30, 35, 42, 48, 55, 60, 66, 70, 75]
javascript_popularity = [30, 28, 27, 25, 23, 22, 20, 19, 18, 17, 15]
java_popularity = [25, 24, 23, 22, 20, 18, 17, 15, 13, 12, 10]
cpp_popularity = [25, 23, 20, 18, 15, 12, 8, 6, 3, 1, 0]

# Create a line chart with annotations
plt.figure(figsize=(12, 6))

# Plot each language with distinct style
plt.plot(years, python_popularity, marker='o', linestyle='-', color='blue', linewidth=2, label='Python')
plt.plot(years, javascript_popularity, marker='s', linestyle='--', color='green', linewidth=2, label='JavaScript')
plt.plot(years, java_popularity, marker='^', linestyle='-.', color='orange', linewidth=2, label='Java')
plt.plot(years, cpp_popularity, marker='x', linestyle=':', color='red', linewidth=2, label='C++')

# Annotate data points
for (x, y) in zip(years, python_popularity):
    plt.text(x, y + 1, f'{y}%', color='blue', fontsize=8, ha='center')

for (x, y) in zip(years, javascript_popularity):
    plt.text(x, y - 2, f'{y}%', color='green', fontsize=8, ha='center')

for (x, y) in zip(years, java_popularity):
    plt.text(x, y - 2.5, f'{y}%', color='orange', fontsize=8, ha='center')

for (x, y) in zip(years, cpp_popularity):
    plt.text(x, y + 1, f'{y}%', color='red', fontsize=8, ha='center')

# Title and labels
plt.title('Evolution of Programming Languages Popularity\nAmong Students (2015-2025)', fontsize=14, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Student Preference (%)', fontsize=12)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(range(0, 81, 10))

# Add a legend
plt.legend(title='Programming Languages', fontsize=10, loc='upper left')

# Grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()