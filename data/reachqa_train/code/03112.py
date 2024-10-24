import numpy as np
import matplotlib.pyplot as plt

# Define the extended time period: months over 20 years (2000-2020)
months = np.arange(1, 241)  # 20 years * 12 months each

# Define an extended list of genres
genres = ['Fiction', 'Mystery', 'Science Fiction', 'Non-Fiction', 'Fantasy', 
          'Historical', 'Romance', 'Thriller', 'Biography']

# Create more complex artificial data for each genre
fiction = 20 + 3 * np.sin(np.linspace(0, 20 * np.pi, 240)) + np.linspace(0, 7, 240)
mystery = 16 + 5 * np.sin(np.linspace(0, 15 * np.pi, 240)) + np.linspace(3, 10, 240) * 0.8
science_fiction = 12 + 4 * np.sin(np.linspace(0, 16 * np.pi, 240)) + np.logspace(0.1, 1, 240) * 0.5
non_fiction = 10 + 2 * np.sin(np.linspace(0, 22 * np.pi, 240)) + np.linspace(2, 5, 240)
fantasy = 11 + 6 * np.sin(np.linspace(0, 13 * np.pi, 240)) + np.sqrt(np.linspace(1, 10, 240))
historical = 8 + 3 * np.cos(np.linspace(0, 19 * np.pi, 240)) + np.linspace(4, 12, 240)
romance = 9 + 4 * np.cos(np.linspace(0, 18 * np.pi, 240)) + np.sqrt(np.linspace(2, 15, 240))
thriller = 10 + 5 * np.cos(np.linspace(0, 21 * np.pi, 240)) + np.log(np.linspace(3, 50, 240))
biography = 7 + 2.5 * np.sin(np.linspace(0, 25 * np.pi, 240)) + np.linspace(3, 8, 240)

# Stack the data for area plotting
data = np.vstack([fiction, mystery, science_fiction, non_fiction, fantasy, 
                  historical, romance, thriller, biography])

# Create the stacked area chart
plt.figure(figsize=(16, 10))
plt.stackplot(months, data, labels=genres, 
              colors=['lightcoral', 'goldenrod', 'skyblue', 'lightgreen', 'plum',
                      'wheat', 'salmon', 'turquoise', 'lavender'])

# Define plot details
plt.title("Literary Popularity Over Two Decades:\nExploration of Book Genres", fontsize=16, weight='bold', pad=20)
plt.xlabel("Months from January 2000", fontsize=12)
plt.ylabel("Average Books Read Per Month", fontsize=12)

# Set x-ticks for each 2 years
plt.xticks(np.arange(0, 241, step=24), 
           ['2000', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016', '2018', '2020'], fontsize=10)
plt.yticks(fontsize=10)

# Adding a legend outside the plot
plt.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adding grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent text from being cut off
plt.tight_layout()

# Show the plot
plt.show()