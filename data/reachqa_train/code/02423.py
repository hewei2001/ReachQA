import matplotlib.pyplot as plt
import numpy as np

# Define data for the classical works by age group
pride_and_prejudice_ages = [25, 27, 28, 30, 32, 35, 36, 40, 42, 45]
the_odyssey_ages = [18, 20, 22, 24, 25, 27, 30, 32, 35, 40, 42, 45]
nineteen_eighty_four_ages = [20, 22, 23, 25, 27, 28, 30, 35, 38, 40, 45, 50]

# Combine data into a list
data = [pride_and_prejudice_ages, the_odyssey_ages, nineteen_eighty_four_ages]

# Define book names for labels
books = ["Pride and Prejudice", "The Odyssey", "1984"]

# Create the horizontal box plot
plt.figure(figsize=(12, 7))
box_plot = plt.boxplot(data, vert=False, patch_artist=True, notch=True, 
                       boxprops=dict(facecolor='lightblue', color='blue', alpha=0.6),
                       whiskerprops=dict(color='blue', linewidth=1.5),
                       capprops=dict(color='blue', linewidth=1.5),
                       medianprops=dict(color='darkblue', linewidth=1.5),
                       flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5))

# Add title and labels
plt.title("Classical Literature Appreciation Across Ages", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Age Group", fontsize=12)
plt.yticks(range(1, len(books) + 1), books, fontsize=12)

# Customize grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add notes for context
plt.annotate('Diverse Readership', xy=(30, 1), xytext=(35, 1.8),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

plt.annotate('Wide Age Range', xy=(35, 2), xytext=(40, 2.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

plt.annotate('Youth Interest\nRising', xy=(22, 3), xytext=(26, 2.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()