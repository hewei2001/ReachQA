import matplotlib.pyplot as plt
import numpy as np

# Define the cities and their popularity indices over the years
cities = ['New York', 'London', 'Tokyo', 'Melbourne', 'Istanbul']
popularity_2000 = [70, 55, 30, 25, 40]
popularity_2010 = [85, 65, 45, 70, 50]
popularity_2020 = [95, 80, 60, 85, 65]

# Create additional data for a line chart
years = np.arange(2000, 2021, 1)
popularity_ny_trend = np.interp(years, [2000, 2010, 2020], [70, 85, 95])
popularity_london_trend = np.interp(years, [2000, 2010, 2020], [55, 65, 80])

# Set up the plot with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Coffee Shop Popularity Trends Across Major Cities', fontsize=16, fontweight='bold')

# --- Horizontal Bar Chart ---

bar_width = 0.2
y_pos = np.arange(len(cities))

ax1.barh(y_pos - bar_width, popularity_2000, bar_width, label='2000', color='#99c2ff')
ax1.barh(y_pos, popularity_2010, bar_width, label='2010', color='#3399ff')
ax1.barh(y_pos + bar_width, popularity_2020, bar_width, label='2020', color='#0066cc')

ax1.set_yticks(y_pos)
ax1.set_yticklabels(cities, fontsize=10)
ax1.set_xlabel('Popularity Index', fontsize=12)
ax1.set_title('Evolution (2000 - 2020)', fontsize=14, fontweight='bold', pad=10)

growth_2000_2020 = [pop2020 - pop2000 for pop2020, pop2000 in zip(popularity_2020, popularity_2000)]
for i, growth in enumerate(growth_2000_2020):
    ax1.annotate(f'Growth: {growth}', xy=(popularity_2020[i] + 1, i + bar_width), fontsize=9, color='darkblue')

for i, value in enumerate(popularity_2000):
    ax1.text(value + 0.5, i - bar_width, str(value), va='center', color='black', fontsize=9)
for i, value in enumerate(popularity_2010):
    ax1.text(value + 0.5, i, str(value), va='center', color='black', fontsize=9)
for i, value in enumerate(popularity_2020):
    ax1.text(value + 0.5, i + bar_width, str(value), va='center', color='black', fontsize=9)

ax1.legend(title='Year', loc='lower right', fontsize=10)
ax1.grid(visible=True, which='major', axis='x', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# --- Line Chart ---

ax2.plot(years, popularity_ny_trend, label='New York', color='#ff5733', linewidth=2, marker='o')
ax2.plot(years, popularity_london_trend, label='London', color='#33ff77', linewidth=2, marker='s')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Popularity Index', fontsize=12)
ax2.set_title('Yearly Trend for Selected Cities', fontsize=14, fontweight='bold', pad=10)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(visible=True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Display the plots
plt.show()