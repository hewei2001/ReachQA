import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Popularity data for different literary genres
fantasy = np.array([20, 22, 24, 27, 30, 34, 33, 32, 36, 38, 40])
mystery = np.array([25, 27, 29, 31, 30, 28, 26, 25, 24, 23, 22])
science_fiction = np.array([15, 18, 20, 23, 27, 30, 32, 35, 37, 40, 42])
historical_fiction = np.array([18, 18, 17, 17, 16, 15, 14, 14, 13, 13, 12])
romance = np.array([22, 23, 24, 22, 23, 22, 21, 20, 19, 19, 18])

# Create the stackplot data
genre_data = np.vstack([fantasy, mystery, science_fiction, historical_fiction, romance])

# Set up the plot
plt.figure(figsize=(14, 8))

# Plotting the area chart (stacked)
plt.stackplot(years, genre_data, labels=['Fantasy', 'Mystery', 'Science Fiction', 'Historical Fiction', 'Romance'], 
              colors=['#6a0dad', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Customize the plot
plt.title("Rise and Fall of Literary Genres (2010-2020)\nAn Exploration of Changing Reading Trends", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Popularity Index", fontsize=14)

# Add grid lines and set ticks
plt.grid(linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 141, 20))

# Add legend with a title
plt.legend(loc='upper left', fontsize=10, title="Genres")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()