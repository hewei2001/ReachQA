import matplotlib.pyplot as plt

# Define book genres and their respective distribution in the library collection
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Biographies']
distribution = [25, 20, 15, 15, 10, 10, 5]

# Colors for each genre
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', '#C2C2F0', '#FFB3E6']

# Emphasize 'Fiction' by exploding it slightly from the pie
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    distribution, 
    labels=genres, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w')  # Add width for a more sector-like pie
)

# Customize the appearance of texts
plt.setp(texts, size=10, weight="bold")
plt.setp(autotexts, size=10, weight="bold", color="white")

# Add a title to the pie chart, splitting it into two lines for clarity
plt.title('Genre Distribution at\nThe Bibliophile\'s Haven', fontsize=14, fontweight='bold', pad=20)

# Create a legend, positioning it outside the pie to keep the chart clear
plt.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure no visual overlap and adjust layout
plt.tight_layout()

# Show the pie chart
plt.show()