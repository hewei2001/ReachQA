import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2023
years = np.arange(2015, 2024)

# Popularity index data for each age group
teens_popularity = [10, 15, 20, 30, 35, 50, 55, 60, 65]
young_adults_popularity = [25, 30, 35, 40, 55, 70, 75, 80, 85]
adults_popularity = [5, 7, 10, 12, 15, 20, 25, 30, 35]
seniors_popularity = [2, 3, 5, 7, 9, 12, 14, 16, 18]

# Calculating cumulative data for stacking
teens_cumulative = teens_popularity
young_adults_cumulative = np.add(teens_cumulative, young_adults_popularity)
adults_cumulative = np.add(young_adults_cumulative, adults_popularity)
seniors_cumulative = np.add(adults_cumulative, seniors_popularity)

# Plotting the area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot areas for each group, stacked
ax.fill_between(years, 0, teens_cumulative, label='Teens (13-19)', color='#ff9999', alpha=0.7)
ax.fill_between(years, teens_cumulative, young_adults_cumulative, label='Young Adults (20-35)', color='#66b3ff', alpha=0.7)
ax.fill_between(years, young_adults_cumulative, adults_cumulative, label='Adults (36-50)', color='#99ff99', alpha=0.7)
ax.fill_between(years, adults_cumulative, seniors_cumulative, label='Seniors (51+)', color='#ffcc99', alpha=0.7)

# Adding titles and labels
ax.set_title('The Surge of Vintage Fashion:\nA Decade of Style Rediscovered', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)

# Customizing x-axis ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Adding grid lines for clarity
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adding legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()