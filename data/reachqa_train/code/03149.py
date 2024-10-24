import numpy as np
import matplotlib.pyplot as plt

# Define the time period: months over 11 years (2010-2020)
months = np.arange(1, 133)  # 11 years * 12 months each

# Define genres
genres = ['Fiction', 'Mystery', 'Science Fiction', 'Non-Fiction', 'Fantasy']

# Create artificial data for each genre
fiction = 15 + 3 * np.sin(np.linspace(0, 10 * np.pi, 132)) + np.linspace(0, 5, 132)
mystery = 12 + 4 * np.sin(np.linspace(0, 6 * np.pi, 132)) + np.linspace(2, 8, 132)
science_fiction = 8 + 5 * np.sin(np.linspace(0, 8 * np.pi, 132)) + np.linspace(1, 7, 132)
non_fiction = 10 + 2 * np.sin(np.linspace(0, 12 * np.pi, 132)) + np.linspace(1, 3, 132)
fantasy = 9 + 4 * np.sin(np.linspace(0, 9 * np.pi, 132)) + np.linspace(1, 6, 132)

# Stack the data for area plotting
data = np.vstack([fiction, mystery, science_fiction, non_fiction, fantasy])

# Create the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(months, data, labels=genres, colors=['lightcoral', 'goldenrod', 'skyblue', 'lightgreen', 'plum'])

# Define plot details
plt.title("Literary Popularity Over Time:\nA Decade of Book Club Preferences", fontsize=16, weight='bold', pad=20)
plt.xlabel("Months from January 2010", fontsize=12)
plt.ylabel("Average Books Read Per Month", fontsize=12)

# Set x-ticks for each year
plt.xticks(np.arange(0, 132, step=12), 
           ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], fontsize=10)
plt.yticks(fontsize=10)

# Adding a legend outside the plot
plt.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adding grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent text from being cut off
plt.tight_layout()

# Show the plot
plt.show()