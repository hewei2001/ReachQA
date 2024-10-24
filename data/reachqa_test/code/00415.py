import matplotlib.pyplot as plt

# Increased genres and books read by two groups
genres = ['Fiction', 'Non-Fiction', 'Fantasy', 'Biography', 'Sci-Fi', 'Mystery', 
          'Romance', 'History', 'Thriller', 'Horror', 'Short Stories', 'Poetry']
books_read_avid = [24, 18, 32, 10, 16, 20, 14, 8, 28, 12, 10, 6]
books_read_casual = [12, 10, 20, 5, 8, 10, 8, 5, 14, 6, 6, 4]

# Customized colors for two groups
colors_avid = ['skyblue']*len(genres)
colors_casual = ['lightcoral']*len(genres)

# Setting the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Creating grouped bar chart
bar_width = 0.35
index = range(len(genres))

bar1 = ax.bar(index, books_read_avid, bar_width, color=colors_avid, label='Avid Readers')
bar2 = ax.bar([i + bar_width for i in index], books_read_casual, bar_width, color=colors_casual, label='Casual Readers')

# Adding text labels above each bar
for bar in bar1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

for bar in bar2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

# Set plot title and labels
ax.set_title('Comparison of Reading Habits: \nPopularity of Book Genres Among Avid vs Casual Readers')
ax.set_xlabel('Book Genre')
ax.set_ylabel('Number of Books Read')

# Set the x-axis labels to be the genres at the center of the two bar charts
ax.set_xticks([x + bar_width/2 for x in index])
ax.set_xticklabels(genres)
ax.tick_params(axis='x', rotation=60)

# Adding a legend to explain the two groups
ax.legend()

# Automatically adjust image layout
plt.tight_layout()

# Show the plot
plt.show()