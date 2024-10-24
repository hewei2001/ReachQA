import matplotlib.pyplot as plt
import numpy as np

# Define the years and office amenities
years = ['2010', '2015', '2020', '2023']
amenities = ['Flex Work Hours', 'Free Snacks', 'Onsite Gym', 'Meditation Rooms', 'Childcare']

# Percentage of startups offering each amenity in given years
amenity_data = np.array([
    [30, 50, 20, 5, 10],   # 2010
    [60, 70, 30, 15, 20],  # 2015
    [80, 85, 50, 30, 35],  # 2020
    [90, 90, 70, 50, 45]   # 2023
])

# Define bar width and x-axis positions for grouped bars
bar_width = 0.15
x = np.arange(len(years))

# Set the color scheme using a colormap
colors = plt.cm.cividis(np.linspace(0.2, 0.8, len(amenities)))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting each amenity with a different color
for i in range(len(amenities)):
    ax.bar(x + i * bar_width, amenity_data[:, i], bar_width, label=amenities[i], color=colors[i], edgecolor='black')

# Set axis labels, title, and x-ticks with rotation
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Startups (%)', fontsize=12)
ax.set_title('The Evolution of Office Amenities in Tech Startups\n(2010-2023)', fontsize=16, weight='bold', pad=15)
ax.set_xticks(x + bar_width * (len(amenities) - 1) / 2)
ax.set_xticklabels(years)
plt.xticks(rotation=45)

# Add data labels on top of each bar
for i in range(len(years)):
    for j in range(len(amenities)):
        ax.text(x[i] + j * bar_width, amenity_data[i, j] + 1, f'{amenity_data[i, j]}%', ha='center', va='bottom', fontsize=9)

# Add a legend to differentiate amenities
ax.legend(title='Office Amenities', fontsize=10, title_fontsize='11', loc='upper left', bbox_to_anchor=(1,1))

# Add a grid on y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent any overlaps and ensure clear visibility of all elements
plt.tight_layout()

# Display the plot
plt.show()