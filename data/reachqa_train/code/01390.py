import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])

# Popularity data for each genre (in percentage)
fantasy_popularity = np.array([25, 30, 40, 35, 45, 50, 55])
science_fiction_popularity = np.array([35, 40, 35, 30, 28, 25, 20])
mystery_popularity = np.array([40, 30, 25, 35, 27, 25, 25])

# Define error margins for each genre
error = np.array([3, 4, 2, 3, 4, 3, 5])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each genre with error bars
ax.errorbar(years, fantasy_popularity, yerr=error, fmt='-o', 
            label='Fantasy', color='goldenrod', capsize=4, capthick=1.5, alpha=0.8)
ax.errorbar(years, science_fiction_popularity, yerr=error, fmt='-^', 
            label='Science Fiction', color='steelblue', capsize=4, capthick=1.5, alpha=0.8)
ax.errorbar(years, mystery_popularity, yerr=error, fmt='-s', 
            label='Mystery', color='indigo', capsize=4, capthick=1.5, alpha=0.8)

# Customizing the plot
ax.set_title("The Evolution of Book Genres\nPopularity from 1990 to 2020", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=13)
ax.set_ylabel("Popularity (%)", fontsize=13)
ax.legend(loc='upper left', fontsize=11, title='Genres')

# Add grid for better readability
ax.grid(visible=True, linestyle='--', alpha=0.5)

# Customize the ticks on x and y axes
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 61, 10))

# Ensure all elements are within the figure's boundary
plt.tight_layout()

# Display the plot
plt.show()