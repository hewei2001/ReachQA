import matplotlib.pyplot as plt

# Define cuisine categories and popularity percentages
cuisines = ['Italian', 'Japanese', 'Mexican', 'Indian', 'Thai', 'French', 'Chinese', 'Mediterranean']
cuisine_popularity = [18, 14, 15, 12, 10, 11, 13, 7]

# Define colors for each segment
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#ff6666', '#c4e17f']

# Define explosion to emphasize the most popular cuisine
explode = [0.1 if cuisine == 'Italian' else 0 for cuisine in cuisines]

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(cuisine_popularity, explode=explode, labels=cuisines, colors=colors, autopct='%1.1f%%',
                                  startangle=140, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

# Draw a circle at the center to transform the pie into a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Add aesthetic adjustments
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11)
ax.set_title('2023 Culinary Trends:\nGlobal Cuisine Preferences in a Modern Food Festival', size=16, weight='bold', ha='center')

# Adding a legend to identify each cuisine
ax.legend(wedges, cuisines, title="Cuisines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure the layout is neat and components do not overlap
plt.tight_layout()

# Display the chart
plt.show()