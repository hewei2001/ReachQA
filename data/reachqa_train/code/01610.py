import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for weekly podcast listening hours for different genres over a year
technology = [3, 3.5, 3.8, 4, 3.9, 4.1, 4.2, 4.4, 5, 4.8, 5.1, 5.3, 5.5, 5.6, 5.2, 5.8, 6, 6.5, 6.2, 6.8, 7, 7.3, 7.5, 7.8, 8, 8.2, 8.5, 8.3, 8.7, 9, 8.9, 9.1, 9.3, 9.5, 9.6, 10, 9.8, 10.2, 10.5, 10.8, 11, 11.3, 11.5, 11.2, 11.8, 12, 12.3, 12.5, 12.8, 13, 13.2, 13.5]
comedy = [2, 2.5, 2.8, 3, 2.9, 3.1, 3.3, 3.2, 4, 4.1, 4.3, 4.5, 4.2, 4.8, 5, 5.5, 5.2, 5.3, 5.6, 6, 6.3, 6.5, 6.2, 6.8, 7, 7.2, 7.4, 7.3, 7.8, 8, 8.3, 8.5, 8.7, 8.5, 9, 9.5, 9.8, 9.6, 10, 10.2, 10.5, 10.8, 11, 11.3, 11.5, 11.8, 12, 12.3, 12.6, 12.7, 13, 13.5]
true_crime = [1.5, 1.8, 2, 2.3, 2.1, 2.5, 2.7, 2.8, 3, 3.2, 3.5, 3.3, 3.8, 4, 4.2, 4.5, 4.3, 4.6, 5, 5.3, 5.5, 5.8, 6, 6.2, 6.5, 6.7, 7, 7.2, 7.5, 8, 8.3, 8.5, 8.2, 8.6, 9, 9.1, 9.5, 9.3, 9.8, 10, 10.3, 10.5, 11, 11.2, 11.7, 11.8, 12, 12.5, 12.7, 13, 13.3, 13.5]
history = [1, 1.3, 1.5, 1.7, 2, 2.3, 2.5, 2.7, 3, 3.3, 3.5, 3.7, 4, 4.2, 4.5, 4.7, 5, 5.3, 5.5, 5.8, 6, 6.2, 6.5, 6.7, 7, 7.3, 7.5, 7.8, 8, 8.2, 8.5, 8.7, 8.9, 9.2, 9.5, 9.7, 10, 10.3, 10.5, 10.8, 11, 11.2, 11.5, 11.7, 12, 12.3, 12.5, 12.8, 13, 13.1, 13.3, 13.5]
health_fitness = [1.2, 1.5, 1.8, 2.2, 2.5, 2.7, 3, 3.3, 3.5, 3.8, 4, 4.3, 4.5, 4.8, 5, 5.3, 5.5, 5.8, 6, 6.3, 6.5, 6.8, 7, 7.2, 7.5, 7.7, 8, 8.3, 8.5, 8.7, 9, 9.5, 9.7, 10, 10.5, 10.8, 11, 11.2, 11.5, 11.8, 12, 12.3, 12.5, 12.7, 13, 13.2, 13.5, 13.8, 14, 14.2, 14.5, 14.8]

# Compile data into a list
data = [technology, comedy, true_crime, history, health_fitness]
genres = ['Technology', 'Comedy', 'True Crime', 'History', 'Health & Fitness']

# Set style
sns.set(style="whitegrid")

# Plotting the box plot with additional features
plt.figure(figsize=(12, 8))
box = plt.boxplot(data, patch_artist=True, labels=genres, notch=True, vert=True)

# Customizing box plot appearance
colors = sns.color_palette("pastel", len(genres))
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add jittered strip plot to show distribution
for i, genre_data in enumerate(data, start=1):
    plt.scatter(np.full_like(genre_data, i), genre_data, alpha=0.6, edgecolor='k', linewidth=0.5)

# Add statistical markers
means = [np.mean(genre) for genre in data]
plt.scatter(range(1, len(means) + 1), means, color='black', marker='o', label='Mean')

# Customizing whiskers, caps, medians
plt.setp(box['whiskers'], color='darkgray', linestyle='--')
plt.setp(box['caps'], color='darkgray')
plt.setp(box['medians'], color='black')

# Adding plot title and labels
plt.title('Podcast Listening Evolution:\nWeekly Consumption Hours by Genre', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Podcast Genres', fontsize=12)
plt.ylabel('Listening Hours per Week', fontsize=12)

# Adding grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Adding legend
plt.legend(['Data Points', 'Mean'], loc='upper left')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()