import matplotlib.pyplot as plt
import numpy as np

# Define years and fashion item trends
years = np.arange(2010, 2021)

# Popularity index for each streetwear item
hoodies_popularity = [50, 55, 58, 62, 70, 72, 80, 78, 81, 83, 85]
sneakers_popularity = [40, 42, 45, 48, 55, 60, 65, 67, 68, 70, 75]
graphic_tees_popularity = [30, 35, 40, 42, 48, 50, 55, 53, 57, 60, 63]
oversized_jackets_popularity = [20, 22, 25, 28, 35, 38, 45, 50, 52, 54, 58]

# Plotting the data
plt.figure(figsize=(12, 7))

# Plot lines with markers for each fashion element
plt.plot(years, hoodies_popularity, marker='o', linestyle='-', color='#1f77b4', label='Hoodies', linewidth=2)
plt.plot(years, sneakers_popularity, marker='s', linestyle='-', color='#ff7f0e', label='Sneakers', linewidth=2)
plt.plot(years, graphic_tees_popularity, marker='^', linestyle='-', color='#2ca02c', label='Graphic Tees', linewidth=2)
plt.plot(years, oversized_jackets_popularity, marker='d', linestyle='-', color='#d62728', label='Oversized Jackets', linewidth=2)

# Add title and labels
plt.title('Streetwear Evolution:\nA Decade of Trends (2010-2020)', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Index', fontsize=12)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Set x-ticks and y-ticks
plt.xticks(years, rotation=45)  # Rotate years slightly for better readability
plt.yticks(np.arange(20, 101, step=10))

# Add legend with title and move it to avoid data overlap
plt.legend(loc='upper left', fontsize=10, title='Fashion Elements', title_fontsize='12')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()