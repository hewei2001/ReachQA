import matplotlib.pyplot as plt
import numpy as np

# Define years from 2015 to 2025
years = np.array(list(range(2015, 2026)))

# Percentage of students preferring each language
python_popularity = [20, 25, 30, 35, 42, 48, 55, 60, 66, 70, 75]
javascript_popularity = [30, 28, 27, 25, 23, 22, 20, 19, 18, 17, 15]
java_popularity = [25, 24, 23, 22, 20, 18, 17, 15, 13, 12, 10]
cpp_popularity = [25, 23, 20, 18, 15, 12, 8, 6, 3, 1, 0]

# Calculate cumulative preference percentage for all languages
cumulative_preference = [sum(x) for x in zip(python_popularity, javascript_popularity, java_popularity, cpp_popularity)]

# Create a complex chart with line and area plot
plt.figure(figsize=(14, 8))

# Plot line charts for each programming language
plt.plot(years, python_popularity, marker='o', linestyle='-', color='blue', linewidth=2, label='Python')
plt.plot(years, javascript_popularity, marker='s', linestyle='--', color='green', linewidth=2, label='JavaScript')
plt.plot(years, java_popularity, marker='^', linestyle='-.', color='orange', linewidth=2, label='Java')
plt.plot(years, cpp_popularity, marker='x', linestyle=':', color='red', linewidth=2, label='C++')

# Overlay an area chart for cumulative preference
plt.fill_between(years, 0, cumulative_preference, color='purple', alpha=0.2, label='Cumulative Preference')

# Annotate data points for Python
for (x, y) in zip(years, python_popularity):
    plt.text(x, y + 2, f'{y}%', color='blue', fontsize=9, ha='center')

# Update title and labels to avoid text overlap
plt.title('Evolution of Programming Languages Popularity Among Students\nWith Cumulative Preference Overlay (2015-2025)', fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=13)
plt.ylabel('Student Preference (%)', fontsize=13)

# Customize ticks and layout
plt.xticks(years, rotation=45)
plt.yticks(range(0, 101, 10))

# Add a legend and grid
plt.legend(title='Legend', fontsize=11, loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()