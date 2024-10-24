import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Define popularity index data for each digital art style
vector_art = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
pixel_art = np.array([20, 22, 25, 35, 45, 55, 60, 62, 65, 70, 72])
concept_art = np.array([50, 48, 47, 46, 45, 44, 43, 42, 40, 38, 35])
cyberpunk = np.array([10, 15, 25, 35, 50, 65, 80, 90, 95, 100, 105])
doodle_art = np.array([5, 10, 25, 40, 60, 65, 55, 45, 40, 35, 30])

# Calculate cumulative values for stacking the area plot
cumulative_vector_art = vector_art
cumulative_pixel_art = cumulative_vector_art + pixel_art
cumulative_concept_art = cumulative_pixel_art + concept_art
cumulative_cyberpunk = cumulative_concept_art + cyberpunk
cumulative_doodle_art = cumulative_cyberpunk + doodle_art

# Calculate the overall average popularity index across all art styles
average_popularity = (vector_art + pixel_art + concept_art + cyberpunk + doodle_art) / 5

# Plotting
plt.figure(figsize=(16, 9))

# Stacked area plot
plt.fill_between(years, 0, cumulative_vector_art, color='#FF9999', label='Vector Art', alpha=0.7)
plt.fill_between(years, cumulative_vector_art, cumulative_pixel_art, color='#66B2FF', label='Pixel Art', alpha=0.7)
plt.fill_between(years, cumulative_pixel_art, cumulative_concept_art, color='#99FF99', label='Concept Art', alpha=0.7)
plt.fill_between(years, cumulative_concept_art, cumulative_cyberpunk, color='#FFCC66', label='Cyberpunk', alpha=0.7)
plt.fill_between(years, cumulative_cyberpunk, cumulative_doodle_art, color='#C299FF', label='Doodle Art', alpha=0.7)

# Overlay line plot for average popularity
plt.plot(years, average_popularity, color='black', linewidth=2, linestyle='--', label='Average Popularity Index')

# Add title and labels
plt.title('The Rise and Fall of Digital Art Styles\nfrom 2010 to 2020 with Average Popularity', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Index', fontsize=12)

# Customize x-axis ticks
plt.xticks(years, rotation=45, ha='right')

# Add grid lines
plt.grid(visible=True, linestyle='--', alpha=0.5, axis='y')

# Add legend
plt.legend(loc='upper left', title='Digital Art Styles', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()