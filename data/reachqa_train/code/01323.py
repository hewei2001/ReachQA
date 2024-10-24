import matplotlib.pyplot as plt
import numpy as np

# Culinary dishes and their ratings
ratings_data = {
    'Risotto (Italy)': [7.5, 8.0, 7.8, 8.5, 8.2, 7.9, 8.0],
    'Sushi (Japan)': [9.0, 8.8, 9.2, 9.1, 9.0, 9.1, 8.9],
    'Tacos (Mexico)': [8.0, 7.8, 8.3, 8.1, 8.4, 8.2, 8.0],
    'Curry (India)': [8.5, 8.3, 8.6, 8.7, 8.2, 8.4, 8.3],
    'Ratatouille (France)': [7.8, 8.0, 7.9, 8.2, 8.3, 8.1, 7.9]
}

# Additional data for line plot
# Let's create a trend over a period of time (e.g., weeks) for each dish
time_period = np.array([1, 2, 3, 4, 5, 6, 7])
average_ratings = {
    'Risotto (Italy)': [7.2, 7.6, 7.8, 8.0, 7.9, 7.7, 8.1],
    'Sushi (Japan)': [8.8, 8.9, 9.0, 9.1, 9.0, 8.9, 9.2],
    'Tacos (Mexico)': [7.5, 7.7, 8.0, 8.1, 8.2, 8.3, 8.4],
    'Curry (India)': [8.0, 8.2, 8.3, 8.5, 8.3, 8.4, 8.6],
    'Ratatouille (France)': [7.4, 7.6, 7.8, 8.0, 8.2, 8.0, 8.3]
}

dishes = list(ratings_data.keys())
ratings = list(ratings_data.values())

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Box plot
box = axs[0].boxplot(ratings, vert=False, patch_artist=True, labels=dishes, notch=True, whis=1.5)
colors = ['lightcoral', 'lightblue', 'lightgreen', 'khaki', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

axs[0].set_title('Culinary Ratings Across\nInternational Dishes', fontsize=14, fontweight='bold', pad=20, loc='center')
axs[0].set_xlabel('Ratings (Scale: 1-10)', fontsize=12)
axs[0].set_ylabel('Dishes', fontsize=12)
axs[0].xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

for i, dish in enumerate(dishes, 1):
    median_value = np.median(ratings[i-1])
    axs[0].text(median_value, i, f'{median_value:.1f}', verticalalignment='center', 
                fontweight='bold', color='black', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

# Line plot
for dish, color in zip(dishes, colors):
    axs[1].plot(time_period, average_ratings[dish], marker='o', linestyle='-', color=color, label=dish)

axs[1].set_title('Trends in Average Ratings\nOver Time', fontsize=14, fontweight='bold', pad=20, loc='center')
axs[1].set_xlabel('Weeks', fontsize=12)
axs[1].set_ylabel('Average Ratings', fontsize=12)
axs[1].legend(loc='upper left', fontsize=9)
axs[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
axs[1].grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()