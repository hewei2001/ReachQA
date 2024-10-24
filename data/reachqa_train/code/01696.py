import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

# Music genres and their preference percentages
genres = ['Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz', 'Electronic', 'Country']
preferences = [25, 20, 15, 10, 10, 10, 10]  # Ensure the total is 100%

# Define colors for each music genre using gradient approach
colors = ['#ff9999', '#ff8080', '#99ccff', '#99ff99', '#ffcc99', '#e6b3ff', '#c2f0c2']

# Explode the 'Pop' slice to highlight it more
explode = (0.1, 0.05, 0.05, 0, 0, 0, 0)

# Create the main figure
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

# Create wedges with 3D effect by using a custom transformation
wedges, texts, autotexts = ax.pie(
    preferences, labels=genres, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(width=0.4, edgecolor='w')
)

# Apply custom border styles to wedges
for w in wedges:
    w.set_linewidth(1.5)
    w.set_edgecolor('darkgrey')

# Customize the appearance of the text with more detail
plt.setp(autotexts, size=11, weight="bold", color="black", bbox=dict(boxstyle="round,pad=0.3", edgecolor='white', facecolor='lightgray'))
plt.setp(texts, size=12, weight="bold")

# Set a title with a line break to fit nicely
ax.set_title("Music Genre Preferences Among\nCollege Students in 2023", fontsize=16, fontweight='bold', pad=20)

# Add a legend to the right of the chart
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Add an inner circle for a donut chart effect and additional info
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
plt.annotate('Total: 100%', xy=(0,0), fontsize=13, ha='center')

# Add tight layout for non-overlapping elements
plt.tight_layout()

# Display the plot
plt.show()