import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2000, 2024)

# Complex score patterns with a quadratic trend and some variability
scores_africa = 45 + 0.5 * (years - 2000) + 5 * np.sin(0.3 * (years - 2000))
scores_asia = 50 + 0.8 * (years - 2000) + 4 * np.cos(0.2 * (years - 2000))
scores_europe = 55 + 0.7 * (years - 2000) + 3 * np.sin(0.5 * (years - 2000))
scores_north_america = 60 + 0.9 * (years - 2000) + 2 * np.sin(0.4 * (years - 2000))
scores_south_america = 50 + 0.6 * (years - 2000) + 3 * np.cos(0.6 * (years - 2000))
scores_oceania = 52 + 0.75 * (years - 2000) + 3.5 * np.sin(0.35 * (years - 2000))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Plot the digital literacy scores for each region
ax.plot(years, scores_africa, marker='o', label='Africa', linestyle='-', linewidth=2, color='#FF5733')
ax.plot(years, scores_asia, marker='s', label='Asia', linestyle='--', linewidth=2, color='#33FF57')
ax.plot(years, scores_europe, marker='^', label='Europe', linestyle='-.', linewidth=2, color='#3357FF')
ax.plot(years, scores_north_america, marker='d', label='North America', linestyle='-', linewidth=2, color='#F3FF33')
ax.plot(years, scores_south_america, marker='v', label='South America', linestyle=':', linewidth=2, color='#FF33F3')
ax.plot(years, scores_oceania, marker='*', label='Oceania', linestyle='-', linewidth=2, color='#33FFF3')

# Add a secondary y-axis for overall literacy sum
ax2 = ax.twinx()
overall_scores = scores_africa + scores_asia + scores_europe + scores_north_america + scores_south_america + scores_oceania
ax2.plot(years, overall_scores, color='gray', linestyle='--', linewidth=2, label='Total Literacy Score', alpha=0.7)
ax2.set_ylabel('Total Digital Literacy Score', fontsize=12, color='gray')

# Add title and labels
ax.set_title('Complex Patterns in Digital Literacy Scores \nAcross Global Regions (2000-2023)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Average Digital Literacy Score', fontsize=14)

# Customize ticks
ax.set_xticks(np.arange(2000, 2024, 2))
ax.set_yticks(np.arange(40, 101, 5))
ax2.set_yticks(np.arange(300, 550, 50))

# Add grid
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()