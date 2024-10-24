import matplotlib.pyplot as plt

# Data Preparation
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Romance']
overall_preference = [35, 25, 20, 10, 10]

age_groups = ['Kids', 'Teens', 'Adults', 'Seniors']
age_distribution = {
    'Fiction': [25, 20, 45, 10],
    'Non-Fiction': [10, 15, 50, 25],
    'Mystery': [5, 15, 55, 25],
    'Science Fiction': [15, 25, 45, 15],
    'Romance': [10, 15, 50, 25],
}

# Colors for genres and age groups
genre_colors = ['#8B008B', '#FF8C00', '#4682B4', '#32CD32', '#FF1493']
age_colors = ['#F4A460', '#00FA9A', '#6495ED', '#FFD700']

# Plotting the donut pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(overall_preference, labels=genres, colors=genre_colors, 
                                  startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'),
                                  autopct='%1.1f%%', pctdistance=0.85)

# Draw the outer ring representing the age distribution
for i, genre in enumerate(genres):
    ax.pie(age_distribution[genre], radius=0.7, colors=age_colors,
           startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'))

# Adding a circle in the middle to create a donut shape
centre_circle = plt.Circle((0,0),0.35,fc='white')
fig.gca().add_artist(centre_circle)

# Customizing text properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Customizing the legend and title
ax.legend(wedges, age_groups, title="Age Groups", loc="center left", bbox_to_anchor=(1, 0.5))
plt.title("The Literary Diet: An Analysis of \nReading Preferences by Genre and Age Group", fontsize=14, weight='bold')

# Optimize layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()