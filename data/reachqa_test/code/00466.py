import matplotlib.pyplot as plt
import numpy as np

# Data setup
cities = ['New York', 'Berlin', 'Tokyo', 'Copenhagen', 'Barcelona']
green_space = np.array([10, 50, 20, 70, 30])  # Average green space in sq. meters per person
life_satisfaction = np.array([6.5, 8.0, 7.0, 9.0, 7.5])  # Life satisfaction scores
population = np.array([8.4, 3.7, 14.0, 1.3, 5.5])  # Population in millions for sizing

# Create the figure and axes
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Bar Chart for Life Satisfaction
bar_colors = ['#FF6F61', '#6FA3EF', '#66B3B5', '#FFA07A', '#FFB74D']
bars = axs[0].bar(cities, life_satisfaction, color=bar_colors, alpha=0.9)

# Adding annotations for green space in bar chart
for bar, gs in zip(bars, green_space):
    yval = bar.get_height()
    axs[0].annotate(f'Green Space: {gs} sq. m', 
                    xy=(bar.get_x() + bar.get_width() / 2, yval), 
                    xytext=(0, 5), 
                    textcoords='offset points', 
                    ha='center', 
                    fontsize=9, 
                    color='black')

# Set titles and labels for the bar chart
axs[0].set_title('Impact of Urban Green Spaces on City Life Satisfaction\nin 2023', fontsize=14, fontweight='bold')
axs[0].set_ylabel('Life Satisfaction Score (out of 10)', fontsize=12)
axs[0].set_ylim(0, 10)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=15, ha='right')

# Scatter Plot for Green Space vs. Life Satisfaction
axs[1].scatter(green_space, life_satisfaction, s=population * 10, color=bar_colors, alpha=0.6, edgecolor='w')

# Adding a regression line
m, b = np.polyfit(green_space, life_satisfaction, 1)
axs[1].plot(green_space, m * green_space + b, color='black', linestyle='--', label='Trend Line')

# Annotations for scatter plot
for i, city in enumerate(cities):
    axs[1].annotate(city, (green_space[i], life_satisfaction[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Set titles and labels for the scatter plot
axs[1].set_title('Correlation Between Green Space and Life Satisfaction', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Green Space (sq. meters per person)', fontsize=12)
axs[1].set_ylabel('Life Satisfaction Score (out of 10)', fontsize=12)
axs[1].legend(loc='upper left')
axs[1].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()