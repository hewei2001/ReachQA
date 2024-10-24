import matplotlib.pyplot as plt
import numpy as np

# Define city names
cities = ["New York", "London", "Tokyo", "Paris", "Toronto", "Sydney", "Berlin", "Singapore"]

# Define the number of parks per square mile for each city
parks_per_square_mile = np.array([3.2, 4.1, 2.8, 5.0, 3.5, 6.3, 4.5, 3.7])

# Define bar colors for each city
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f"]

# Set the positions and width for the bars
positions = np.arange(len(cities))
bar_width = 0.6

# Create the bar chart
plt.figure(figsize=(12, 7))
bars = plt.bar(positions, parks_per_square_mile, color=colors, width=bar_width, alpha=0.8, edgecolor='black')

# Adding data labels on top of each bar
for bar, height in zip(bars, parks_per_square_mile):
    plt.text(bar.get_x() + bar.get_width()/2, height - 0.25, f'{height:.1f}', ha='center', va='bottom', color='white', fontsize=10)

# Configure the chart
plt.title('Rise of Urban Green Spaces:\nParks per Square Mile in Major Cities (2023)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('City', fontsize=12)
plt.ylabel('Parks per Square Mile', fontsize=12)
plt.xticks(positions, cities, rotation=45, ha='right')

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the layout to ensure there's no overlap
plt.tight_layout()

# Show the plot
plt.show()