import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

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
fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Set background gradient
ax.set_facecolor('#f0f8ff')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Bars with patterns
patterns = ["", "//", "\\\\", "xx"]

for i, (demographic_data, demographic_label) in enumerate(zip(data, demographics)):
    bars = ax.bar(indices + i * bar_width, demographic_data, width=bar_width, label=demographic_label, 
                  color=colors[i], hatch=patterns[i])
    
    # Adding data labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}', ha='center', va='bottom', fontsize=10)

# Configuring the chart
ax.set_xlabel('Genres', fontsize=13)
ax.set_ylabel('Average Number of Books Read', fontsize=13)
ax.set_title('Annual Book Reading Preferences\nAcross Demographic Groups', fontsize=18, color='darkblue', pad=20)
ax.set_xticks(indices + bar_width * 1.5)
ax.set_xticklabels(genres, rotation=30, ha='right', fontsize=11)
ax.legend(title='Demographic Groups', fontsize='small', loc='upper right')

# Add a small data table
table_data = np.transpose(data)
table_rows = ['Teens', 'Young Adults', 'Adults', 'Seniors']
table_columns = genres
the_table = ax.table(cellText=table_data,
                     rowLabels=table_columns,
                     colLabels=table_rows,
                     cellLoc='center',
                     loc='bottom',
                     bbox=[0.0, -0.45, 1.0, 0.25])

# Automatically adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)

# Display the bar chart
plt.show()