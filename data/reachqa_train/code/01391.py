import matplotlib.pyplot as plt
import numpy as np

# Define a broader range of years
years = np.arange(1980, 2021, 2)

# Define popularity data for each genre
fantasy_popularity = 20 + 5 * np.sin(np.linspace(0, 3 * np.pi, len(years))) + np.linspace(0, 5, len(years))
science_fiction_popularity = 30 + 4 * np.sin(np.linspace(0, 3 * np.pi, len(years))) + np.linspace(5, -5, len(years))
mystery_popularity = 25 + 6 * np.cos(np.linspace(0, 3 * np.pi, len(years)))
historical_fiction_popularity = 15 + 4 * np.cos(np.linspace(0, 3 * np.pi, len(years)))
romance_popularity = 18 + 3 * np.sin(np.linspace(0, 3 * np.pi, len(years)))

# Variable error margins
error = np.linspace(2, 5, len(years))

# Create the figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Plot each genre with error bars
axs[0].errorbar(years, fantasy_popularity, yerr=error, fmt='-o', label='Fantasy', color='goldenrod', capsize=4)
axs[0].errorbar(years, science_fiction_popularity, yerr=error, fmt='-^', label='Science Fiction', color='steelblue', capsize=4)
axs[0].errorbar(years, mystery_popularity, yerr=error, fmt='-s', label='Mystery', color='indigo', capsize=4)
axs[0].errorbar(years, historical_fiction_popularity, yerr=error, fmt='-x', label='Historical Fiction', color='darkgreen', capsize=4)
axs[0].errorbar(years, romance_popularity, yerr=error, fmt='-d', label='Romance', color='crimson', capsize=4)

# Customize the first subplot
axs[0].set_title("Book Genre Popularity Trends from 1980 to 2020", fontsize=14, fontweight='bold')
axs[0].set_ylabel("Popularity (%)")
axs[0].legend(loc='upper right', fontsize=10, title='Genres')
axs[0].grid(True, linestyle='--', alpha=0.5)

# Aggregate data for total market share
total_popularity = (fantasy_popularity + science_fiction_popularity + 
                    mystery_popularity + historical_fiction_popularity + romance_popularity)

# Plot the total market share trend
axs[1].plot(years, total_popularity, '-o', color='purple', label='Total Market Share')
axs[1].set_title("Total Book Market Share Over Time", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year")
axs[1].set_ylabel("Total Popularity (%)")
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()