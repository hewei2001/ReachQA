import matplotlib.pyplot as plt
import numpy as np

# Define the cities and their popularity indices over the years
cities = ['New York', 'London', 'Tokyo', 'Melbourne', 'Istanbul']
popularity_2000 = [70, 55, 30, 25, 40]
popularity_2010 = [85, 65, 45, 70, 50]
popularity_2020 = [95, 80, 60, 85, 65]

# Calculate the growth in popularity from 2000 to 2020
growth_2000_2020 = [pop2020 - pop2000 for pop2020, pop2000 in zip(popularity_2020, popularity_2000)]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.2
y_pos = np.arange(len(cities))

# Plot the horizontal bars for each year
ax.barh(y_pos - bar_width, popularity_2000, bar_width, label='2000', color='#99c2ff')
ax.barh(y_pos, popularity_2010, bar_width, label='2010', color='#3399ff')
ax.barh(y_pos + bar_width, popularity_2020, bar_width, label='2020', color='#0066cc')

# Set the labels and title
ax.set_yticks(y_pos)
ax.set_yticklabels(cities, fontsize=12)
ax.set_xlabel('Popularity Index', fontsize=12)
ax.set_title('The Evolution of Coffee Shop Popularity\nAcross Major Cities (2000 - 2020)', fontsize=14, fontweight='bold', pad=20)

# Add a legend
ax.legend(title='Year', loc='lower right', fontsize=10)

# Annotate the growth for each city
for i, growth in enumerate(growth_2000_2020):
    ax.annotate(f'Growth: {growth}', xy=(popularity_2020[i] + 2, i + bar_width), fontsize=10, color='darkblue')

# Add value labels to each bar
for i, value in enumerate(popularity_2000):
    ax.text(value + 1, i - bar_width, str(value), va='center', color='black', fontsize=10)
for i, value in enumerate(popularity_2010):
    ax.text(value + 1, i, str(value), va='center', color='black', fontsize=10)
for i, value in enumerate(popularity_2020):
    ax.text(value + 1, i + bar_width, str(value), va='center', color='black', fontsize=10)

# Enhance plot layout
plt.grid(visible=True, which='major', axis='x', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()