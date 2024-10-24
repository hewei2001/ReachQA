import matplotlib.pyplot as plt

# Define the fruit categories and their market share percentages
fruit_categories = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Berries']
market_shares = [30, 25, 20, 15, 10]

# Specify colors for each fruit category
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create a ring chart using the pie function
wedges, texts, autotexts = ax.pie(
    market_shares,
    labels=fruit_categories,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Customize text properties
plt.setp(autotexts, size=10, weight='bold', color='black')

# Draw a center circle for the ring effect
centre_circle = plt.Circle((0, 0), 0.55, fc='white', edgecolor='black', linewidth=1.25)
fig.gca().add_artist(centre_circle)

# Set chart title
plt.title('Fruitlandia\'s Fruit Export Market Share\n2023', fontsize=16, fontweight='bold')

# Optimize layout to ensure no overlap
plt.tight_layout()

# Add legend outside the chart
ax.legend(
    wedges,
    fruit_categories,
    title="Fruit Categories",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=10,
    title_fontsize='13'
)

# Display the chart
plt.show()