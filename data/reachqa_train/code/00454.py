import matplotlib.pyplot as plt

# Genres and their sales percentages
genres = ['Fantasy', 'Science Fiction', 'Mystery', 'Romance', 'Non-fiction', 'Horror']
sales_percentage = [25, 15, 20, 18, 17, 5]

# Colors for each genre segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create the ring chart
wedges, texts, autotexts = ax.pie(
    sales_percentage, 
    labels=genres, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Customize the text appearance
plt.setp(autotexts, size=10, weight="bold", color="darkslategray")
plt.setp(texts, size=12, weight="bold")

# Title and annotations
plt.title("Market Share of Book Genres\nat Pages & Pixels Digital Bookstore", 
          fontsize=14, fontweight='bold', color='teal', pad=20)

# Draw a circle at the center to transform the pie chart into a ring chart
center_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(center_circle)

# Equal aspect ratio ensures that the pie is drawn as a circle
ax.axis('equal')  

# Automatically adjust layout to fit elements neatly
plt.tight_layout()

# Display the chart
plt.show()