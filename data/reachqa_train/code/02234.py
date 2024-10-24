import matplotlib.pyplot as plt

# Data for the market share of different cuisines
cuisines = ['Italian', 'Asian Fusion', 'Mexican', 'Middle Eastern', 'American', 'Vegan/Vegetarian']
market_share = [20, 25, 15, 10, 15, 15]

# Colors for each segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot a donut pie chart with explosion for the largest segment
explode = [0, 0.1, 0, 0, 0, 0]
wedges, texts, autotexts = ax.pie(market_share, labels=cuisines, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, shadow=True,
                                  wedgeprops=dict(width=0.3, edgecolor='w'))

# Add a circle at the center to make it a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title
plt.title('The Culinary Evolution of Urban Cuisine:\nMarket Share in 2023', fontsize=14, fontweight='bold', va='bottom')

# Improve the readability of the text
plt.setp(texts, size=12, weight="bold")
plt.setp(autotexts, size=10, weight="bold", color="darkblue")

# Add a legend outside the plot area
ax.legend(wedges, cuisines, title="Cuisines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()