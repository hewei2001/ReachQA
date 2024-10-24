import matplotlib.pyplot as plt

# Data for box office revenues (in million dollars) for various film genres over the past 10 years
# Slight adjustments made to create a clearer visualization without overlaps
action_revenues = [505, 545, 635, 570, 620, 655, 670, 710, 735, 745]
comedy_revenues = [325, 315, 325, 345, 365, 375, 385, 405, 425, 435]
drama_revenues = [285, 295, 315, 295, 325, 345, 325, 365, 375, 395]
animation_revenues = [455, 465, 485, 475, 515, 515, 535, 575, 565, 605]
horror_revenues = [155, 165, 175, 175, 185, 205, 215, 245, 255, 275]

# Organize the data into a list for the horizontal box plot
data = [action_revenues, comedy_revenues, drama_revenues, animation_revenues, horror_revenues]

# Define the labels for the y-axis
genres = ['Action', 'Comedy', 'Drama', 'Animation', 'Horror']

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the horizontal box plot
boxes = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='#C6E2FF', color='black'),
                   whiskerprops=dict(color='black'),
                   capprops=dict(color='black'),
                   medianprops=dict(color='red'))

# Customize the box colors for differentiation
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#5F9EA0', '#FF4500']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels
ax.set_title('Film Genre Popularity Over the Years:\nAnnual Box Office Revenue Distribution (2013-2022)', 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Revenue (Million Dollars)', fontsize=12)
ax.set_yticklabels(genres, fontsize=12)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend for the colors used in the box plot
for genre, color in zip(genres, colors):
    plt.plot([], [], color=color, label=genre)
plt.legend(title="Film Genres", loc="upper right", fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()