import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Romance']
percentages = np.array([30, 25, 15, 10, 10, 10])
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Explode the Fiction sector for emphasis
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(percentages, explode=explode, labels=genres, colors=colors,
                                   autopct='%1.1f%%', startangle=140, shadow=True, pctdistance=0.85)

# Style adjustments for better readability
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Draw a circle for a donut-style pie chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title with line break for better readability
plt.title("Global Reader Preferences Survey: Popularity of Literary Genres in 2023", fontsize=16, fontweight='bold', pad=20)

# Ensure equal aspect ratio for a circular pie chart
plt.axis('equal')

# Add a legend to the right of the plot
plt.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust subplot parameters to fit into the figure area
plt.tight_layout()

# Display the plot
plt.show()