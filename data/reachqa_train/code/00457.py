import matplotlib.pyplot as plt
import numpy as np

# Genres of books
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Biography']

# Average number of books read annually by each demographic group in different genres
teens_books = [12, 4, 8, 15, 3]
young_adults_books = [15, 10, 12, 9, 5]
adults_books = [10, 8, 5, 4, 7]
seniors_books = [5, 12, 7, 3, 10]

# Grouping data for plotting
data = np.array([teens_books, young_adults_books, adults_books, seniors_books])
demographics = ['Teens (13-19)', 'Young Adults (20-35)', 'Adults (36-55)', 'Seniors (56+)']

# Setting the bar width and indices for the grouped bar plot
bar_width = 0.2
indices = np.arange(len(genres))

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

for i, (demographic_data, demographic_label) in enumerate(zip(data, demographics)):
    bars = ax.bar(indices + i * bar_width, demographic_data, width=bar_width, label=demographic_label, color=colors[i])
    
    # Adding data labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}', ha='center', va='bottom', fontsize=9)

# Configuring the chart
ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('Average Number of Books Read', fontsize=12)
ax.set_title('Annual Book Reading Preferences\nAcross Demographics', fontsize=16, color='darkblue')
ax.set_xticks(indices + bar_width * 1.5)
ax.set_xticklabels(genres)
ax.legend(title='Demographic Groups', fontsize='small')

# Adding a grid for better readability
ax.yaxis.grid(True)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the bar chart
plt.show()