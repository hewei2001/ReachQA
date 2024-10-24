import matplotlib.pyplot as plt

# Data for the pie chart
destinations = ['Lunar Surface', 'Mars Base', 'Asteroid Resorts', 'Jupiter Orbit Hotel', 'Saturn Rings Cruise', 'Titan Outpost']
visit_percentages = [40, 30, 15, 5, 5, 5]

# Colors for each segment of the pie chart
colors = ['lightgray', 'red', 'darkorange', 'dodgerblue', 'lightyellow', 'violet']

# Highlight the Mars Base segment
explode = (0, 0.1, 0, 0, 0, 0)  # Only "explode" the Mars Base slice

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(
    visit_percentages,
    labels=destinations,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Set title and description
plt.title('Favorite Destinations for Space Tourism\nin 2040', fontsize=14, fontweight='bold', pad=20)
plt.annotate('Projected space tourism trends.', (0, -1.1), fontsize=10, ha='center')

# Adding a legend outside the pie
plt.legend(
    destinations,
    title='Destinations',
    loc='center left',
    bbox_to_anchor=(1, 0.5)
)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()