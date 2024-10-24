import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2010, 2021)

# Hypothetical digital literacy scores for students across different regions (out of 100)
scores_africa = [45, 47, 50, 53, 55, 57, 60, 62, 65, 67, 70]
scores_asia = [60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80]
scores_europe = [70, 71, 73, 75, 77, 78, 79, 81, 82, 84, 85]
scores_north_america = [75, 76, 78, 80, 81, 83, 85, 86, 88, 89, 90]
scores_south_america = [50, 52, 53, 55, 57, 59, 61, 63, 65, 67, 69]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the digital literacy scores for each region
ax.plot(years, scores_africa, marker='o', label='Africa', linestyle='-', linewidth=2, color='#FF5733')
ax.plot(years, scores_asia, marker='s', label='Asia', linestyle='--', linewidth=2, color='#33FF57')
ax.plot(years, scores_europe, marker='^', label='Europe', linestyle='-.', linewidth=2, color='#3357FF')
ax.plot(years, scores_north_america, marker='d', label='North America', linestyle='-', linewidth=2, color='#F3FF33')
ax.plot(years, scores_south_america, marker='v', label='South America', linestyle=':', linewidth=2, color='#FF33F3')

# Add title and labels with multiple lines in the title for better visibility
ax.set_title('Evolution of Digital Literacy \nin Global Education (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Digital Literacy Score', fontsize=12)

# Customize ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(40, 101, 5))

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend with title
ax.legend(title='Regions', loc='lower right', fontsize=10)

# Automatically adjust layout for better visibility of elements
plt.tight_layout()

# Display the plot
plt.show()