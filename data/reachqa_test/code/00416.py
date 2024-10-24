import matplotlib.pyplot as plt
import numpy as np

# Original film ratings data
ratings_data = {
    2013: [7, 6.5, 8, 8.5, 7.5, 6.3, 8.2, 7.8, 6.9, 8.1],
    2014: [7.2, 7.8, 6.9, 8.1, 8.5, 7.3, 6.7, 8.4, 7.6, 6.8],
    2015: [6.9, 7.7, 8.2, 7.1, 7.6, 6.5, 7.8, 8, 7.4, 8.3],
    2016: [8.1, 7.5, 7.9, 7.2, 8.5, 6.6, 8.3, 7.1, 8.2, 7.7],
    2017: [7.4, 7.8, 8, 6.9, 7.3, 8.1, 7.2, 7.6, 8.3, 7.9],
    2018: [8.2, 7.4, 7.8, 8.5, 7.1, 7.6, 8, 7.3, 8.1, 7.9],
    2019: [7.5, 7.7, 8.1, 7.9, 7.3, 7.6, 8, 8.5, 6.9, 8.2],
    2020: [8, 7.4, 7.8, 8.1, 7.6, 7.9, 8.5, 7.3, 8.3, 7.7],
    2021: [7.6, 7.9, 8.3, 7.1, 7.4, 7.7, 8.2, 8.5, 7.8, 8.1],
    2022: [7.7, 8, 8.1, 7.9, 7.4, 7.6, 8.3, 8.5, 7.2, 8],
    2023: [7.8, 8.1, 8.3, 7.9, 7.5, 8.2, 7.6, 7.9, 8.4, 8.2]
}

# Calculate the average rating for each year
average_ratings = {year: np.mean(ratings) for year, ratings in ratings_data.items()}

# Flatten the dictionary into a single list of ratings for the histogram
ratings = [rating for year_ratings in ratings_data.values() for rating in year_ratings]

# Choose an appropriate number of bins for the histogram
bins = np.arange(6, 9.5, 0.5)

# Set the figure size to accommodate two subplots
plt.figure(figsize=(15, 6))

# Plotting the histogram on the first subplot
plt.subplot(1, 2, 1)
n, bins, patches = plt.hist(ratings, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xlabel("Film Rating")
plt.ylabel("Number of Films")
plt.title('Decade of Cinematic Magic\nFilm Festival Ratings 2013-2023')

# Plotting the line plot on the second subplot
plt.subplot(1, 2, 2)
years = list(average_ratings.keys())
avg_ratings = list(average_ratings.values())
plt.plot(years, avg_ratings, marker='o', color='r')
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.title('Trends in Film Ratings Over a Decade')

# Adjust layout to prevent clipping
plt.tight_layout()

# Showing the plots
plt.show()