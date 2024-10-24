import matplotlib.pyplot as plt
import numpy as np

# Extend the years from 2000 to 2023
years = np.arange(2000, 2024)

# Generate popularity index data for each age group with non-linear and complex patterns
teens_popularity = np.sin(np.linspace(0, 3 * np.pi, len(years))) * 20 + np.linspace(10, 30, len(years))
young_adults_popularity = np.log(np.linspace(1, 40, len(years))) * 20
adults_popularity = np.linspace(5, 35, len(years)) ** 0.5 * 10
seniors_popularity = np.log(np.linspace(1, 50, len(years))) * 15
middle_aged_adults_popularity = np.linspace(1, 20, len(years)) ** 1.5

# Calculating cumulative data for stacking
teens_cumulative = teens_popularity
young_adults_cumulative = teens_cumulative + young_adults_popularity
adults_cumulative = young_adults_cumulative + adults_popularity
middle_aged_adults_cumulative = adults_cumulative + middle_aged_adults_popularity
seniors_cumulative = middle_aged_adults_cumulative + seniors_popularity

# Create subplots for the main plot and a secondary metric
fig, ax = plt.subplots(figsize=(14, 9))

# Plot areas for each group, stacked
ax.fill_between(years, 0, teens_cumulative, label='Teens (13-19)', color='#ff9999', alpha=0.6)
ax.fill_between(years, teens_cumulative, young_adults_cumulative, label='Young Adults (20-35)', color='#66b3ff', alpha=0.6)
ax.fill_between(years, young_adults_cumulative, adults_cumulative, label='Adults (36-50)', color='#99ff99', alpha=0.6)
ax.fill_between(years, adults_cumulative, middle_aged_adults_cumulative, label='Middle-aged Adults (51-65)', color='#c2c2f0', alpha=0.6)
ax.fill_between(years, middle_aged_adults_cumulative, seniors_cumulative, label='Seniors (66+)', color='#ffcc99', alpha=0.6)

# Adding titles and labels with line breaks for clarity
ax.set_title('The Evolution of Fashion Trends:\nComplex Interplay Among Age Groups (2000-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)

# Customizing x-axis ticks
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45, ha='right')

# Adding grid lines for clarity
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adding legend outside the plot area
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=10)

# Adding a secondary y-axis for the rate of change
ax2 = ax.twinx()
popularity_rate_of_change = np.gradient(seniors_cumulative)
ax2.plot(years, popularity_rate_of_change, label='Rate of Change', color='black', linestyle='--', linewidth=2)
ax2.set_ylabel('Rate of Change', fontsize=12, color='black')
ax2.tick_params(axis='y', colors='black')

# Adding legend for the secondary y-axis
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()