import matplotlib.pyplot as plt

# Data for the chart
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Biography', 'Self-Help']
percentages = [30, 25, 15, 10, 10, 5, 5]

# Colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create a pie chart with a circle in the center to make it a ring chart
wedges, texts, autotexts = ax.pie(percentages, labels=genres, autopct='%1.1f%%', startangle=90, 
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'), 
                                  textprops=dict(color="black"))

# Style the texts and autotexts
for text in texts:
    text.set_fontsize(10)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Draw circle for the donut shape
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that the pie is drawn as a circle
ax.axis('equal')  

# Central label within the ring
plt.text(0, 0, 'Litopia\n2023', ha='center', va='center', fontsize=12, fontweight='bold')

# Title
plt.title('Book Genres Published in Litopia, 2023', fontsize=16, fontweight='bold', pad=20)

# Customize the legend
plt.legend(wedges, genres, title="Genres", loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, title_fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()