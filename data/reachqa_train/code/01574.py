import matplotlib.pyplot as plt
import numpy as np

# Define genres and the respective counts representing the number of books
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Mystery', 'Biography', 'Fantasy', 'Self-Help']
counts = [1500, 800, 600, 400, 300, 550, 350]

# Colors for each genre slice
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#ff6666']

# Emphasize the largest genre with explode
explode = (0.1, 0, 0, 0, 0, 0, 0)  

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(counts, explode=explode, labels=genres, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140, pctdistance=0.85)

# Draw a circle at the center of the pie to transform it into a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title that fits the storyline
plt.title('Library Book Genres Distribution:\nDiversity in the Collection', fontsize=14, fontweight='bold')

# Place the legend outside the pie for better readability
plt.legend(genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5))

# Ensure that layout is optimized to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()