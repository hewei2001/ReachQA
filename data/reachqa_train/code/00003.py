import matplotlib.pyplot as plt
import numpy as np

# Data preparation
genres = ["Action", "Comedy", "Drama", "Sci-Fi", "Animation"]
advertising_budgets = {
    "Action": [50, 70, 85, 100],
    "Comedy": [20, 35, 50, 65],
    "Drama": [15, 30, 45, 60],
    "Sci-Fi": [60, 85, 90, 120],
    "Animation": [25, 40, 55, 70]
}
box_office_revenue = {
    "Action": [200, 250, 320, 400],
    "Comedy": [80, 120, 150, 210],
    "Drama": [60, 110, 140, 180],
    "Sci-Fi": [220, 300, 330, 500],
    "Animation": [90, 150, 200, 260]
}

# Define colors and markers for genres
colors = ['blue', 'green', 'red', 'purple', 'orange']
markers = ['o', 's', 'D', '^', 'v']

# Create the scatter plot
plt.figure(figsize=(12, 8))

for i, genre in enumerate(genres):
    plt.scatter(advertising_budgets[genre], box_office_revenue[genre], 
                color=colors[i], label=genre, s=150, alpha=0.7, 
                edgecolors='w', marker=markers[i])

# Setting title and labels
plt.title('Impact of Advertising Budget on Box Office Revenue\nAcross Various Movie Genres', fontsize=16)
plt.xlabel('Advertising Budget (in millions)', fontsize=12)
plt.ylabel('Box Office Revenue (in millions)', fontsize=12)

# Grid and axis ticks
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(np.arange(0, 130, 10))
plt.yticks(np.arange(0, 550, 50))

# Add legend
plt.legend(title='Genres', loc='upper left', fontsize=10)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()