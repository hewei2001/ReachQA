import matplotlib.pyplot as plt
import numpy as np

# Decades from the 1960s to the 2020s
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Popularity data in percentages
science_fiction = [15, 20, 18, 25, 30, 28, 26]
fantasy = [10, 15, 20, 22, 24, 30, 32]
mystery = [30, 25, 20, 18, 15, 10, 8]
romance = [20, 15, 18, 20, 18, 20, 21]
non_fiction = [25, 25, 24, 15, 13, 12, 13]

# Stack the data to prepare for a stacked area plot
data = np.vstack([science_fiction, fantasy, mystery, romance, non_fiction])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot a stacked area chart
ax.stackplot(decades, data, labels=['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Non-Fiction'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

# Add a title and labels
ax.set_title('The Rise and Fall of Literary Genres Over the Decades', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)

# Add a legend outside the plot area to avoid obscuring data
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right')

# Automatically adjust the layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()