import matplotlib.pyplot as plt

# Define the categories and their global popularity percentages
cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian', 'Japanese', 'Mediterranean', 'Others']
popularity = [18, 15, 12, 14, 10, 8, 23]  # Fictional data representing popularity in percentages

# Define colors for each cuisine
colors = ['#FF5733', '#33FFBD', '#FFD700', '#FF33A6', '#33A1FF', '#95FF33', '#D3D3D3']

# Explode the largest category slightly for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0)  # Exploding the 'Italian' category

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(popularity, labels=cuisines, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, shadow=True, textprops={'fontsize': 11, 'weight': 'bold'})

# Set the title
ax.set_title("Global Culinary Trends in 2023:\nA Taste of Diversity", fontsize=14, weight='bold', pad=20)

# Customize the legend and place it outside the pie
ax.legend(wedges, cuisines, title='Cuisines', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()