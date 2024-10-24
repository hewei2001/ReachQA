import matplotlib.pyplot as plt

# Define the tea flavors and their respective popularity percentages
flavors = ['Jasmine', 'Hibiscus', 'Chamomile', 'Earl Grey', 'Matcha', 'Oolong']
popularity = [25, 20, 15, 15, 15, 10]

# Assign distinct colors to each flavor
colors = ['#FFB6C1', '#FF69B4', '#87CEFA', '#9370DB', '#90EE90', '#FFD700']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(popularity, labels=flavors, autopct='%1.1f%%', startangle=140,
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3), shadow=True)

# Customizing text properties for clarity
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Add a central circle to complete the donut appearance
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(center_circle)

# Set the title with a creative multi-line approach
ax.set_title('2023 Beverage Industry Survey:\nPreferences on Exotic Tea Flavors', fontsize=16, weight='bold', va='bottom')

# Legend positioned outside of the chart
ax.legend(wedges, flavors, title='Tea Flavors', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout for neatness
plt.tight_layout()

# Display the plot
plt.show()