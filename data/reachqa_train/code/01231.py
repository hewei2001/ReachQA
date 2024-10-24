import matplotlib.pyplot as plt
import numpy as np

# Dishes and their popularity percentages
dishes = [
    'Martian Space Stew', 'Venusian Veggie Delight', 'Jovian Juices', 
    'Saturnine Sushi', 'Mercurial Meats', 'Neptunian Noodles', 'Plutonian Pie',
    'Ceresian Curry', 'Europa Entree', 'Lunar Luncheon'
]
popularity = [15.5, 12.5, 8.7, 10.3, 9.2, 6.8, 14.4, 7.6, 8.9, 6.1]

# Adjust percentages to ensure they sum up to 100%
popularity = [p * (100 / sum(popularity)) for p in popularity]

# Predicted popularity (just an additional metric for complexity)
predicted_popularity = [p * 1.05 if i % 2 == 0 else p * 0.95 for i, p in enumerate(popularity)]

# Color palette for the pie charts
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#F5C242',
          '#D5A6BD', '#9B2335', '#C94C4C', '#5DA399']

# Explode configuration
explode = [0.1 if i == 0 else 0 for i in range(len(dishes))]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Create a pie chart for actual popularity
wedges1, texts1, autotexts1 = axs[0].pie(
    popularity, labels=dishes, autopct='%1.1f%%', startangle=140, colors=colors,
    explode=explode, wedgeprops=dict(width=0.3), pctdistance=0.85
)
axs[0].set_title("Actual Popularity", fontsize=14, weight='bold', color='#333333', pad=20)
plt.setp(autotexts1, size=9, weight='bold', color='white')
plt.setp(texts1, size=10)

# Create a pie chart for predicted popularity
wedges2, texts2, autotexts2 = axs[1].pie(
    predicted_popularity, labels=dishes, autopct='%1.1f%%', startangle=140, colors=colors,
    explode=explode, wedgeprops=dict(width=0.3), pctdistance=0.85
)
axs[1].set_title("Predicted Popularity", fontsize=14, weight='bold', color='#333333', pad=20)
plt.setp(autotexts2, size=9, weight='bold', color='white')
plt.setp(texts2, size=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()